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
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import (
    PartRepository,
)
from src.schemas.customer_return_schema import (
    CustomerReturnCreateRequest,
    CustomerReturnItemCreateRequest,
    CustomerReturnItemResponse,
    CustomerReturnResponse,
)
from src.services.customer_return_service import (
    CustomerReturnService,
)


router = APIRouter(
    prefix="/customer-returns",
    tags=["Customer Returns"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_customer_return_service(
    session: SessionDependency,
) -> CustomerReturnService:
    """
    Monta o serviço de devoluções de clientes
    com seus repositórios.
    """

    customer_return_repository = (
        CustomerReturnRepository(
            session
        )
    )

    customer_return_item_repository = (
        CustomerReturnItemRepository(
            session
        )
    )

    customer_return_allocation_repository = (
        CustomerReturnAllocationRepository(
            session
        )
    )

    outbound_repository = OutboundRepository(
        session
    )

    outbound_item_repository = (
        OutboundItemRepository(
            session
        )
    )

    part_repository = PartRepository(
        session
    )

    return CustomerReturnService(
        customer_return_repository=(
            customer_return_repository
        ),
        customer_return_item_repository=(
            customer_return_item_repository
        ),
        customer_return_allocation_repository=(
            customer_return_allocation_repository
        ),
        outbound_repository=(
            outbound_repository
        ),
        outbound_item_repository=(
            outbound_item_repository
        ),
        part_repository=part_repository,
    )


CustomerReturnServiceDependency = Annotated[
    CustomerReturnService,
    Depends(get_customer_return_service),
]


NOT_FOUND_MESSAGES = {
    "Devolução do cliente não encontrada.",
    "Peça não encontrada.",
    "Saída original não encontrada.",
}


def raise_customer_return_http_error(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio da devolução
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

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    ) from error


@router.post(
    "",
    response_model=CustomerReturnResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar devolução de cliente",
)
def create_customer_return(
    payload: Annotated[
        CustomerReturnCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: CustomerReturnServiceDependency,
) -> CustomerReturnResponse:
    """
    Registra uma nova devolução de casco
    realizada por um cliente.

    A devolução é vinculada à saída original
    por meio do tipo e do número de referência.
    """

    try:
        customer_return = (
            service.create_customer_return(
                return_type=(
                    payload.return_type.value
                ),
                reference_number=(
                    payload.reference_number
                ),
                customer_name=(
                    payload.customer_name
                ),
                created_by=payload.created_by,
                status=payload.status.value,
                notes=payload.notes,
            )
        )

        session.commit()
        session.refresh(customer_return)

        return CustomerReturnResponse.model_validate(
            customer_return
        )

    except ValueError as error:
        session.rollback()
        raise_customer_return_http_error(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[CustomerReturnResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar devoluções de clientes",
)
def list_customer_returns(
    service: CustomerReturnServiceDependency,
) -> list[CustomerReturnResponse]:
    """
    Lista todas as devoluções de clientes
    registradas no sistema.
    """

    customer_returns = (
        service.list_customer_returns()
    )

    return [
        CustomerReturnResponse.model_validate(
            customer_return
        )
        for customer_return in customer_returns
    ]


@router.get(
    "/{customer_return_id}",
    response_model=CustomerReturnResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar devolução de cliente",
)
def get_customer_return(
    service: CustomerReturnServiceDependency,
    customer_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da devolução "
            "do cliente"
        ),
    ),
) -> CustomerReturnResponse:
    """
    Retorna uma devolução de cliente
    pelo seu identificador.
    """

    try:
        customer_return = (
            service.get_customer_return(
                customer_return_id
            )
        )

        return CustomerReturnResponse.model_validate(
            customer_return
        )

    except ValueError as error:
        raise_customer_return_http_error(
            error
        )


@router.post(
    "/{customer_return_id}/items",
    response_model=CustomerReturnItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à devolução",
)
def add_customer_return_item(
    payload: Annotated[
        CustomerReturnItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: CustomerReturnServiceDependency,
    customer_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da devolução "
            "do cliente"
        ),
    ),
) -> CustomerReturnItemResponse:
    """
    Adiciona uma peça à devolução do cliente.

    O sistema valida a saída original e impede
    quantidades superiores ao saldo pendente.
    """

    try:
        customer_return_item = (
            service.add_item(
                customer_return_id=(
                    customer_return_id
                ),
                part_id=payload.part_id,
                quantity=payload.quantity,
            )
        )

        session.commit()
        session.refresh(
            customer_return_item
        )

        return (
            CustomerReturnItemResponse
            .model_validate(
                customer_return_item
            )
        )

    except ValueError as error:
        session.rollback()
        raise_customer_return_http_error(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{customer_return_id}/items",
    response_model=list[
        CustomerReturnItemResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar itens da devolução",
)
def list_customer_return_items(
    service: CustomerReturnServiceDependency,
    customer_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da devolução "
            "do cliente"
        ),
    ),
) -> list[CustomerReturnItemResponse]:
    """
    Lista todos os itens pertencentes
    a uma devolução de cliente.
    """

    try:
        customer_return_items = (
            service.list_customer_return_items(
                customer_return_id
            )
        )

        return [
            (
                CustomerReturnItemResponse
                .model_validate(
                    customer_return_item
                )
            )
            for customer_return_item
            in customer_return_items
        ]

    except ValueError as error:
        raise_customer_return_http_error(
            error
        )