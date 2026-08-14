from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.queries.purchase_tracking_query import PurchaseTrackingQuery
from src.schemas.purchase_tracking_schema import (
    PurchaseTrackingResponse,
)
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)
from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
)


router = APIRouter(
    prefix="/purchases",
    tags=["Purchase Tracking"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_purchase_tracking_service(
    session: SessionDependency,
) -> PurchaseTrackingService:
    """
    Monta o Service com suas dependências.

    A rota não cria consultas diretamente. Ela recebe uma sessão,
    cria a Query e injeta a Query no Service.
    """

    query = PurchaseTrackingQuery(session)

    return PurchaseTrackingService(query)


PurchaseTrackingServiceDependency = Annotated[
    PurchaseTrackingService,
    Depends(get_purchase_tracking_service),
]

@router.get(
    "/tracking/by-invoice",
    response_model=PurchaseTrackingResponse,
    status_code=status.HTTP_200_OK,
    summary=(
        "Consultar acompanhamento "
        "pela Nota Fiscal de compra"
    ),
)
def get_purchase_tracking_by_invoice(
    service: PurchaseTrackingServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Query(
        ...,
        gt=0,
        description=(
            "Identificador do fornecedor "
            "da Nota Fiscal"
        ),
    ),
    invoice_number: str = Query(
        ...,
        min_length=1,
        max_length=100,
        pattern=r".*\S.*",
        description=(
            "Número da Nota Fiscal de compra"
        ),
    ),
    invoice_series: str | None = Query(
        default=None,
        max_length=50,
        description=(
            "Série da Nota Fiscal de compra"
        ),
    ),
) -> PurchaseTrackingResponse:
    """
    Retorna o acompanhamento completo
    de uma compra localizada pela Nota Fiscal.

    A identificação utiliza fornecedor,
    número da Nota Fiscal e série.
    """

    try:
        tracking = (
            service
            .get_purchase_tracking_by_invoice(
                supplier_id=supplier_id,
                invoice_number=invoice_number,
                invoice_series=invoice_series,
            )
        )

        return (
            PurchaseTrackingResponse
            .from_dto(
                tracking
            )
        )

    except ValueError as error:
        message = str(error)

        if message == "Compra não encontrada.":
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

@router.get(
    "/{purchase_id}/tracking",
    response_model=PurchaseTrackingResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar acompanhamento de uma compra",
)
def get_purchase_tracking(
    service: PurchaseTrackingServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseTrackingResponse:
    """
    Retorna o acompanhamento completo de uma compra.

    A resposta inclui as quantidades compradas, enviadas,
    devolvidas pelo cliente e devolvidas ao fornecedor.
    """

    try:
        tracking = service.get_purchase_tracking(purchase_id)

        return PurchaseTrackingResponse.from_dto(tracking)

    except ValueError as error:
        message = str(error)

        if message == "Compra não encontrada.":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            ) from error

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        ) from error