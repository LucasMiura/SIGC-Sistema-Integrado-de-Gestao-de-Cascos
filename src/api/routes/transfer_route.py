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
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.schemas.transfer_schema import (
    TransferAvailableQuantityResponse,
    TransferCreateRequest,
    TransferItemCreateRequest,
    TransferItemResponse,
    TransferResponse,
)
from src.services.transfer_service import (
    TransferService,
)
from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
)


router = APIRouter(
    prefix="/transfers",
    tags=["Transfers"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_transfer_service(
    session: SessionDependency,
) -> TransferService:
    """
    Monta o serviço de transferências
    com seus repositórios.
    """

    transfer_repository = TransferRepository(
        session
    )

    transfer_item_repository = (
        TransferItemRepository(
            session
        )
    )

    part_repository = PartRepository(
        session
    )

    return TransferService(
        transfer_repository=(
            transfer_repository
        ),
        transfer_item_repository=(
            transfer_item_repository
        ),
        part_repository=(
            part_repository
        ),
    )


TransferServiceDependency = Annotated[
    TransferService,
    Depends(get_transfer_service),
]


NOT_FOUND_MESSAGES = {
    "Transferência não encontrada.",
    "Item de transferência não encontrado.",
    "Peça não encontrada.",
}


CONFLICT_MESSAGES = {
    (
        "Já existe uma transferência cadastrada "
        "com esse número de Nota Fiscal."
    ),
    (
        "Esta peça já foi adicionada "
        "à transferência."
    ),
    "A transferência já está cancelada.",
}


def raise_transfer_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio da transferência
    em respostas HTTP.
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
    response_model=TransferResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar transferência",
)
def create_transfer(
    request: Annotated[
        TransferCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: TransferServiceDependency,
    current_user: AdminOrBuyerUserDependency,
) -> TransferResponse:
    """
    Registra uma transferência recebida
    de outra filial.
    """

    try:
        transfer = service.create_transfer(
            origin_branch_id=(
                request.origin_branch_id
            ),
            destination_branch_id=(
                request.destination_branch_id
            ),
            invoice_number=(
                request.invoice_number
            ),
            issue_date=request.issue_date,
            created_by=current_user.id,
            status=request.status.value,
        )

        session.commit()
        session.refresh(
            transfer
        )

        return TransferResponse.model_validate(
            transfer
        )

    except ValueError as error:
        session.rollback()
        raise_transfer_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[TransferResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar transferências",
)
def list_transfers(
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
) -> list[TransferResponse]:
    """
    Lista todas as transferências
    cadastradas no sistema.
    """

    transfers = service.list_transfers()

    return [
        TransferResponse.model_validate(
            transfer
        )
        for transfer in transfers
    ]


@router.get(
    "/{transfer_id}",
    response_model=TransferResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar transferência",
)
def get_transfer(
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da transferência"
        ),
    ),
) -> TransferResponse:
    """
    Retorna uma transferência
    pelo seu identificador.
    """

    try:
        transfer = service.get_transfer(
            transfer_id
        )

        return TransferResponse.model_validate(
            transfer
        )

    except ValueError as error:
        raise_transfer_http_exception(
            error
        )


@router.post(
    "/{transfer_id}/items",
    response_model=TransferItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à transferência",
)
def add_transfer_item(
    request: Annotated[
        TransferItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da transferência"
        ),
    ),
) -> TransferItemResponse:
    """
    Adiciona uma peça recebida
    à transferência.
    """

    try:
        transfer_item = service.add_item(
            transfer_id=transfer_id,
            part_id=request.part_id,
            quantity=request.quantity,
            return_deadline_days=(
                request.return_deadline_days
            ),
        )

        session.commit()
        session.refresh(
            transfer_item
        )

        return TransferItemResponse.model_validate(
            transfer_item
        )

    except ValueError as error:
        session.rollback()
        raise_transfer_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{transfer_id}/items",
    response_model=list[
        TransferItemResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar itens da transferência",
)
def list_transfer_items(
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da transferência"
        ),
    ),
) -> list[TransferItemResponse]:
    """
    Lista os itens pertencentes
    a uma transferência.
    """

    try:
        transfer_items = service.list_items(
            transfer_id
        )

        return [
            TransferItemResponse.model_validate(
                transfer_item
            )
            for transfer_item
            in transfer_items
        ]

    except ValueError as error:
        raise_transfer_http_exception(
            error
        )


@router.get(
    "/items/{transfer_item_id}",
    response_model=TransferItemResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar item da transferência",
)
def get_transfer_item(
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_item_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do item "
            "da transferência"
        ),
    ),
) -> TransferItemResponse:
    """
    Retorna um item de transferência
    pelo seu identificador.
    """

    try:
        transfer_item = (
            service.get_transfer_item(
                transfer_item_id
            )
        )

        return TransferItemResponse.model_validate(
            transfer_item
        )

    except ValueError as error:
        raise_transfer_http_exception(
            error
        )


@router.get(
    "/items/{transfer_item_id}/available",
    response_model=(
        TransferAvailableQuantityResponse
    ),
    status_code=status.HTTP_200_OK,
    summary="Consultar saldo disponível",
)
def get_available_quantity(
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_item_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do item "
            "da transferência"
        ),
    ),
) -> TransferAvailableQuantityResponse:
    """
    Retorna a quantidade ainda disponível
    no item da transferência.
    """

    try:
        available_quantity = (
            service.get_available_quantity(
                transfer_item_id
            )
        )

        return (
            TransferAvailableQuantityResponse(
                transfer_item_id=(
                    transfer_item_id
                ),
                available_quantity=(
                    available_quantity
                ),
            )
        )

    except ValueError as error:
        raise_transfer_http_exception(
            error
        )


@router.post(
    "/{transfer_id}/cancel",
    response_model=TransferResponse,
    status_code=status.HTTP_200_OK,
    summary="Cancelar transferência",
)
def cancel_transfer(
    session: SessionDependency,
    service: TransferServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    transfer_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da transferência"
        ),
    ),
) -> TransferResponse:
    """
    Cancela uma transferência sem movimentações.
    """

    try:
        transfer = service.cancel_transfer(
            transfer_id
        )

        session.commit()
        session.refresh(
            transfer
        )

        return TransferResponse.model_validate(
            transfer
        )

    except ValueError as error:
        session.rollback()
        raise_transfer_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise