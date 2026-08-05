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
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)
from src.schemas.supplier_return_schema import (
    SupplierReturnAvailableQuantityResponse,
    SupplierReturnCreateRequest,
    SupplierReturnItemCreateRequest,
    SupplierReturnItemResponse,
    SupplierReturnResponse,
)
from src.services.supplier_return_service import (
    SupplierReturnService,
)


router = APIRouter(
    prefix="/supplier-returns",
    tags=["Supplier Returns"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_supplier_return_service(
    session: SessionDependency,
) -> SupplierReturnService:
    """
    Monta o serviço de remessas aos fornecedores
    com seus repositórios.
    """

    supplier_return_repository = (
        SupplierReturnRepository(
            session
        )
    )

    supplier_return_item_repository = (
        SupplierReturnItemRepository(
            session
        )
    )

    supplier_repository = SupplierRepository(
        session
    )

    purchase_repository = PurchaseRepository(
        session
    )

    purchase_item_repository = (
        PurchaseItemRepository(
            session
        )
    )

    outbound_purchase_allocation_repository = (
        OutboundPurchaseAllocationRepository(
            session
        )
    )

    customer_return_allocation_repository = (
        CustomerReturnAllocationRepository(
            session
        )
    )

    return SupplierReturnService(
        supplier_return_repository=(
            supplier_return_repository
        ),
        supplier_return_item_repository=(
            supplier_return_item_repository
        ),
        supplier_repository=(
            supplier_repository
        ),
        purchase_repository=(
            purchase_repository
        ),
        purchase_item_repository=(
            purchase_item_repository
        ),
        outbound_purchase_allocation_repository=(
            outbound_purchase_allocation_repository
        ),
        customer_return_allocation_repository=(
            customer_return_allocation_repository
        ),
    )


SupplierReturnServiceDependency = Annotated[
    SupplierReturnService,
    Depends(get_supplier_return_service),
]


NOT_FOUND_MESSAGES = {
    "Fornecedor não encontrado.",
    "Remessa ao fornecedor não encontrada.",
    "Item de compra não encontrado.",
    "Compra de origem não encontrada.",
}


CONFLICT_MESSAGES = {
    (
        "Já existe uma remessa cadastrada com esse "
        "número de Nota Fiscal de Simples Remessa."
    ),
    (
        "Este item de compra já foi adicionado "
        "à remessa."
    ),
}


def raise_supplier_return_http_error(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio da remessa
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
    response_model=SupplierReturnResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar remessa ao fornecedor",
)
def create_supplier_return(
    payload: Annotated[
        SupplierReturnCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: SupplierReturnServiceDependency,
) -> SupplierReturnResponse:
    """
    Registra uma nova remessa de cascos
    destinada a um fornecedor.
    """

    try:
        supplier_return = (
            service.create_supplier_return(
                supplier_id=payload.supplier_id,
                dispatch_invoice_number=(
                    payload.dispatch_invoice_number
                ),
                dispatch_invoice_series=(
                    payload.dispatch_invoice_series
                ),
                issue_date=payload.issue_date,
                created_by=payload.created_by,
                status=payload.status.value,
                notes=payload.notes,
            )
        )

        session.commit()
        session.refresh(
            supplier_return
        )

        return SupplierReturnResponse.model_validate(
            supplier_return
        )

    except ValueError as error:
        session.rollback()
        raise_supplier_return_http_error(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[SupplierReturnResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar remessas aos fornecedores",
)
def list_supplier_returns(
    service: SupplierReturnServiceDependency,
) -> list[SupplierReturnResponse]:
    """
    Lista todas as remessas aos fornecedores
    registradas no sistema.
    """

    supplier_returns = (
        service.list_supplier_returns()
    )

    return [
        SupplierReturnResponse.model_validate(
            supplier_return
        )
        for supplier_return in supplier_returns
    ]


@router.get(
    "/{supplier_return_id}",
    response_model=SupplierReturnResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar remessa ao fornecedor",
)
def get_supplier_return(
    service: SupplierReturnServiceDependency,
    supplier_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da remessa "
            "ao fornecedor"
        ),
    ),
) -> SupplierReturnResponse:
    """
    Retorna uma remessa ao fornecedor
    pelo seu identificador.
    """

    try:
        supplier_return = (
            service.get_supplier_return(
                supplier_return_id
            )
        )

        return SupplierReturnResponse.model_validate(
            supplier_return
        )

    except ValueError as error:
        raise_supplier_return_http_error(
            error
        )


@router.post(
    "/{supplier_return_id}/items",
    response_model=SupplierReturnItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à remessa",
)
def add_supplier_return_item(
    payload: Annotated[
        SupplierReturnItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: SupplierReturnServiceDependency,
    supplier_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da remessa "
            "ao fornecedor"
        ),
    ),
) -> SupplierReturnItemResponse:
    """
    Adiciona um item de compra à remessa.

    O sistema verifica o fornecedor, a Nota Fiscal
    de compra de origem e a quantidade disponível.
    """

    try:
        supplier_return_item = (
            service.add_item(
                supplier_return_id=(
                    supplier_return_id
                ),
                purchase_item_id=(
                    payload.purchase_item_id
                ),
                quantity=payload.quantity,
            )
        )

        session.commit()
        session.refresh(
            supplier_return_item
        )

        return (
            SupplierReturnItemResponse
            .model_validate(
                supplier_return_item
            )
        )

    except ValueError as error:
        session.rollback()
        raise_supplier_return_http_error(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{supplier_return_id}/items",
    response_model=list[
        SupplierReturnItemResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar itens da remessa",
)
def list_supplier_return_items(
    service: SupplierReturnServiceDependency,
    supplier_return_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da remessa "
            "ao fornecedor"
        ),
    ),
) -> list[SupplierReturnItemResponse]:
    """
    Lista os itens pertencentes a uma
    remessa ao fornecedor.
    """

    try:
        supplier_return_items = (
            service.list_items(
                supplier_return_id
            )
        )

        return [
            (
                SupplierReturnItemResponse
                .model_validate(
                    supplier_return_item
                )
            )
            for supplier_return_item
            in supplier_return_items
        ]

    except ValueError as error:
        raise_supplier_return_http_error(
            error
        )


@router.get(
    (
        "/purchase-items/"
        "{purchase_item_id}/available-quantity"
    ),
    response_model=(
        SupplierReturnAvailableQuantityResponse
    ),
    status_code=status.HTTP_200_OK,
    summary="Consultar quantidade disponível",
)
def get_supplier_return_available_quantity(
    service: SupplierReturnServiceDependency,
    purchase_item_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do item "
            "da compra de origem"
        ),
    ),
) -> SupplierReturnAvailableQuantityResponse:
    """
    Retorna a quantidade de cascos já recebida
    dos clientes e ainda disponível para uma
    nova remessa ao fornecedor.
    """

    try:
        available_quantity = (
            service.get_available_quantity(
                purchase_item_id
            )
        )

        return (
            SupplierReturnAvailableQuantityResponse(
                purchase_item_id=(
                    purchase_item_id
                ),
                available_quantity=(
                    available_quantity
                ),
            )
        )

    except ValueError as error:
        raise_supplier_return_http_error(
            error
        )