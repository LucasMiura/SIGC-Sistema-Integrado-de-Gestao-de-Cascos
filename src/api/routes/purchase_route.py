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

from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
)
from src.api.dependencies.audit import (
    AuditServiceDependency,
)
from src.database.connection import get_session
from src.repositories.part_repository import (
    PartRepository,
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
from src.schemas.purchase_schema import (
    PurchaseCancelRequest,
    PurchaseCreateRequest,
    PurchaseItemCreateRequest,
    PurchaseItemResponse,
    PurchaseResponse,
    PurchaseUpdateRequest,
)
from src.services.purchase_service import (
    PurchaseService,
)


router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_purchase_service(
    session: SessionDependency,
) -> PurchaseService:
    """
    Cria o serviço de compras com suas
    dependências.
    """

    purchase_repository = PurchaseRepository(
        session
    )

    purchase_item_repository = (
        PurchaseItemRepository(
            session
        )
    )

    supplier_repository = SupplierRepository(
        session
    )

    part_repository = PartRepository(
        session
    )

    return PurchaseService(
        purchase_repository=purchase_repository,
        purchase_item_repository=(
            purchase_item_repository
        ),
        supplier_repository=supplier_repository,
        part_repository=part_repository,
    )


PurchaseServiceDependency = Annotated[
    PurchaseService,
    Depends(get_purchase_service),
]


def raise_purchase_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio
    em respostas HTTP.
    """

    message = str(error)

    not_found_messages = {
        "Compra não encontrada.",
        "Fornecedor não encontrado.",
        "Peça não encontrada.",
    }

    conflict_messages = {
        (
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        ),
        "Esta peça já foi adicionada à compra.",
        "A compra já está cancelada.",
    }

    if message in not_found_messages:
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    if message in conflict_messages:
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
    response_model=PurchaseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar compra",
)
def create_purchase(
    request: Annotated[
        PurchaseCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
    audit_service: AuditServiceDependency,
    current_user: AdminOrBuyerUserDependency,
) -> PurchaseResponse:
    """
    Cadastra uma nova compra.

    O responsável é obtido automaticamente
    do usuário autenticado.
    """

    try:
        purchase = service.create_purchase(
            supplier_id=request.supplier_id,
            invoice_number=request.invoice_number,
            invoice_series=request.invoice_series,
            issue_date=request.issue_date,
            created_by=current_user.id,
            status=request.status,
            notes=request.notes,
        )

        audit_service.register(
            user_id=current_user.id,
            action="CREATE",
            module="PURCHASE",
            entity_type="Purchase",
            entity_id=purchase.id,
            description=(
                "Compra cadastrada."
            ),
            new_values={
                "supplier_id": purchase.supplier_id,
                "invoice_number": (
                    purchase.invoice_number
                ),
                "invoice_series": (
                    purchase.invoice_series
                ),
                "issue_date": purchase.issue_date,
                "received_at": purchase.received_at,
                "status": purchase.status,
                "notes": purchase.notes,
                "created_by": purchase.created_by,
            },
        )

        session.commit()

        session.refresh(
            purchase
        )

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        session.rollback()

        raise_purchase_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[PurchaseResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar compras",
)
def list_purchases(
    service: PurchaseServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra as compras pelo fornecedor"
        ),
    ),
) -> list[PurchaseResponse]:
    """
    Lista todas as compras ou filtra
    por fornecedor.
    """

    try:
        if supplier_id is None:
            purchases = (
                service.list_purchases()
            )

        else:
            purchases = (
                service.list_purchases_by_supplier(
                    supplier_id
                )
            )

        return [
            PurchaseResponse.model_validate(
                purchase
            )
            for purchase in purchases
        ]

    except ValueError as error:
        raise_purchase_http_exception(
            error
        )


@router.get(
    "/{purchase_id}",
    response_model=PurchaseResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar compra",
)
def get_purchase(
    service: PurchaseServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseResponse:
    """
    Retorna uma compra pelo identificador.
    """

    try:
        purchase = service.get_purchase(
            purchase_id
        )

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        raise_purchase_http_exception(
            error
        )


@router.patch(
    "/{purchase_id}",
    response_model=PurchaseResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar compra",
)
def update_purchase(
    request: Annotated[
        PurchaseUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
    audit_service: AuditServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseResponse:
    """
    Atualiza somente os campos enviados.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True
        )

        existing_purchase = service.get_purchase(
            purchase_id
        )

        old_values = {
            field: getattr(
                existing_purchase,
                field,
            )
            for field in update_data
        }

        purchase = service.update_purchase(
            purchase_id=purchase_id,
            **update_data,
        )

        new_values = {
            field: getattr(
                purchase,
                field,
            )
            for field in update_data
        }

        audit_service.register(
            user_id=current_user.id,
            action="UPDATE",
            module="PURCHASE",
            entity_type="Purchase",
            entity_id=purchase.id,
            description="Compra atualizada.",
            old_values=old_values,
            new_values=new_values,
        )

        session.commit()

        session.refresh(
            purchase
        )

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        session.rollback()

        raise_purchase_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{purchase_id}/cancel",
    response_model=PurchaseResponse,
    status_code=status.HTTP_200_OK,
    summary="Cancelar compra",
)
def cancel_purchase(
    request: Annotated[
        PurchaseCancelRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
    audit_service: AuditServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseResponse:
    """
    Cancela uma compra sem apagar
    seu histórico.

    O cancelamento exige justificativa
    e gera registro permanente de auditoria.
    """

    try:
        existing_purchase = service.get_purchase(
            purchase_id
        )

        old_values = {
            "status": existing_purchase.status,
        }

        purchase = service.cancel_purchase(
            purchase_id
        )

        audit_service.register(
            user_id=current_user.id,
            action="CANCEL",
            module="PURCHASE",
            entity_type="Purchase",
            entity_id=purchase.id,
            description="Compra cancelada.",
            old_values=old_values,
            new_values={
                "status": purchase.status,
            },
            justification=request.justification,
        )

        session.commit()

        session.refresh(
            purchase
        )

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        session.rollback()

        raise_purchase_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.post(
    "/{purchase_id}/items",
    response_model=PurchaseItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à compra",
)
def add_purchase_item(
    request: Annotated[
        PurchaseItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
    audit_service: AuditServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseItemResponse:
    """
    Adiciona uma peça à compra.
    """

    try:
        purchase_item = service.add_item(
            purchase_id=purchase_id,
            part_id=request.part_id,
            quantity_purchased=(
                request.quantity_purchased
            ),
        )

        audit_service.register(
            user_id=current_user.id,
            action="CREATE",
            module="PURCHASE",
            entity_type="PurchaseItem",
            entity_id=purchase_item.id,
            description=(
                "Item adicionado à compra."
            ),
            new_values={
                "purchase_id": (
                    purchase_item.purchase_id
                ),
                "part_id": (
                    purchase_item.part_id
                ),
                "quantity_purchased": (
                    purchase_item.quantity_purchased
                ),
                "quantity_available": (
                    purchase_item.quantity_available
                ),
            },
        )

        session.commit()

        session.refresh(
            purchase_item
        )

        return PurchaseItemResponse.model_validate(
            purchase_item
        )

    except ValueError as error:
        session.rollback()

        raise_purchase_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{purchase_id}/items",
    response_model=list[PurchaseItemResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar itens da compra",
)
def list_purchase_items(
    service: PurchaseServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> list[PurchaseItemResponse]:
    """
    Lista os itens vinculados a uma compra.
    """

    try:
        purchase_items = (
            service.list_purchase_items(
                purchase_id
            )
        )

        return [
            PurchaseItemResponse.model_validate(
                purchase_item
            )
            for purchase_item in purchase_items
        ]

    except ValueError as error:
        raise_purchase_http_exception(
            error
        )