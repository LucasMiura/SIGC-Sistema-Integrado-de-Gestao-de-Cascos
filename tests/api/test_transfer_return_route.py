from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.transfer_return_route import (
    get_transfer_return_service,
    router,
)
from src.database.connection import get_session
from src.services.transfer_return_service import (
    TransferReturnService,
)


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=TransferReturnService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    test_app = FastAPI()

    test_app.include_router(
        router
    )

    def override_get_session():
        yield session

    def override_get_transfer_return_service():
        return service

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_transfer_return_service
    ] = override_get_transfer_return_service

    return test_app


@pytest.fixture
def client(
    app: FastAPI,
) -> TestClient:
    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_transfer_return(
    transfer_return_id: int = 30,
    transfer_id: int = 10,
    dispatch_invoice_number: str = "NF-RETURN-100",
    dispatch_invoice_series: str | None = "1",
    issue_date: str = "2026-08-05",
    created_by: int = 50,
    created_at: str = "2026-08-05T17:30:00",
    updated_at: str = "2026-08-05T17:30:00",
    status: str = "ACTIVE",
    notes: str | None = "Devolução parcial.",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_return_id,
        transfer_id=transfer_id,
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


def create_transfer_return_item(
    transfer_return_item_id: int = 60,
    transfer_return_id: int = 30,
    transfer_item_id: int = 20,
    quantity: int = 4,
    created_at: str = "2026-08-05T17:35:00",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_return_item_id,
        transfer_return_id=transfer_return_id,
        transfer_item_id=transfer_item_id,
        quantity=quantity,
        created_at=created_at,
    )


def expected_transfer_return_response(
    transfer_return_id: int = 30,
    transfer_id: int = 10,
    dispatch_invoice_number: str = "NF-RETURN-100",
    dispatch_invoice_series: str | None = "1",
    notes: str | None = "Devolução parcial.",
) -> dict:
    return {
        "id": transfer_return_id,
        "transfer_id": transfer_id,
        "dispatch_invoice_number": (
            dispatch_invoice_number
        ),
        "dispatch_invoice_series": (
            dispatch_invoice_series
        ),
        "issue_date": "2026-08-05",
        "created_by": 50,
        "created_at": "2026-08-05T17:30:00",
        "updated_at": "2026-08-05T17:30:00",
        "status": "ACTIVE",
        "notes": notes,
    }


def test_should_create_transfer_return(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    transfer_return = create_transfer_return()

    service.create_transfer_return.return_value = (
        transfer_return
    )

    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "dispatch_invoice_series": "1",
            "issue_date": "2026-08-05",
            "created_by": 50,
            "status": "ACTIVE",
            "notes": "Devolução parcial.",
        },
    )

    assert response.status_code == 201

    assert response.json() == (
        expected_transfer_return_response()
    )

    service.create_transfer_return.assert_called_once_with(
        transfer_id=10,
        dispatch_invoice_number="NF-RETURN-100",
        dispatch_invoice_series="1",
        issue_date="2026-08-05",
        created_by=50,
        status="ACTIVE",
        notes="Devolução parcial.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        transfer_return
    )

    session.rollback.assert_not_called()


def test_should_create_transfer_return_without_optional_fields(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    transfer_return = create_transfer_return(
        dispatch_invoice_series=None,
        notes=None,
    )

    service.create_transfer_return.return_value = (
        transfer_return
    )

    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
        },
    )

    assert response.status_code == 201

    assert response.json() == (
        expected_transfer_return_response(
            dispatch_invoice_series=None,
            notes=None,
        )
    )

    service.create_transfer_return.assert_called_once_with(
        transfer_id=10,
        dispatch_invoice_number="NF-RETURN-100",
        dispatch_invoice_series=None,
        issue_date="2026-08-05",
        created_by=50,
        status="ACTIVE",
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        transfer_return
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
                    "NF-RETURN-100"
                ),
                "issue_date": "2026-08-05",
                "created_by": 50,
            },
            "transfer_id",
        ),
        (
            {
                "transfer_id": 10,
                "issue_date": "2026-08-05",
                "created_by": 50,
            },
            "dispatch_invoice_number",
        ),
        (
            {
                "transfer_id": 10,
                "dispatch_invoice_number": (
                    "NF-RETURN-100"
                ),
                "created_by": 50,
            },
            "issue_date",
        ),
        (
            {
                "transfer_id": 10,
                "dispatch_invoice_number": (
                    "NF-RETURN-100"
                ),
                "issue_date": "2026-08-05",
            },
            "created_by",
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
        "/transfer-returns",
        json=payload,
    )

    assert response.status_code == 422
    assert missing_field in response.text

    service.create_transfer_return.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "field",
        "value",
    ),
    [
        (
            "transfer_id",
            0,
        ),
        (
            "transfer_id",
            -1,
        ),
        (
            "created_by",
            0,
        ),
        (
            "created_by",
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
        "transfer_id": 10,
        "dispatch_invoice_number": (
            "NF-RETURN-100"
        ),
        "issue_date": "2026-08-05",
        "created_by": 50,
    }

    payload[field] = value

    response = client.post(
        "/transfer-returns",
        json=payload,
    )

    assert response.status_code == 422

    service.create_transfer_return.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


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
        "transfer_id": 10,
        "dispatch_invoice_number": (
            "NF-RETURN-100"
        ),
        "issue_date": "2026-08-05",
        "created_by": 50,
    }

    payload[field] = value

    response = client.post(
        "/transfer-returns",
        json=payload,
    )

    assert response.status_code == 422

    service.create_transfer_return.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_create_status_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
            "status": "FINISHED",
        },
    )

    assert response.status_code == 422

    service.create_transfer_return.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service.create_transfer_return.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        "Transferência não encontrada.",
    ],
)
def test_should_return_404_when_related_resource_is_not_found_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create_transfer_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_invoice_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "Já existe uma devolução à filial "
        "cadastrada com esse número de Nota "
        "Fiscal de Simples Remessa."
    )

    service.create_transfer_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
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
        (
            "Não é possível registrar devolução "
            "para uma transferência que não está "
            "ativa."
        ),
        (
            "Uma devolução à filial não pode ser "
            "criada já cancelada."
        ),
        (
            "O status da devolução à filial deve "
            "ser ACTIVE ou CANCELLED."
        ),
    ],
)
def test_should_return_400_when_business_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create_transfer_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
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
    service.create_transfer_return.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/transfer-returns",
        json={
            "transfer_id": 10,
            "dispatch_invoice_number": (
                "NF-RETURN-100"
            ),
            "issue_date": "2026-08-05",
            "created_by": 50,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_transfer_returns(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_transfer_returns.return_value = [
        create_transfer_return(),
        create_transfer_return(
            transfer_return_id=31,
            dispatch_invoice_number=(
                "NF-RETURN-200"
            ),
            dispatch_invoice_series=None,
            notes=None,
        ),
    ]

    response = client.get(
        "/transfer-returns"
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_transfer_return_response(),
        expected_transfer_return_response(
            transfer_return_id=31,
            dispatch_invoice_number=(
                "NF-RETURN-200"
            ),
            dispatch_invoice_series=None,
            notes=None,
        ),
    ]

    service.list_transfer_returns.assert_called_once_with()


def test_should_return_empty_transfer_return_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_transfer_returns.return_value = []

    response = client.get(
        "/transfer-returns"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_transfer_returns.assert_called_once_with()


def test_should_list_transfer_returns_by_transfer(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_by_transfer.return_value = [
        create_transfer_return(),
        create_transfer_return(
            transfer_return_id=31,
            dispatch_invoice_number=(
                "NF-RETURN-200"
            ),
        ),
    ]

    response = client.get(
        "/transfer-returns/transfer/10"
    )

    assert response.status_code == 200

    assert len(
        response.json()
    ) == 2

    service.list_by_transfer.assert_called_once_with(
        10
    )


def test_should_return_empty_list_by_transfer(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_by_transfer.return_value = []

    response = client.get(
        "/transfer-returns/transfer/10"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_by_transfer.assert_called_once_with(
        10
    )


def test_should_return_404_when_transfer_is_not_found_on_list(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Transferência não encontrada."

    service.list_by_transfer.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/transfer-returns/transfer/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.list_by_transfer.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_id_is_invalid_on_list(
    client: TestClient,
    service: Mock,
    transfer_id: int,
) -> None:
    response = client.get(
        (
            "/transfer-returns/transfer/"
            f"{transfer_id}"
        )
    )

    assert response.status_code == 422

    service.list_by_transfer.assert_not_called()


def test_should_get_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_available_quantity.return_value = 6

    response = client.get(
        (
            "/transfer-returns/transfer-items/"
            "20/available-quantity"
        )
    )

    assert response.status_code == 200

    assert response.json() == {
        "transfer_item_id": 20,
        "available_quantity": 6,
    }

    service.get_available_quantity.assert_called_once_with(
        20
    )


def test_should_return_zero_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_available_quantity.return_value = 0

    response = client.get(
        (
            "/transfer-returns/transfer-items/"
            "20/available-quantity"
        )
    )

    assert response.status_code == 200

    assert response.json() == {
        "transfer_item_id": 20,
        "available_quantity": 0,
    }


def test_should_return_404_when_transfer_item_is_not_found_on_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Item de transferência não encontrado."

    service.get_available_quantity.side_effect = (
        ValueError(message)
    )

    response = client.get(
        (
            "/transfer-returns/transfer-items/"
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
    "transfer_item_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_item_id_is_invalid_on_available_quantity(
    client: TestClient,
    service: Mock,
    transfer_item_id: int,
) -> None:
    response = client.get(
        (
            "/transfer-returns/transfer-items/"
            f"{transfer_item_id}/available-quantity"
        )
    )

    assert response.status_code == 422

    service.get_available_quantity.assert_not_called()


def test_should_get_transfer_return(
    client: TestClient,
    service: Mock,
) -> None:
    transfer_return = create_transfer_return()

    service.get_transfer_return.return_value = (
        transfer_return
    )

    response = client.get(
        "/transfer-returns/30"
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_transfer_return_response()
    )

    service.get_transfer_return.assert_called_once_with(
        30
    )


def test_should_return_404_when_transfer_return_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Devolução à filial não encontrada."

    service.get_transfer_return.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/transfer-returns/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.get_transfer_return.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "transfer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_return_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    transfer_return_id: int,
) -> None:
    response = client.get(
        (
            "/transfer-returns/"
            f"{transfer_return_id}"
        )
    )

    assert response.status_code == 422

    service.get_transfer_return.assert_not_called()


def test_should_add_transfer_return_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    transfer_return_item = (
        create_transfer_return_item()
    )

    service.add_item.return_value = (
        transfer_return_item
    )

    response = client.post(
        "/transfer-returns/30/items",
        json={
            "transfer_item_id": 20,
            "quantity": 4,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 60,
        "transfer_return_id": 30,
        "transfer_item_id": 20,
        "quantity": 4,
        "created_at": "2026-08-05T17:35:00",
    }

    service.add_item.assert_called_once_with(
        transfer_return_id=30,
        transfer_item_id=20,
        quantity=4,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        transfer_return_item
    )

    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Devolução à filial não encontrada.",
            404,
        ),
        (
            "Item de transferência não encontrado.",
            404,
        ),
        (
            (
                "Este item de transferência já foi "
                "adicionado à devolução."
            ),
            409,
        ),
        (
            (
                "Não é possível adicionar itens a uma "
                "devolução à filial que não está ativa."
            ),
            400,
        ),
        (
            (
                "O item informado não pertence à "
                "transferência vinculada à devolução."
            ),
            400,
        ),
        (
            (
                "Não existe quantidade disponível para "
                "devolução à filial neste item de "
                "transferência."
            ),
            400,
        ),
        (
            (
                "A quantidade devolvida é maior que a "
                "quantidade disponível para devolução "
                "à filial. Quantidade máxima permitida: "
                "2."
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
        "/transfer-returns/30/items",
        json={
            "transfer_item_id": 20,
            "quantity": 4,
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    service.add_item.assert_called_once_with(
        transfer_return_id=30,
        transfer_item_id=20,
        quantity=4,
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "transfer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_return_id_is_invalid_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    transfer_return_id: int,
) -> None:
    response = client.post(
        (
            "/transfer-returns/"
            f"{transfer_return_id}/items"
        ),
        json={
            "transfer_item_id": 20,
            "quantity": 4,
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    "payload",
    [
        {
            "quantity": 4,
        },
        {
            "transfer_item_id": 20,
        },
        {
            "transfer_item_id": 0,
            "quantity": 4,
        },
        {
            "transfer_item_id": -1,
            "quantity": 4,
        },
        {
            "transfer_item_id": 20,
            "quantity": 0,
        },
        {
            "transfer_item_id": 20,
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
        "/transfer-returns/30/items",
        json=payload,
    )

    assert response.status_code == 422

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
        "/transfer-returns/30/items",
        json={
            "transfer_item_id": 20,
            "quantity": 4,
            "unexpected_field": "value",
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
    service.add_item.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/transfer-returns/30/items",
        json={
            "transfer_item_id": 20,
            "quantity": 4,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_transfer_return_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_items.return_value = [
        create_transfer_return_item(),
        create_transfer_return_item(
            transfer_return_item_id=61,
            transfer_item_id=21,
            quantity=2,
        ),
    ]

    response = client.get(
        "/transfer-returns/30/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 60,
            "transfer_return_id": 30,
            "transfer_item_id": 20,
            "quantity": 4,
            "created_at": "2026-08-05T17:35:00",
        },
        {
            "id": 61,
            "transfer_return_id": 30,
            "transfer_item_id": 21,
            "quantity": 2,
            "created_at": "2026-08-05T17:35:00",
        },
    ]

    service.list_items.assert_called_once_with(
        30
    )


def test_should_return_empty_transfer_return_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_items.return_value = []

    response = client.get(
        "/transfer-returns/30/items"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_items.assert_called_once_with(
        30
    )


def test_should_return_404_when_transfer_return_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Devolução à filial não encontrada."

    service.list_items.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/transfer-returns/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.list_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "transfer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_return_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    transfer_return_id: int,
) -> None:
    response = client.get(
        (
            "/transfer-returns/"
            f"{transfer_return_id}/items"
        )
    )

    assert response.status_code == 422

    service.list_items.assert_not_called()