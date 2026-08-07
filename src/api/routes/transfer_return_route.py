from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.repositories.transfer_return_item_repository import (
    TransferReturnItemRepository,
)
from src.repositories.transfer_return_repository import (
    TransferReturnRepository,
)
from src.schemas.transfer_return_schema import (
    TransferReturnAvailableQuantityResponse,
    TransferReturnCreateRequest,
    TransferReturnItemCreateRequest,
    TransferReturnItemResponse,
    TransferReturnResponse,
)
from src.services.transfer_return_service import (
    TransferReturnService,
)
from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
)


router = APIRouter(
    prefix="/transfer-returns",
    tags=["Transfer Returns"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_transfer_return_service(
    session: SessionDependency,
) -> TransferReturnService:
    """
    Monta o serviço de devoluções entre filiais
    com seus repositórios.
    """

    transfer_return_repository = (
        TransferReturnRepository(
            session
        )
    )

    transfer_return_item_repository = (
        TransferReturnItemRepository(
            session
        )
    )

    transfer_repository = TransferRepository(
        session
    )

    transfer_item_repository = (
        TransferItemRepository(
            session
        )
    )

    outbound_transfer_allocation_repository = (
        OutboundTransferAllocationRepository(
            session
        )
    )

    customer_return_allocation_repository = (
        CustomerReturnAllocationRepository(
            session
        )
    )

    return TransferReturnService(
        transfer_return_repository=(
            transfer_return_repository
        ),
        transfer_return_item_repository=(
            transfer_return_item_repository
        ),
        transfer_repository=(
            transfer_repository
        ),
        transfer_item_repository=(
            transfer_item_repository
        ),
        outbound_transfer_allocation_repository=(
            outbound_transfer_allocation_repository
        ),
        customer_return_allocation_repository=(
            customer_return_allocation_repository
        ),
    )


TransferReturnServiceDependency = Annotated[
    TransferReturnService,
    Depends(get_transfer_return_service),
]


NOT_FOUND_MESSAGES = {
    "Transferência não encontrada.",
    "Devolução à filial não encontrada.",
    "Item de transferência não encontrado.",
}


CONFLICT_MESSAGES = {
    (
        "Já existe uma devolução à filial "
        "cadastrada com esse número de Nota "
        "Fiscal de Simples Remessa."
    ),
    (
        "Este item de transferência já foi "
        "adicionado à devolução."
    ),
}


def raise_transfer_return_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio das devoluções
    entre filiais em respostas HTTP.
    """

    message = str(error)

    if message in NOT_FOUND_MESSAGES:
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    if message in CONFLICT_MESSAGES:
        raise HTTPException(
            status_code=(
                status.HTTP_409_CONFLICT
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
    response_model=TransferReturnResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar devolução à filial",
)
def create_transfer_return(
    request: Annotated[
        TransferReturnCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: TransferReturnServiceDependency,
    current_user: AdminOrBuyerUserDependency,
) -> TransferReturnResponse:
    """
    Registra uma nova remessa de cascos
    para a filial que originou a transferência.
    """

    try:
        transfer_return = (
            service.create_transfer_return(
                transfer_id=request.transfer_id,
                dispatch_invoice_number=(
                    request.dispatch_invoice_number
                ),
                dispatch_invoice_series=(
                    request.dispatch_invoice_series
                ),
                issue_date=request.issue_date,
                created_by=current_user.id,
                status=request.status.value,
                notes=request.notes,
            )
        )

        session.commit()
        session.refresh(
            transfer_return
        )

        return TransferReturnResponse.model_validate(
            transfer_return
        )

    except ValueError as error:
        session.rollback()
        raise_transfer_return_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[
        TransferReturnResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar devoluções às filiais",
)
def list_transfer_returns(
    service: TransferReturnServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
) -> list[TransferReturnResponse]:
    """
    Lista todas as devoluções de cascos
    registradas para filiais de origem.
    """

    transfer_returns = (
        service.list_transfer_returns()
    )

    return [
        TransferReturnResponse.model_validate(
            transfer_return
        )
        for transfer_return in transfer_returns
    ]


@router.get(
    "/transfer/{transfer_id}",
    response_model=list[
        TransferReturnResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar devoluções por transferência",
)
def list_transfer_returns_by_transfer(
    service: TransferReturnServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da transferência "
            "de entrada"
        ),
    ),
) -> list[TransferReturnResponse]:
    """
    Lista todas as devoluções vinculadas
    a uma transferência específica.
    """

    try:
        transfer_returns = (
            service.list_by_transfer(
                transfer_id
            )
        )

        return [
            TransferReturnResponse.model_validate(
                transfer_return
            )
            for transfer_return in transfer_returns
        ]

    except ValueError as error:
        raise_transfer_return_http_exception(
            error
        )


@router.get(
    (
        "/transfer-items/"
        "{transfer_item_id}/available-quantity"
    ),
    response_model=(
        TransferReturnAvailableQuantityResponse
    ),
    status_code=status.HTTP_200_OK,
    summary=(
        "Consultar quantidade disponível "
        "para devolução à filial"
    ),
)
def get_transfer_return_available_quantity(
    service: TransferReturnServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_item_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do item recebido "
            "por transferência"
        ),
    ),
) -> TransferReturnAvailableQuantityResponse:
    """
    Retorna a quantidade de cascos devolvida
    pelos clientes e ainda não enviada
    à filial de origem.
    """

    try:
        available_quantity = (
            service.get_available_quantity(
                transfer_item_id
            )
        )

        return (
            TransferReturnAvailableQuantityResponse(
                transfer_item_id=(
                    transfer_item_id
                ),
                available_quantity=(
                    available_quantity
                ),
            )
        )

    except ValueError as error:
        raise_transfer_return_http_exception(
            error
        )


@router.get(
    "/{transfer_return_id}",
    response_model=TransferReturnResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar devolução à filial",
)
def get_transfer_return(
    service: TransferReturnServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da devolução "
            "à filial"
        ),
    ),
) -> TransferReturnResponse:
    """
    Retorna uma devolução à filial
    pelo seu identificador.
    """

    try:
        transfer_return = (
            service.get_transfer_return(
                transfer_return_id
            )
        )

        return TransferReturnResponse.model_validate(
            transfer_return
        )

    except ValueError as error:
        raise_transfer_return_http_exception(
            error
        )


@router.post(
    "/{transfer_return_id}/items",
    response_model=TransferReturnItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à devolução",
)
def add_transfer_return_item(
    request: Annotated[
        TransferReturnItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: TransferReturnServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da devolução "
            "à filial"
        ),
    ),
) -> TransferReturnItemResponse:
    """
    Adiciona à remessa uma quantidade
    pertencente a um item de transferência.
    """

    try:
        transfer_return_item = (
            service.add_item(
                transfer_return_id=(
                    transfer_return_id
                ),
                transfer_item_id=(
                    request.transfer_item_id
                ),
                quantity=request.quantity,
            )
        )

        session.commit()
        session.refresh(
            transfer_return_item
        )

        return (
            TransferReturnItemResponse
            .model_validate(
                transfer_return_item
            )
        )

    except ValueError as error:
        session.rollback()
        raise_transfer_return_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{transfer_return_id}/items",
    response_model=list[
        TransferReturnItemResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar itens da devolução",
)
def list_transfer_return_items(
    service: TransferReturnServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da devolução "
            "à filial"
        ),
    ),
) -> list[TransferReturnItemResponse]:
    """
    Lista os itens pertencentes
    a uma devolução para a filial.
    """

    try:
        transfer_return_items = (
            service.list_items(
                transfer_return_id
            )
        )

        return [
            (
                TransferReturnItemResponse
                .model_validate(
                    transfer_return_item
                )
            )
            for transfer_return_item
            in transfer_return_items
        ]

    except ValueError as error:
        raise_transfer_return_http_exception(
            error
        )