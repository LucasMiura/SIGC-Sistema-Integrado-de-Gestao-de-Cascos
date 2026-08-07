from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.supplier_return_route import (
    get_supplier_return_service,
    router,
)
from src.database.connection import get_session
from src.services.supplier_return_service import (
    SupplierReturnService,
)
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_BUYER,
)


@pytest.fixture
def session() -> Mock:
    """Cria uma sessão de banco simulada."""

    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    """Cria um SupplierReturnService simulado."""

    return Mock(
        spec=SupplierReturnService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    """
    Cria uma aplicação isolada simulando
    um Comprador autenticado.
    """

    test_app = FastAPI()

    buyer_user = SimpleNamespace(
        id=30,
        username="comprador",
        role_id=2,
        is_active=1,
    )

    buyer_role = SimpleNamespace(
        id=2,
        name=ROLE_BUYER,
    )

    def override_get_session():
        yield session

    def override_get_supplier_return_service():
        return service

    def override_get_current_user():
        return buyer_user

    session.scalar.return_value = (
        buyer_role
    )

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_supplier_return_service
    ] = override_get_supplier_return_service

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
    """Cria o cliente HTTP da aplicação de teste."""

    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_supplier_return(
    supplier_return_id: int = 10,
    supplier_id: int = 20,
    dispatch_invoice_number: str = "NF-REMESSA-12345",
    dispatch_invoice_series: str | None = "1",
    issue_date: str = "2026-08-05",
    created_by: int = 30,
    created_at: str = "2026-08-05T09:00:00",
    updated_at: str = "2026-08-05T09:00:00",
    status: str = "ACTIVE",
    notes: str | None = "Remessa de teste.",
) -> SimpleNamespace:
    """Cria uma remessa simulada."""

    return SimpleNamespace(
        id=supplier_return_id,
        supplier_id=supplier_id,
        dispatch_invoice_number=(
            dispatch_invoice_number
        ),
        dispatch_invoice_series=(
            dispatch_invoice_series
        ),
        issue_date=issue_date,
        created_by=created_by,
        created_at=created_at,
        updated_at=updated_at,
        status=status,
        notes=notes,
    )


def create_supplier_return_item(
    supplier_return_item_id: int = 40,
    supplier_return_id: int = 10,
    purchase_item_id: int = 50,
    quantity: int = 4,
    created_at: str = "2026-08-05T09:05:00",
) -> SimpleNamespace:
    """Cria um item de remessa simulado."""

    return SimpleNamespace(
        id=supplier_return_item_id,
        supplier_return_id=supplier_return_id,
        purchase_item_id=purchase_item_id,
        quantity=quantity,
        created_at=created_at,
    )


def test_should_create_supplier_return(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    supplier_return = create_supplier_return()

    service.create_supplier_return.return_value = (
        supplier_return
    )

    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "dispatch_invoice_series": "1",
            "issue_date": "2026-08-05",
            "status": "ACTIVE",
            "notes": "Remessa de teste.",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "dispatch_invoice_number": (
            "NF-REMESSA-12345"
        ),
        "dispatch_invoice_series": "1",
        "issue_date": "2026-08-05",
        "created_by": 30,
        "created_at": "2026-08-05T09:00:00",
        "updated_at": "2026-08-05T09:00:00",
        "status": "ACTIVE",
        "notes": "Remessa de teste.",
    }

    service.create_supplier_return.assert_called_once_with(
        supplier_id=20,
        dispatch_invoice_number=(
            "NF-REMESSA-12345"
        ),
        dispatch_invoice_series="1",
        issue_date="2026-08-05",
        created_by=30,
        status="ACTIVE",
        notes="Remessa de teste.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        supplier_return
    )

    session.rollback.assert_not_called()


def test_should_create_supplier_return_without_optional_fields(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    supplier_return = create_supplier_return(
        dispatch_invoice_series=None,
        notes=None,
    )

    service.create_supplier_return.return_value = (
        supplier_return
    )

    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 201

    assert response.json()[
        "dispatch_invoice_series"
    ] is None

    assert response.json()["notes"] is None

    service.create_supplier_return.assert_called_once_with(
        supplier_id=20,
        dispatch_invoice_number=(
            "NF-REMESSA-12345"
        ),
        dispatch_invoice_series=None,
        issue_date="2026-08-05",
        created_by=30,
        status="ACTIVE",
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        supplier_return
    )


@pytest.mark.parametrize(
    (
        "payload",
        "missing_field",
    ),
    [
        (
            {
                "dispatch_invoice_number": (
                    "NF-REMESSA-12345"
                ),
                "issue_date": "2026-08-05",
            },
            "supplier_id",
        ),
        (
            {
                "supplier_id": 20,
                "issue_date": "2026-08-05",
            },
            "dispatch_invoice_number",
        ),
        (
            {
                "supplier_id": 20,
                "dispatch_invoice_number": (
                    "NF-REMESSA-12345"
                ),
            },
            "issue_date",
        ),
    ],
)
def test_should_return_422_when_required_create_field_is_missing(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
    missing_field: str,
) -> None:
    response = client.post(
        "/supplier-returns",
        json=payload,
    )

    assert response.status_code == 422
    assert missing_field in response.text

    service.create_supplier_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    (
        "field",
        "value",
    ),
    [
        (
            "supplier_id",
            0,
        ),
        (
            "supplier_id",
            -1,
        ),
    ],
)
def test_should_return_422_when_create_id_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    value: int,
) -> None:
    payload = {
        "supplier_id": 20,
        "dispatch_invoice_number": (
            "NF-REMESSA-12345"
        ),
        "issue_date": "2026-08-05",
    }

    payload[field] = value

    response = client.post(
        "/supplier-returns",
        json=payload,
    )

    assert response.status_code == 422

    service.create_supplier_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    (
        "field",
        "value",
    ),
    [
        (
            "dispatch_invoice_number",
            "",
        ),
        (
            "dispatch_invoice_number",
            "   ",
        ),
        (
            "issue_date",
            "",
        ),
        (
            "issue_date",
            "   ",
        ),
    ],
)
def test_should_return_422_when_required_create_text_is_empty(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    value: str,
) -> None:
    payload = {
        "supplier_id": 20,
        "dispatch_invoice_number": (
            "NF-REMESSA-12345"
        ),
        "issue_date": "2026-08-05",
        "created_by": 30,
    }

    payload[field] = value

    response = client.post(
        "/supplier-returns",
        json=payload,
    )

    assert response.status_code == 422

    service.create_supplier_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_422_when_create_status_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
            "status": "FINISHED",
        },
    )

    assert response.status_code == 422

    service.create_supplier_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service.create_supplier_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        "Fornecedor não encontrado.",
        "Compra de origem não encontrada.",
        "Item de compra não encontrado.",
    ],
)
def test_should_return_404_when_related_resource_is_not_found_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create_supplier_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_dispatch_invoice_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "Já existe uma remessa cadastrada com esse "
        "número de Nota Fiscal de Simples Remessa."
    )

    service.create_supplier_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        "O fornecedor informado está inativo.",
        (
            "Uma remessa ao fornecedor não pode ser "
            "criada já cancelada."
        ),
        (
            "O status da remessa deve ser "
            "ACTIVE ou CANCELLED."
        ),
    ],
)
def test_should_return_400_when_business_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create_supplier_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_supplier_return.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/supplier-returns",
        json={
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_supplier_returns(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_supplier_returns.return_value = [
        create_supplier_return(),
        create_supplier_return(
            supplier_return_id=11,
            dispatch_invoice_number=(
                "NF-REMESSA-67890"
            ),
            dispatch_invoice_series=None,
            notes=None,
        ),
    ]

    response = client.get(
        "/supplier-returns"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 10,
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-12345"
            ),
            "dispatch_invoice_series": "1",
            "issue_date": "2026-08-05",
            "created_by": 30,
            "created_at": "2026-08-05T09:00:00",
            "updated_at": "2026-08-05T09:00:00",
            "status": "ACTIVE",
            "notes": "Remessa de teste.",
        },
        {
            "id": 11,
            "supplier_id": 20,
            "dispatch_invoice_number": (
                "NF-REMESSA-67890"
            ),
            "dispatch_invoice_series": None,
            "issue_date": "2026-08-05",
            "created_by": 30,
            "created_at": "2026-08-05T09:00:00",
            "updated_at": "2026-08-05T09:00:00",
            "status": "ACTIVE",
            "notes": None,
        },
    ]

    service.list_supplier_returns.assert_called_once_with()


def test_should_return_empty_supplier_return_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_supplier_returns.return_value = []

    response = client.get(
        "/supplier-returns"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_supplier_returns.assert_called_once_with()


def test_should_get_supplier_return(
    client: TestClient,
    service: Mock,
) -> None:
    supplier_return = create_supplier_return()

    service.get_supplier_return.return_value = (
        supplier_return
    )

    response = client.get(
        "/supplier-returns/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "dispatch_invoice_number": (
            "NF-REMESSA-12345"
        ),
        "dispatch_invoice_series": "1",
        "issue_date": "2026-08-05",
        "created_by": 30,
        "created_at": "2026-08-05T09:00:00",
        "updated_at": "2026-08-05T09:00:00",
        "status": "ACTIVE",
        "notes": "Remessa de teste.",
    }

    service.get_supplier_return.assert_called_once_with(
        10
    )


def test_should_return_404_when_supplier_return_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Remessa ao fornecedor não encontrada."

    service.get_supplier_return.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/supplier-returns/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.get_supplier_return.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "supplier_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_supplier_return_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    supplier_return_id: int,
) -> None:
    response = client.get(
        (
            "/supplier-returns/"
            f"{supplier_return_id}"
        )
    )

    assert response.status_code == 422

    service.get_supplier_return.assert_not_called()


def test_should_add_supplier_return_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    supplier_return_item = (
        create_supplier_return_item()
    )

    service.add_item.return_value = (
        supplier_return_item
    )

    response = client.post(
        "/supplier-returns/10/items",
        json={
            "purchase_item_id": 50,
            "quantity": 4,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 40,
        "supplier_return_id": 10,
        "purchase_item_id": 50,
        "quantity": 4,
        "created_at": "2026-08-05T09:05:00",
    }

    service.add_item.assert_called_once_with(
        supplier_return_id=10,
        purchase_item_id=50,
        quantity=4,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        supplier_return_item
    )

    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Remessa ao fornecedor não encontrada.",
            404,
        ),
        (
            "Item de compra não encontrado.",
            404,
        ),
        (
            "Compra de origem não encontrada.",
            404,
        ),
        (
            (
                "Este item de compra já foi adicionado "
                "à remessa."
            ),
            409,
        ),
        (
            (
                "Não é possível adicionar itens a uma "
                "remessa que não está ativa."
            ),
            400,
        ),
        (
            (
                "O item de compra não pertence ao "
                "fornecedor da remessa."
            ),
            400,
        ),
        (
            (
                "Todos os itens da remessa devem "
                "pertencer à mesma Nota Fiscal de compra."
            ),
            400,
        ),
        (
            (
                "Não existe quantidade disponível para "
                "remessa neste item de compra."
            ),
            400,
        ),
        (
            (
                "A quantidade remetida é maior que a "
                "quantidade disponível para remessa. "
                "Quantidade máxima permitida: 2."
            ),
            400,
        ),
    ],
)
def test_should_convert_business_error_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
    expected_status: int,
) -> None:
    service.add_item.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/supplier-returns/10/items",
        json={
            "purchase_item_id": 50,
            "quantity": 4,
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    service.add_item.assert_called_once_with(
        supplier_return_id=10,
        purchase_item_id=50,
        quantity=4,
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "supplier_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_supplier_return_id_is_invalid_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    supplier_return_id: int,
) -> None:
    response = client.post(
        (
            "/supplier-returns/"
            f"{supplier_return_id}/items"
        ),
        json={
            "purchase_item_id": 50,
            "quantity": 4,
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "payload",
    [
        {
            "quantity": 4,
        },
        {
            "purchase_item_id": 50,
        },
        {
            "purchase_item_id": 0,
            "quantity": 4,
        },
        {
            "purchase_item_id": -1,
            "quantity": 4,
        },
        {
            "purchase_item_id": 50,
            "quantity": 0,
        },
        {
            "purchase_item_id": 50,
            "quantity": -1,
        },
    ],
)
def test_should_return_422_when_add_item_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
) -> None:
    response = client.post(
        "/supplier-returns/10/items",
        json=payload,
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_422_when_add_item_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/supplier-returns/10/items",
        json={
            "purchase_item_id": 50,
            "quantity": 4,
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/supplier-returns/10/items",
        json={
            "purchase_item_id": 50,
            "quantity": 4,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_supplier_return_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_items.return_value = [
        create_supplier_return_item(),
        create_supplier_return_item(
            supplier_return_item_id=41,
            purchase_item_id=51,
            quantity=2,
        ),
    ]

    response = client.get(
        "/supplier-returns/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 40,
            "supplier_return_id": 10,
            "purchase_item_id": 50,
            "quantity": 4,
            "created_at": "2026-08-05T09:05:00",
        },
        {
            "id": 41,
            "supplier_return_id": 10,
            "purchase_item_id": 51,
            "quantity": 2,
            "created_at": "2026-08-05T09:05:00",
        },
    ]

    service.list_items.assert_called_once_with(
        10
    )


def test_should_return_empty_supplier_return_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_items.return_value = []

    response = client.get(
        "/supplier-returns/10/items"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_supplier_return_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Remessa ao fornecedor não encontrada."

    service.list_items.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/supplier-returns/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.list_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "supplier_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_supplier_return_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    supplier_return_id: int,
) -> None:
    response = client.get(
        (
            "/supplier-returns/"
            f"{supplier_return_id}/items"
        )
    )

    assert response.status_code == 422

    service.list_items.assert_not_called()


def test_should_get_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_available_quantity.return_value = 6

    response = client.get(
        (
            "/supplier-returns/purchase-items/"
            "50/available-quantity"
        )
    )

    assert response.status_code == 200

    assert response.json() == {
        "purchase_item_id": 50,
        "available_quantity": 6,
    }

    service.get_available_quantity.assert_called_once_with(
        50
    )


def test_should_return_zero_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_available_quantity.return_value = 0

    response = client.get(
        (
            "/supplier-returns/purchase-items/"
            "50/available-quantity"
        )
    )

    assert response.status_code == 200

    assert response.json() == {
        "purchase_item_id": 50,
        "available_quantity": 0,
    }


def test_should_return_404_when_purchase_item_is_not_found_on_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Item de compra não encontrado."

    service.get_available_quantity.side_effect = (
        ValueError(message)
    )

    response = client.get(
        (
            "/supplier-returns/purchase-items/"
            "999/available-quantity"
        )
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.get_available_quantity.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "purchase_item_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_item_id_is_invalid_on_available_quantity(
    client: TestClient,
    service: Mock,
    purchase_item_id: int,
) -> None:
    response = client.get(
        (
            "/supplier-returns/purchase-items/"
            f"{purchase_item_id}/available-quantity"
        )
    )

    assert response.status_code == 422

    service.get_available_quantity.assert_not_called()