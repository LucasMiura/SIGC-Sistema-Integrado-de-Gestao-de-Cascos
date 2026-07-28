from collections.abc import Generator
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.purchase_tracking_route import (
    get_purchase_tracking_service,
)
from src.dtos.purchase_tracking import (
    PurchaseItemTrackingDTO,
    PurchaseTrackingDTO,
)
from src.main import app
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock compatível com PurchaseTrackingService.
    """

    return Mock(spec=PurchaseTrackingService)


@pytest.fixture
def client(
    service_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo a dependência real do serviço.

    Dessa forma, os testes da rota não acessam o banco SQLite.
    """

    def override_purchase_tracking_service() -> Mock:
        return service_mock

    app.dependency_overrides[
        get_purchase_tracking_service
    ] = override_purchase_tracking_service

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_tracking_dto() -> PurchaseTrackingDTO:
    """
    Cria um acompanhamento completo para o teste HTTP.
    """

    item = PurchaseItemTrackingDTO(
        purchase_item_id=10,
        part_id=20,
        part_code="PCA-001",
        part_name="Peça com casco",
        quantity_purchased=10,
        quantity_available_for_outbound=2,
        quantity_outbound=8,
        quantity_returned_by_customer=5,
        quantity_pending_customer_return=3,
        quantity_available_for_supplier_return=3,
        quantity_returned_to_supplier=2,
        quantity_pending_supplier_return=8,
        lifecycle_status="PARTIALLY_RETURNED_TO_SUPPLIER",
    )

    return PurchaseTrackingDTO(
        purchase_id=1,
        supplier_id=5,
        supplier_name="Fornecedor Teste",
        invoice_number="NF-12345",
        invoice_series="1",
        issue_date="2026-07-28",
        purchase_status="ACTIVE",
        items=(item,),
    )


def test_should_return_purchase_tracking_with_status_200(
    client: TestClient,
    service_mock: Mock,
) -> None:
    expected_tracking = create_tracking_dto()

    service_mock.get_purchase_tracking.return_value = (
        expected_tracking
    )

    response = client.get(
        "/purchases/1/tracking",
    )

    assert response.status_code == 200

    assert response.json() == {
        "purchase_id": 1,
        "supplier_id": 5,
        "supplier_name": "Fornecedor Teste",
        "invoice_number": "NF-12345",
        "invoice_series": "1",
        "issue_date": "2026-07-28",
        "purchase_status": "ACTIVE",
        "items": [
            {
                "purchase_item_id": 10,
                "part_id": 20,
                "part_code": "PCA-001",
                "part_name": "Peça com casco",
                "quantity_purchased": 10,
                "quantity_available_for_outbound": 2,
                "quantity_outbound": 8,
                "quantity_returned_by_customer": 5,
                "quantity_pending_customer_return": 3,
                "quantity_available_for_supplier_return": 3,
                "quantity_returned_to_supplier": 2,
                "quantity_pending_supplier_return": 8,
                "lifecycle_status": (
                    "PARTIALLY_RETURNED_TO_SUPPLIER"
                ),
            }
        ],
    }

    service_mock.get_purchase_tracking.assert_called_once_with(1)


def test_should_return_404_when_purchase_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_purchase_tracking.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.get(
        "/purchases/999/tracking",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada.",
    }

    service_mock.get_purchase_tracking.assert_called_once_with(999)


def test_should_return_400_for_business_validation_error(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_purchase_tracking.side_effect = ValueError(
        "Erro de validação da compra."
    )

    response = client.get(
        "/purchases/1/tracking",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Erro de validação da compra.",
    }

    service_mock.get_purchase_tracking.assert_called_once_with(1)


def test_should_return_422_for_non_positive_purchase_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/purchases/0/tracking",
    )

    assert response.status_code == 422

    service_mock.get_purchase_tracking.assert_not_called()