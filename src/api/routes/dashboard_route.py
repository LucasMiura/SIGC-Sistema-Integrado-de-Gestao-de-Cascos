from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.api.dependencies.authorization import (
    OperationalUserDependency,
)
from src.database.connection import get_session
from src.queries.dashboard_query import DashboardQuery
from src.schemas.dashboard_schema import (
    DashboardStockPositionItemResponse,
    DashboardSummaryResponse,
)
from src.services.dashboard_service import (
    DashboardService,
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_dashboard_service(
    session: SessionDependency,
) -> DashboardService:
    """
    Monta o serviço de dashboard utilizando
    uma Query somente de leitura.
    """

    query = DashboardQuery(
        session
    )

    return DashboardService(
        query
    )


DashboardServiceDependency = Annotated[
    DashboardService,
    Depends(get_dashboard_service),
]


def raise_dashboard_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de validação do dashboard
    em respostas HTTP.
    """

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=str(error),
    ) from error


@router.get(
    "",
    response_model=DashboardSummaryResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar dashboard geral",
)
def get_dashboard_summary(
    service: DashboardServiceDependency,
    _current_user: OperationalUserDependency,
    supplier_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra por fornecedor"
        ),
    ),
    part_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra por peça"
        ),
    ),
    origin_type: str | None = Query(
        default=None,
        max_length=20,
        description=(
            "Origem: PURCHASE ou TRANSFER"
        ),
    ),
    deadline_status: str | None = Query(
        default=None,
        max_length=20,
        description=(
            "Classificação do prazo"
        ),
    ),
    date_from: str | None = Query(
        default=None,
        max_length=10,
        description=(
            "Data inicial no formato YYYY-MM-DD"
        ),
    ),
    date_to: str | None = Query(
        default=None,
        max_length=10,
        description=(
            "Data final no formato YYYY-MM-DD"
        ),
    ),
) -> DashboardSummaryResponse:
    """
    Retorna os principais indicadores
    operacionais do SIGC.

    Pode ser utilizado pelo Administrador Master,
    Comprador e Vendedor.
    """

    try:
        summary = service.get_summary(
            supplier_id=supplier_id,
            part_id=part_id,
            origin_type=origin_type,
            deadline_status=(
                deadline_status
            ),
            date_from=date_from,
            date_to=date_to,
        )

        return (
            DashboardSummaryResponse
            .from_dto(
                summary
            )
        )

    except ValueError as error:
        raise_dashboard_http_exception(
            error
        )


@router.get(
    "/stock-position",
    response_model=list[
        DashboardStockPositionItemResponse
    ],
    status_code=status.HTTP_200_OK,
    summary=(
        "Consultar posição de estoque "
        "e cascos por peça"
    ),
)
def get_dashboard_stock_position(
    service: DashboardServiceDependency,
    _current_user:
        OperationalUserDependency,
    supplier_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra por fornecedor"
        ),
    ),
    part_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra por peça"
        ),
    ),
) -> list[
    DashboardStockPositionItemResponse
]:
    """
    Retorna a posição atual de cada peça
    entre estoque, oficina, clientes e
    cascos já retornados.
    """

    try:
        items = (
            service
            .get_stock_position(
                supplier_id=(
                    supplier_id
                ),
                part_id=part_id,
            )
        )

        return [
            DashboardStockPositionItemResponse
            .from_dto(item)
            for item in items
        ]

    except ValueError as error:
        raise_dashboard_http_exception(
            error
        )