from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.purchase_route import (
    get_purchase_service,
    router,
)
from src.database.connection import get_session
from src.services.purchase_service import (
    PurchaseService,
)


@pytest.fixture
def session() -> Mock:
    """
    Cria uma sessão de banco simulada.
    """

    return Mock(spec=Session)


@pytest.fixture
def service() -> Mock:
    """
    Cria um PurchaseService simulado.
    """

    return Mock(spec=PurchaseService)


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    """
    Cria uma aplicação isolada para os testes.
    """

    test_app = FastAPI()

    test_app.include_router(router)

    def override_get_session():
        yield session

    def override_get_purchase_service():
        return service

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_purchase_service
    ] = override_get_purchase_service

    return test_app


@pytest.fixture
def client(
    app: FastAPI,
) -> TestClient:
    """
    Cria o cliente HTTP para a aplicação de teste.
    """

    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_purchase(
    purchase_id: int = 10,
    supplier_id: int = 20,
    invoice_number: str = "NF-12345",
    invoice_series: str | None = "1",
    issue_date: str = "2026-07-29",
    received_at: str | None = None,
    notes: str | None = "Compra de teste.",
    created_by: int = 30,
    created_at: str = "2026-07-29T08:00:00",
    updated_at: str = "2026-07-29T08:00:00",
    status: str = "PENDING",
) -> SimpleNamespace:
    """
    Cria uma compra simulada para os testes.
    """

    return SimpleNamespace(
        id=purchase_id,
        supplier_id=supplier_id,
        invoice_number=invoice_number,
        invoice_series=invoice_series,
        issue_date=issue_date,
        received_at=received_at,
        notes=notes,
        created_by=created_by,
        created_at=created_at,
        updated_at=updated_at,
        status=status,
    )

def test_should_create_purchase(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase()

    service.create_purchase.return_value = purchase

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "status": "PENDING",
            "notes": "Compra de teste.",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "invoice_number": "NF-12345",
        "invoice_series": "1",
        "issue_date": "2026-07-29",
        "received_at": None,
        "notes": "Compra de teste.",
        "created_by": 30,
        "created_at": "2026-07-29T08:00:00",
        "updated_at": "2026-07-29T08:00:00",
        "status": "PENDING",
    }

    service.create_purchase.assert_called_once_with(
        supplier_id=20,
        invoice_number="NF-12345",
        invoice_series="1",
        issue_date="2026-07-29",
        created_by=30,
        status="PENDING",
        notes="Compra de teste.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()

def test_should_create_purchase_with_optional_fields_omitted(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series=None,
        notes=None,
    )

    service.create_purchase.return_value = purchase

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["invoice_series"] is None
    assert response_data["notes"] is None
    assert response_data["status"] == "PENDING"

    service.create_purchase.assert_called_once_with(
        supplier_id=20,
        invoice_number="NF-12345",
        invoice_series=None,
        issue_date="2026-07-29",
        created_by=30,
        status="PENDING",
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()

def test_should_return_404_when_supplier_is_not_found_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 999,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "status": "PENDING",
            "notes": "Compra de teste.",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_return_400_when_supplier_is_inactive_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = ValueError(
        "Não é possível cadastrar uma compra "
        "para um fornecedor inativo."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível cadastrar uma compra "
            "para um fornecedor inativo."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_return_409_when_invoice_is_duplicated_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = ValueError(
        "Já existe uma compra com esta nota fiscal, "
        "série e fornecedor."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

@pytest.mark.parametrize(
    (
        "payload",
        "missing_field",
    ),
    [
        (
            {
                "invoice_number": "NF-12345",
                "issue_date": "2026-07-29",
                "created_by": 30,
            },
            "supplier_id",
        ),
        (
            {
                "supplier_id": 20,
                "issue_date": "2026-07-29",
                "created_by": 30,
            },
            "invoice_number",
        ),
        (
            {
                "supplier_id": 20,
                "invoice_number": "NF-12345",
                "created_by": 30,
            },
            "issue_date",
        ),
        (
            {
                "supplier_id": 20,
                "invoice_number": "NF-12345",
                "issue_date": "2026-07-29",
            },
            "created_by",
        ),
    ],
)
def test_should_return_422_when_required_field_is_missing(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict[str, object],
    missing_field: str,
) -> None:
    response = client.post(
        "/purchases",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == missing_field
        for error in errors
    )

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

@pytest.mark.parametrize(
    (
        "field",
        "invalid_value",
    ),
    [
        ("supplier_id", 0),
        ("supplier_id", -1),
        ("created_by", 0),
        ("created_by", -1),
    ],
)
def test_should_return_422_when_create_id_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    invalid_value: int,
) -> None:
    payload = {
        "supplier_id": 20,
        "invoice_number": "NF-12345",
        "issue_date": "2026-07-29",
        "created_by": 30,
    }

    payload[field] = invalid_value

    response = client.post(
        "/purchases",
        json=payload,
    )

    assert response.status_code == 422

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

def test_should_return_422_when_create_status_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "status": "INVALID",
        },
    )

    assert response.status_code == 422

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "unexpected_field": "valor inválido",
        },
    )

    assert response.status_code == 422

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

def test_should_rollback_when_unexpected_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_list_purchases(
    client: TestClient,
    service: Mock,
) -> None:
    first_purchase = create_purchase(
        purchase_id=10,
        invoice_number="NF-12345",
    )

    second_purchase = create_purchase(
        purchase_id=11,
        invoice_number="NF-67890",
        invoice_series="2",
        notes=None,
        status="RECEIVED",
    )

    service.list_purchases.return_value = [
        first_purchase,
        second_purchase,
    ]

    response = client.get(
        "/purchases"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 10,
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "received_at": None,
            "notes": "Compra de teste.",
            "created_by": 30,
            "created_at": "2026-07-29T08:00:00",
            "updated_at": "2026-07-29T08:00:00",
            "status": "PENDING",
        },
        {
            "id": 11,
            "supplier_id": 20,
            "invoice_number": "NF-67890",
            "invoice_series": "2",
            "issue_date": "2026-07-29",
            "received_at": None,
            "notes": None,
            "created_by": 30,
            "created_at": "2026-07-29T08:00:00",
            "updated_at": "2026-07-29T08:00:00",
            "status": "RECEIVED",
        },
    ]

    service.list_purchases.assert_called_once_with()

def test_should_return_empty_purchase_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchases.return_value = []

    response = client.get(
        "/purchases"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_purchases.assert_called_once_with()

def test_should_list_purchases_by_supplier(
    client: TestClient,
    service: Mock,
) -> None:
    purchases = [
        create_purchase(
            purchase_id=10,
            supplier_id=20,
        ),
        create_purchase(
            purchase_id=11,
            supplier_id=20,
            invoice_number="NF-67890",
        ),
    ]

    service.list_purchases_by_supplier.return_value = (
        purchases
    )

    response = client.get(
        "/purchases",
        params={
            "supplier_id": 20,
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 2

    assert all(
        purchase["supplier_id"] == 20
        for purchase in response.json()
    )

    service.list_purchases_by_supplier.assert_called_once_with(
        20
    )

    service.list_purchases.assert_not_called()

def test_should_return_empty_list_when_supplier_has_no_purchases(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchases_by_supplier.return_value = []

    response = client.get(
        "/purchases",
        params={
            "supplier_id": 20,
        },
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_purchases_by_supplier.assert_called_once_with(
        20
    )

    service.list_purchases.assert_not_called()

def test_should_return_404_when_supplier_is_not_found_on_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchases_by_supplier.side_effect = (
        ValueError(
            "Fornecedor não encontrado."
        )
    )

    response = client.get(
        "/purchases",
        params={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado."
    }

    service.list_purchases_by_supplier.assert_called_once_with(
        999
    )

    service.list_purchases.assert_not_called()

@pytest.mark.parametrize(
    "supplier_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_supplier_filter_is_invalid(
    client: TestClient,
    service: Mock,
    supplier_id: int,
) -> None:
    response = client.get(
        "/purchases",
        params={
            "supplier_id": supplier_id,
        },
    )

    assert response.status_code == 422

    service.list_purchases.assert_not_called()

    service.list_purchases_by_supplier.assert_not_called()

def test_should_get_purchase(
    client: TestClient,
    service: Mock,
) -> None:
    purchase = create_purchase()

    service.get_purchase.return_value = purchase

    response = client.get(
        "/purchases/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "invoice_number": "NF-12345",
        "invoice_series": "1",
        "issue_date": "2026-07-29",
        "received_at": None,
        "notes": "Compra de teste.",
        "created_by": 30,
        "created_at": "2026-07-29T08:00:00",
        "updated_at": "2026-07-29T08:00:00",
        "status": "PENDING",
    }

    service.get_purchase.assert_called_once_with(
        10
    )

def test_should_return_404_when_purchase_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_purchase.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.get(
        "/purchases/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    service.get_purchase.assert_called_once_with(
        999
    )

@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.get(
        f"/purchases/{purchase_id}"
    )

    assert response.status_code == 422

    service.get_purchase.assert_not_called()

def test_should_update_purchase(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        invoice_number="NF-99999",
        invoice_series="2",
        issue_date="2026-07-30",
        notes="Compra atualizada.",
        status="RECEIVED",
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "invoice_number": "NF-99999",
            "invoice_series": "2",
            "issue_date": "2026-07-30",
            "notes": "Compra atualizada.",
            "status": "RECEIVED",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "invoice_number": "NF-99999",
        "invoice_series": "2",
        "issue_date": "2026-07-30",
        "received_at": None,
        "notes": "Compra atualizada.",
        "created_by": 30,
        "created_at": "2026-07-29T08:00:00",
        "updated_at": "2026-07-29T08:00:00",
        "status": "RECEIVED",
    }

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        invoice_number="NF-99999",
        invoice_series="2",
        issue_date="2026-07-30",
        notes="Compra atualizada.",
        status="RECEIVED",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_update_only_sent_purchase_fields(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        notes="Nova observação.",
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 200
    assert response.json()["notes"] == "Nova observação."

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        notes="Nova observação.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_update_purchase_supplier(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        supplier_id=21,
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 21,
        },
    )

    assert response.status_code == 200
    assert response.json()["supplier_id"] == 21

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        supplier_id=21,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_clear_purchase_notes(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        notes=None,
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "notes": None,
        },
    )

    assert response.status_code == 200
    assert response.json()["notes"] is None

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_clear_purchase_invoice_series(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series=None,
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "invoice_series": None,
        },
    )

    assert response.status_code == 200
    assert response.json()["invoice_series"] is None

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        invoice_series=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_allow_empty_update_payload(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase()

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={},
    )

    assert response.status_code == 200

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_purchase_is_not_found_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.patch(
        "/purchases/999",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    service.update_purchase.assert_called_once_with(
        purchase_id=999,
        notes="Nova observação.",
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado."
    }

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        supplier_id=999,
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_supplier_is_inactive_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Não é possível vincular a compra "
        "a um fornecedor inativo."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 21,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível vincular a compra "
            "a um fornecedor inativo."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_invoice_is_duplicated_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Já existe uma compra com esta nota fiscal, "
        "série e fornecedor."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "invoice_number": "NF-99999",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_purchase_is_cancelled_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Não é possível alterar uma compra cancelada."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível alterar uma compra cancelada."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_supplier_is_incompatible_with_items(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Não é possível alterar o fornecedor, "
        "pois existem peças incompatíveis na compra."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 21,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível alterar o fornecedor, "
            "pois existem peças incompatíveis na compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_cancelled_status_is_sent_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Utilize a operação específica para cancelar a compra."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "status": "CANCELLED",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Utilize a operação específica "
            "para cancelar a compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.patch(
        f"/purchases/{purchase_id}",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 422

    service.update_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "invalid_field",
    ),
    [
        (
            {
                "supplier_id": 0,
            },
            "supplier_id",
        ),
        (
            {
                "supplier_id": -1,
            },
            "supplier_id",
        ),
        (
            {
                "invoice_number": "",
            },
            "invoice_number",
        ),
        (
            {
                "issue_date": "",
            },
            "issue_date",
        ),
        (
            {
                "status": "INVALID",
            },
            "status",
        ),
    ],
)
def test_should_return_422_when_update_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict[str, object],
    invalid_field: str,
) -> None:
    response = client.patch(
        "/purchases/10",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == invalid_field
        for error in errors
    )

    service.update_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_update_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.patch(
        "/purchases/10",
        json={
            "unexpected_field": "valor inválido",
        },
    )

    assert response.status_code == 422

    service.update_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def create_purchase_item(
    purchase_item_id: int = 30,
    purchase_id: int = 10,
    part_id: int = 40,
    quantity_purchased: int = 10,
    quantity_available: int = 10,
    created_at: str = "2026-07-29T08:00:00",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=purchase_item_id,
        purchase_id=purchase_id,
        part_id=part_id,
        quantity_purchased=quantity_purchased,
        quantity_available=quantity_available,
        created_at=created_at,
    )


def test_should_add_purchase_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase_item = create_purchase_item()

    service.add_item.return_value = purchase_item

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 30,
        "purchase_id": 10,
        "part_id": 40,
        "quantity_purchased": 10,
        "quantity_available": 10,
        "created_at": "2026-07-29T08:00:00",
    }

    service.add_item.assert_called_once_with(
        purchase_id=10,
        part_id=40,
        quantity_purchased=10,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase_item
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_purchase_is_not_found_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.post(
        "/purchases/999/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_404_when_part_is_not_found_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 999,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_purchase_is_cancelled_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Não é possível adicionar itens "
        "a uma compra cancelada."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível adicionar itens "
            "a uma compra cancelada."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_part_is_inactive_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Não é possível adicionar uma peça inativa."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível adicionar uma peça inativa."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_part_supplier_is_incompatible(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "A peça não pertence ao fornecedor da compra."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "A peça não pertence ao fornecedor da compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_purchase_item_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Esta peça já foi adicionada à compra."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Esta peça já foi adicionada à compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.post(
        f"/purchases/{purchase_id}/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "invalid_field",
    ),
    [
        (
            {
                "part_id": 0,
                "quantity_purchased": 10,
            },
            "part_id",
        ),
        (
            {
                "part_id": -1,
                "quantity_purchased": 10,
            },
            "part_id",
        ),
        (
            {
                "part_id": 40,
                "quantity_purchased": 0,
            },
            "quantity_purchased",
        ),
        (
            {
                "part_id": 40,
                "quantity_purchased": -1,
            },
            "quantity_purchased",
        ),
    ],
)
def test_should_return_422_when_add_item_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict[str, int],
    invalid_field: str,
) -> None:
    response = client.post(
        "/purchases/10/items",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == invalid_field
        for error in errors
    )

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_add_item_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
            "unexpected_field": "valor inválido",
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_purchase_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchase_items.return_value = [
        create_purchase_item(),
        create_purchase_item(
            purchase_item_id=31,
            part_id=41,
            quantity_purchased=5,
            quantity_available=3,
        ),
    ]

    response = client.get(
        "/purchases/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 30,
            "purchase_id": 10,
            "part_id": 40,
            "quantity_purchased": 10,
            "quantity_available": 10,
            "created_at": "2026-07-29T08:00:00",
        },
        {
            "id": 31,
            "purchase_id": 10,
            "part_id": 41,
            "quantity_purchased": 5,
            "quantity_available": 3,
            "created_at": "2026-07-29T08:00:00",
        },
    ]

    service.list_purchase_items.assert_called_once_with(
        10
    )


def test_should_return_empty_purchase_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchase_items.return_value = []

    response = client.get(
        "/purchases/10/items"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_purchase_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_purchase_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchase_items.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.get(
        "/purchases/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    service.list_purchase_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.get(
        f"/purchases/{purchase_id}/items"
    )

    assert response.status_code == 422

    service.list_purchase_items.assert_not_called()


def test_should_cancel_purchase(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        status="CANCELLED",
    )

    service.cancel_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 200

    assert response.json()["status"] == "CANCELLED"

    service.cancel_purchase.assert_called_once_with(
        10
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_purchase_is_not_found_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.patch(
        "/purchases/999/cancel"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_purchase_is_already_cancelled(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = ValueError(
        "A compra já está cancelada."
    )

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": "A compra já está cancelada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_purchase_has_movements_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = ValueError(
        "Não é possível cancelar uma compra "
        "que já possui movimentações."
    )

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível cancelar uma compra "
            "que já possui movimentações."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.patch(
        f"/purchases/{purchase_id}/cancel"
    )

    assert response.status_code == 422

    service.cancel_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()