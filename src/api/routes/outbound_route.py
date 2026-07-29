from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.schemas.outbound_schema import (
    OutboundCreateRequest,
    OutboundItemCreateRequest,
    OutboundItemResponse,
    OutboundResponse,
    OutboundStatus,
    OutboundUpdateRequest,
)
from src.services.outbound_service import (
    OutboundService,
)


router = APIRouter(
    prefix="/outbounds",
    tags=["Outbounds"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_outbound_service(
    session: SessionDependency,
) -> OutboundService:
    """
    Monta o serviço de saídas com seus repositórios.
    """

    outbound_repository = OutboundRepository(
        session
    )

    outbound_item_repository = (
        OutboundItemRepository(
            session
        )
    )

    allocation_repository = (
        OutboundPurchaseAllocationRepository(
            session
        )
    )

    purchase_item_repository = (
        PurchaseItemRepository(
            session
        )
    )

    part_repository = PartRepository(
        session
    )

    return OutboundService(
        outbound_repository=(
            outbound_repository
        ),
        outbound_item_repository=(
            outbound_item_repository
        ),
        outbound_purchase_allocation_repository=(
            allocation_repository
        ),
        purchase_item_repository=(
            purchase_item_repository
        ),
        part_repository=part_repository,
    )


OutboundServiceDependency = Annotated[
    OutboundService,
    Depends(get_outbound_service),
]


NOT_FOUND_MESSAGES = {
    "Saída não encontrada.",
    "Peça não encontrada.",
    (
        "Item de compra relacionado "
        "à saída não encontrado."
    ),
}


def raise_http_error(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio em erros HTTP.
    """

    message = str(error)

    if message in NOT_FOUND_MESSAGES:
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    ) from error


@router.post(
    "",
    response_model=OutboundResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar uma saída",
)
def create_outbound(
    payload: Annotated[
        OutboundCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: OutboundServiceDependency,
) -> OutboundResponse:
    """
    Cadastra uma nova saída de peças.

    A saída deve possuir uma Ordem de Serviço,
    uma Nota Fiscal de venda ou ambas.
    """

    try:
        outbound = service.create_outbound(
            destination_type=(
                payload.destination_type
            ),
            work_order_number=(
                payload.work_order_number
            ),
            sales_invoice_number=(
                payload.sales_invoice_number
            ),
            created_by=payload.created_by,
            status=payload.status.value,
        )

        session.commit()
        session.refresh(outbound)

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[OutboundResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar saídas",
)
def list_outbounds(
    service: OutboundServiceDependency,
    outbound_status: OutboundStatus | None = Query(
        default=None,
        alias="status",
        description="Filtrar pelo status da saída",
    ),
    destination_type: str | None = Query(
        default=None,
        min_length=1,
        max_length=50,
        description=(
            "Filtrar pelo tipo de destino"
        ),
    ),
) -> list[OutboundResponse]:
    """
    Lista todas as saídas.

    Pode ser utilizado um filtro por status ou
    por tipo de destino. Apenas um filtro pode
    ser enviado por vez.
    """

    try:
        outbounds = service.list_outbounds(
            status=(
                outbound_status.value
                if outbound_status is not None
                else None
            ),
            destination_type=destination_type,
        )

        return [
            OutboundResponse.model_validate(
                outbound
            )
            for outbound in outbounds
        ]

    except ValueError as error:
        raise_http_error(error)


@router.get(
    "/{outbound_id}",
    response_model=OutboundResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar uma saída",
)
def get_outbound(
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundResponse:
    """
    Retorna uma saída pelo identificador.
    """

    try:
        outbound = service.get_outbound(
            outbound_id
        )

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        raise_http_error(error)


@router.patch(
    "/{outbound_id}",
    response_model=OutboundResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar uma saída",
)
def update_outbound(
    payload: Annotated[
        OutboundUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundResponse:
    """
    Atualiza parcialmente uma saída.

    Saídas canceladas não podem ser alteradas.
    O cancelamento deve utilizar o endpoint
    específico.
    """

    try:
        update_data = payload.model_dump(
            exclude_unset=True
        )

        outbound_status = update_data.get(
            "status"
        )

        if outbound_status is not None:
            update_data["status"] = (
                outbound_status.value
            )

        outbound = service.update_outbound(
            outbound_id=outbound_id,
            **update_data,
        )

        session.commit()
        session.refresh(outbound)

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{outbound_id}/cancel",
    response_model=OutboundResponse,
    status_code=status.HTTP_200_OK,
    summary="Cancelar uma saída",
)
def cancel_outbound(
    session: SessionDependency,
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundResponse:
    """
    Cancela uma saída e devolve ao estoque as
    quantidades anteriormente consumidas.
    """

    try:
        outbound = service.cancel_outbound(
            outbound_id
        )

        session.commit()
        session.refresh(outbound)

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.post(
    "/{outbound_id}/items",
    response_model=OutboundItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à saída",
)
def add_outbound_item(
    payload: Annotated[
        OutboundItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundItemResponse:
    """
    Adiciona uma peça à saída.

    A quantidade é consumida automaticamente
    dos itens de compra por ordem FIFO.
    """

    try:
        outbound_item = service.add_item(
            outbound_id=outbound_id,
            part_id=payload.part_id,
            quantity=payload.quantity,
        )

        session.commit()
        session.refresh(outbound_item)

        return (
            OutboundItemResponse.model_validate(
                outbound_item
            )
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{outbound_id}/items",
    response_model=list[OutboundItemResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar itens de uma saída",
)
def list_outbound_items(
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> list[OutboundItemResponse]:
    """
    Lista todos os itens pertencentes a uma saída.
    """

    try:
        outbound_items = (
            service.list_outbound_items(
                outbound_id
            )
        )

        return [
            OutboundItemResponse.model_validate(
                outbound_item
            )
            for outbound_item
            in outbound_items
        ]

    except ValueError as error:
        raise_http_error(error)