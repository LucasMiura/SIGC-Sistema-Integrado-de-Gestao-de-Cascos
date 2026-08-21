from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_SELLER,
)
from src.api.routes.dashboard_route import (
    get_dashboard_service,
    router,
)
from src.database.connection import (
    get_session,
)
from src.dtos.dashboard import (
    DashboardCustomerReturnIndicatorsDTO,
    DashboardDeadlineIndicatorsDTO,
    DashboardStockPositionItemDTO,
    DashboardSummaryDTO,
    DashboardSupplierReturnIndicatorsDTO,
    DashboardTransferReturnIndicatorsDTO,
)
from src.services.dashboard_service import (
    DashboardService,
)


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=DashboardService
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    """
    Cria aplicação isolada com
    um Vendedor autenticado.
    """

    test_app = FastAPI()

    seller_user = SimpleNamespace(
        id=30,
        username="vendedor",
        role_id=3,
        is_active=1,
    )

    seller_role = SimpleNamespace(
        id=3,
        name=ROLE_SELLER,
    )

    def override_get_session():
        yield session

    def override_dashboard_service():
        return service

    def override_get_current_user():
        return seller_user

    session.scalar.return_value = (
        seller_role
    )

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_dashboard_service
    ] = override_dashboard_service

    test_app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    test_app.include_router(
        router
    )

    return test_app


@pytest.fixture
def client(
    app: FastAPI,
) -> TestClient:
    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_summary_dto() -> DashboardSummaryDTO:
    return DashboardSummaryDTO(
        total_origin_count=12,
        total_available_quantity=25,
        deadline=(
            DashboardDeadlineIndicatorsDTO(
                normal_quantity=10,
                attention_quantity=8,
                urgent_quantity=4,
                overdue_quantity=3,
            )
        ),
        customer_returns=(
            DashboardCustomerReturnIndicatorsDTO(
                outbound_quantity=30,
                returned_quantity=20,
                pending_quantity=10,
                pending_origin_count=2,
                partial_origin_count=3,
                completed_origin_count=4,
            )
        ),
        supplier_returns=(
            DashboardSupplierReturnIndicatorsDTO(
                available_quantity=7,
                returned_quantity=5,
                pending_quantity=15,
            )
        ),
        transfer_returns=(
            DashboardTransferReturnIndicatorsDTO(
                available_quantity=4,
                returned_quantity=6,
                pending_quantity=8,
            )
        ),
    )


def create_stock_position_dto() -> tuple[
    DashboardStockPositionItemDTO,
    ...,
]:
    return (
        DashboardStockPositionItemDTO(
            part_id=10,
            part_code="ABC123",
            part_name="Compressor de ar",
            stock_quantity=8,
            workshop_pending_quantity=3,
            customer_pending_quantity=2,
            workshop_returned_quantity=1,
            customer_returned_quantity=2,
            available_core_quantity=3,
        ),
    )


def test_should_return_dashboard_summary(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_summary.return_value = (
        create_summary_dto()
    )

    response = client.get(
        "/dashboard"
    )

    assert response.status_code == 200

    assert response.json() == {
        "total_origin_count": 12,
        "total_available_quantity": 25,
        "deadline": {
            "normal_quantity": 10,
            "attention_quantity": 8,
            "urgent_quantity": 4,
            "overdue_quantity": 3,
        },
        "customer_returns": {
            "outbound_quantity": 30,
            "returned_quantity": 20,
            "pending_quantity": 10,
            "pending_origin_count": 2,
            "partial_origin_count": 3,
            "completed_origin_count": 4,
        },
        "supplier_returns": {
            "available_quantity": 7,
            "returned_quantity": 5,
            "pending_quantity": 15,
        },
        "transfer_returns": {
            "available_quantity": 4,
            "returned_quantity": 6,
            "pending_quantity": 8,
        },
    }

    service.get_summary.assert_called_once_with(
        supplier_id=None,
        part_id=None,
        origin_type=None,
        deadline_status=None,
        date_from=None,
        date_to=None,
    )


def test_should_send_dashboard_filters_to_service(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_summary.return_value = (
        create_summary_dto()
    )

    response = client.get(
        "/dashboard",
        params={
            "supplier_id": 5,
            "part_id": 10,
            "origin_type": "purchase",
            "deadline_status": "urgent",
            "date_from": "2026-08-01",
            "date_to": "2026-08-31",
        },
    )

    assert response.status_code == 200

    service.get_summary.assert_called_once_with(
        supplier_id=5,
        part_id=10,
        origin_type="purchase",
        deadline_status="urgent",
        date_from="2026-08-01",
        date_to="2026-08-31",
    )


@pytest.mark.parametrize(
    (
        "parameter",
        "value",
    ),
    [
        (
            "supplier_id",
            0,
        ),
        (
            "part_id",
            0,
        ),
    ],
)
def test_should_return_422_for_invalid_identifier(
    client: TestClient,
    service: Mock,
    parameter: str,
    value: int,
) -> None:
    response = client.get(
        "/dashboard",
        params={
            parameter: value,
        },
    )

    assert response.status_code == 422

    service.get_summary.assert_not_called()


def test_should_return_400_for_business_validation_error(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_summary.side_effect = (
        ValueError(
            "A origem deve ser "
            "PURCHASE ou TRANSFER."
        )
    )

    response = client.get(
        "/dashboard",
        params={
            "origin_type": "INVALID",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "A origem deve ser "
            "PURCHASE ou TRANSFER."
        ),
    }


def test_should_return_401_without_authentication(
    session: Mock,
    service: Mock,
) -> None:
    test_app = FastAPI()

    def override_get_session():
        yield session

    def override_dashboard_service():
        return service

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_dashboard_service
    ] = override_dashboard_service

    test_app.include_router(
        router
    )

    with TestClient(
        test_app,
        raise_server_exceptions=False,
    ) as test_client:
        response = test_client.get(
            "/dashboard"
        )

    assert response.status_code == 401

    service.get_summary.assert_not_called()


def test_should_return_403_for_unauthorized_role(
    session: Mock,
    service: Mock,
) -> None:
    test_app = FastAPI()

    unauthorized_user = SimpleNamespace(
        id=99,
        username="sem-permissao",
        role_id=99,
        is_active=1,
    )

    unauthorized_role = SimpleNamespace(
        id=99,
        name="Perfil sem acesso",
    )

    def override_get_session():
        yield session

    def override_dashboard_service():
        return service

    def override_get_current_user():
        return unauthorized_user

    session.scalar.return_value = (
        unauthorized_role
    )

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_dashboard_service
    ] = override_dashboard_service

    test_app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    test_app.include_router(
        router
    )

    with TestClient(
        test_app,
        raise_server_exceptions=False,
    ) as test_client:
        response = test_client.get(
            "/dashboard"
        )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O usuário autenticado não possui "
            "permissão para realizar esta "
            "operação."
        ),
    }

    service.get_summary.assert_not_called()


def test_should_return_dashboard_stock_position(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_stock_position.return_value = (
        create_stock_position_dto()
    )

    response = client.get(
        "/dashboard/stock-position"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "part_id": 10,
            "part_code": "ABC123",
            "part_name": "Compressor de ar",
            "stock_quantity": 8,
            "workshop_pending_quantity": 3,
            "customer_pending_quantity": 2,
            "workshop_returned_quantity": 1,
            "customer_returned_quantity": 2,
            "available_core_quantity": 3,
        }
    ]

    service.get_stock_position.assert_called_once_with(
        supplier_id=None,
        part_id=None,
    )


def test_should_send_stock_position_filters_to_service(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_stock_position.return_value = (
        ()
    )

    response = client.get(
        "/dashboard/stock-position",
        params={
            "supplier_id": 5,
            "part_id": 10,
        },
    )

    assert response.status_code == 200

    service.get_stock_position.assert_called_once_with(
        supplier_id=5,
        part_id=10,
    )