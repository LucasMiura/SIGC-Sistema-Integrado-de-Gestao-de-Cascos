from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.transfer_route import (
    get_transfer_service,
    router,
)
from src.database.connection import get_session
from src.services.transfer_service import (
    TransferService,
)
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_BUYER,
)
from src.api.dependencies.audit import (
    get_audit_service,
)
from src.services.audit_service import (
    AuditService,
)


@pytest.fixture
def session() -> Mock:
    """Cria uma sessão de banco simulada."""

    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    """Cria um TransferService simulado."""

    return Mock(
        spec=TransferService,
    )


@pytest.fixture
def audit_service() -> Mock:
    """Cria um AuditService simulado."""

    return Mock(
        spec=AuditService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
    audit_service: Mock,
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

    def override_get_transfer_service():
        return service

    def override_get_audit_service():
        return audit_service

    def override_get_current_user():
        return buyer_user

    session.scalar.return_value = (
        buyer_role
    )

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_transfer_service
    ] = override_get_transfer_service

    test_app.dependency_overrides[
        get_audit_service
    ] = override_get_audit_service

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


def create_transfer(
    transfer_id: int = 10,
    origin_branch_id: int = 2,
    destination_branch_id: int = 1,
    invoice_number: str = "NF-TRANSFER-100",
    issue_date: str = "2026-08-05",
    status: str = "ACTIVE",
    created_by: int = 30,
) -> SimpleNamespace:
    """Cria uma transferência simulada."""

    return SimpleNamespace(
        id=transfer_id,
        origin_branch_id=origin_branch_id,
        destination_branch_id=destination_branch_id,
        invoice_number=invoice_number,
        issue_date=issue_date,
        status=status,
        created_by=created_by,
    )


def create_transfer_item(
    transfer_item_id: int = 20,
    transfer_id: int = 10,
    part_id: int = 40,
    quantity: int = 10,
    quantity_available: int = 10,
    return_deadline_days: int = 45,
) -> SimpleNamespace:
    """Cria um item de transferência simulado."""

    return SimpleNamespace(
        id=transfer_item_id,
        transfer_id=transfer_id,
        part_id=part_id,
        quantity=quantity,
        quantity_available=quantity_available,
        return_deadline_days=return_deadline_days,
    )


def test_should_create_transfer(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    transfer = create_transfer()

    service.create_transfer.return_value = transfer

    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
            "status": "ACTIVE",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "origin_branch_id": 2,
        "destination_branch_id": 1,
        "invoice_number": "NF-TRANSFER-100",
        "issue_date": "2026-08-05",
        "status": "ACTIVE",
        "created_by": 30,
    }

    service.create_transfer.assert_called_once_with(
        origin_branch_id=2,
        destination_branch_id=1,
        invoice_number="NF-TRANSFER-100",
        issue_date="2026-08-05",
        created_by=30,
        status="ACTIVE",
    )

    audit_service.register.assert_called_once_with(
        user_id=30,
        action="CREATE",
        module="TRANSFER",
        entity_type="Transfer",
        entity_id=10,
        description="Transferência cadastrada.",
        new_values={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
            "status": "ACTIVE",
            "created_by": 30,
        },
    )

    session.commit.assert_called_once_with()
    session.refresh.assert_called_once_with(
        transfer
    )
    session.rollback.assert_not_called()


def test_should_create_transfer_with_default_status(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    transfer = create_transfer()

    service.create_transfer.return_value = transfer

    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 201

    service.create_transfer.assert_called_once_with(
        origin_branch_id=2,
        destination_branch_id=1,
        invoice_number="NF-TRANSFER-100",
        issue_date="2026-08-05",
        created_by=30,
        status="ACTIVE",
    )

    audit_service.register.assert_called_once_with(
        user_id=30,
        action="CREATE",
        module="TRANSFER",
        entity_type="Transfer",
        entity_id=10,
        description="Transferência cadastrada.",
        new_values={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
            "status": "ACTIVE",
            "created_by": 30,
        },
    )

    session.commit.assert_called_once_with()
    session.refresh.assert_called_once_with(
        transfer
    )


@pytest.mark.parametrize(
    (
        "payload",
        "missing_field",
    ),
    [
        (
            {
                "destination_branch_id": 1,
                "invoice_number": "NF-TRANSFER-100",
                "issue_date": "2026-08-05",
            },
            "origin_branch_id",
        ),
        (
            {
                "origin_branch_id": 2,
                "invoice_number": "NF-TRANSFER-100",
                "issue_date": "2026-08-05",
            },
            "destination_branch_id",
        ),
        (
            {
                "origin_branch_id": 2,
                "destination_branch_id": 1,
                "issue_date": "2026-08-05",
            },
            "invoice_number",
        ),
        (
            {
                "origin_branch_id": 2,
                "destination_branch_id": 1,
                "invoice_number": "NF-TRANSFER-100",
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
        "/transfers",
        json=payload,
    )

    assert response.status_code == 422
    assert missing_field in response.text

    service.create_transfer.assert_not_called()
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
            "origin_branch_id",
            0,
        ),
        (
            "origin_branch_id",
            -1,
        ),
        (
            "destination_branch_id",
            0,
        ),
        (
            "destination_branch_id",
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
        "origin_branch_id": 2,
        "destination_branch_id": 1,
        "invoice_number": "NF-TRANSFER-100",
        "issue_date": "2026-08-05",
    }

    payload[field] = value

    response = client.post(
        "/transfers",
        json=payload,
    )

    assert response.status_code == 422

    service.create_transfer.assert_not_called()
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
            "invoice_number",
            "",
        ),
        (
            "invoice_number",
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
        "origin_branch_id": 2,
        "destination_branch_id": 1,
        "invoice_number": "NF-TRANSFER-100",
        "issue_date": "2026-08-05",
        "created_by": 30,
    }

    payload[field] = value

    response = client.post(
        "/transfers",
        json=payload,
    )

    assert response.status_code == 422

    service.create_transfer.assert_not_called()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_create_status_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
            "status": "FINISHED",
        },
    )

    assert response.status_code == 422

    service.create_transfer.assert_not_called()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",           
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service.create_transfer.assert_not_called()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_409_when_transfer_invoice_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "Já existe uma transferência cadastrada "
        "com esse número de Nota Fiscal."
    )

    service.create_transfer.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
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
        (
            "A filial de origem deve ser diferente "
            "da filial de destino."
        ),
        (
            "Uma transferência não pode ser criada "
            "já cancelada."
        ),
        (
            "O status da transferência deve ser "
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
    service.create_transfer.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
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
    service.create_transfer.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_transfers(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_transfers.return_value = [
        create_transfer(),
        create_transfer(
            transfer_id=11,
            origin_branch_id=3,
            invoice_number="NF-TRANSFER-200",
        ),
    ]

    response = client.get(
        "/transfers"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 10,
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
            "status": "ACTIVE",
            "created_by": 30,
        },
        {
            "id": 11,
            "origin_branch_id": 3,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-200",
            "issue_date": "2026-08-05",
            "status": "ACTIVE",
            "created_by": 30,
        },
    ]

    service.list_transfers.assert_called_once_with()


def test_should_return_empty_transfer_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_transfers.return_value = []

    response = client.get(
        "/transfers"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_transfers.assert_called_once_with()


def test_should_get_transfer(
    client: TestClient,
    service: Mock,
) -> None:
    transfer = create_transfer()

    service.get_transfer.return_value = transfer

    response = client.get(
        "/transfers/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "origin_branch_id": 2,
        "destination_branch_id": 1,
        "invoice_number": "NF-TRANSFER-100",
        "issue_date": "2026-08-05",
        "status": "ACTIVE",
        "created_by": 30,
    }

    service.get_transfer.assert_called_once_with(
        10
    )


def test_should_return_404_when_transfer_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Transferência não encontrada."

    service.get_transfer.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/transfers/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.get_transfer.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    transfer_id: int,
) -> None:
    response = client.get(
        f"/transfers/{transfer_id}"
    )

    assert response.status_code == 422

    service.get_transfer.assert_not_called()


def test_should_add_transfer_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    transfer_item = create_transfer_item()

    service.add_item.return_value = (
        transfer_item
    )

    response = client.post(
        "/transfers/10/items",
        json={
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 45,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 20,
        "transfer_id": 10,
        "part_id": 40,
        "quantity": 10,
        "quantity_available": 10,
        "return_deadline_days": 45,
    }

    service.add_item.assert_called_once_with(
        transfer_id=10,
        part_id=40,
        quantity=10,
        return_deadline_days=45,
    )

    audit_service.register.assert_called_once_with(
        user_id=30,
        action="CREATE",
        module="TRANSFER",
        entity_type="TransferItem",
        entity_id=20,
        description=(
            "Item adicionado à transferência."
        ),
        new_values={
            "transfer_id": 10,
            "part_id": 40,
            "quantity": 10,
            "quantity_available": 10,
            "return_deadline_days": 45,
        },
    )

    session.commit.assert_called_once_with()
    session.refresh.assert_called_once_with(
        transfer_item
    )
    session.rollback.assert_not_called()

def test_should_rollback_when_audit_fails_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    transfer_item = create_transfer_item()

    service.add_item.return_value = (
        transfer_item
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.post(
        "/transfers/10/items",
        json={
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 45,
        },
    )

    assert response.status_code == 500

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_rollback_when_audit_fails_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    transfer = create_transfer()

    service.create_transfer.return_value = (
        transfer
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.post(
        "/transfers",
        json={
            "origin_branch_id": 2,
            "destination_branch_id": 1,
            "invoice_number": "NF-TRANSFER-100",
            "issue_date": "2026-08-05",
        },
    )

    assert response.status_code == 500

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Transferência não encontrada.",
            404,
        ),
        (
            "Peça não encontrada.",
            404,
        ),
        (
            (
                "Esta peça já foi adicionada "
                "à transferência."
            ),
            409,
        ),
        (
            (
                "Não é possível adicionar itens a uma "
                "transferência que não está ativa."
            ),
            400,
        ),
        (
            "A peça informada está inativa.",
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
        "/transfers/10/items",
        json={
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 45,
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    service.add_item.assert_called_once_with(
        transfer_id=10,
        part_id=40,
        quantity=10,
        return_deadline_days=45,
    )

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_id_is_invalid_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    transfer_id: int,
) -> None:
    response = client.post(
        f"/transfers/{transfer_id}/items",
        json={
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 45,
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
            "quantity": 10,
            "return_deadline_days": 45,
        },
        {
            "part_id": 40,
            "return_deadline_days": 45,
        },
        {
            "part_id": 40,
            "quantity": 10,
        },
        {
            "part_id": 0,
            "quantity": 10,
            "return_deadline_days": 45,
        },
        {
            "part_id": -1,
            "quantity": 10,
            "return_deadline_days": 45,
        },
        {
            "part_id": 40,
            "quantity": 0,
            "return_deadline_days": 45,
        },
        {
            "part_id": 40,
            "quantity": -1,
            "return_deadline_days": 45,
        },
        {
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 0,
        },
        {
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": -1,
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
        "/transfers/10/items",
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
        "/transfers/10/items",
        json={
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 45,
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
        "/transfers/10/items",
        json={
            "part_id": 40,
            "quantity": 10,
            "return_deadline_days": 45,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_transfer_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_items.return_value = [
        create_transfer_item(),
        create_transfer_item(
            transfer_item_id=21,
            part_id=41,
            quantity=5,
            quantity_available=3,
            return_deadline_days=30,
        ),
    ]

    response = client.get(
        "/transfers/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 20,
            "transfer_id": 10,
            "part_id": 40,
            "quantity": 10,
            "quantity_available": 10,
            "return_deadline_days": 45,
        },
        {
            "id": 21,
            "transfer_id": 10,
            "part_id": 41,
            "quantity": 5,
            "quantity_available": 3,
            "return_deadline_days": 30,
        },
    ]

    service.list_items.assert_called_once_with(
        10
    )


def test_should_return_empty_transfer_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_items.return_value = []

    response = client.get(
        "/transfers/10/items"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_transfer_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Transferência não encontrada."

    service.list_items.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/transfers/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.list_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    transfer_id: int,
) -> None:
    response = client.get(
        f"/transfers/{transfer_id}/items"
    )

    assert response.status_code == 422

    service.list_items.assert_not_called()


def test_should_get_transfer_item(
    client: TestClient,
    service: Mock,
) -> None:
    transfer_item = create_transfer_item()

    service.get_transfer_item.return_value = (
        transfer_item
    )

    response = client.get(
        "/transfers/items/20"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 20,
        "transfer_id": 10,
        "part_id": 40,
        "quantity": 10,
        "quantity_available": 10,
        "return_deadline_days": 45,
    }

    service.get_transfer_item.assert_called_once_with(
        20
    )


def test_should_return_404_when_transfer_item_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Item de transferência não encontrado."

    service.get_transfer_item.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/transfers/items/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.get_transfer_item.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "transfer_item_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_item_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    transfer_item_id: int,
) -> None:
    response = client.get(
        f"/transfers/items/{transfer_item_id}"
    )

    assert response.status_code == 422

    service.get_transfer_item.assert_not_called()


def test_should_get_available_quantity(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_available_quantity.return_value = 6

    response = client.get(
        "/transfers/items/20/available"
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
        "/transfers/items/20/available"
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
        "/transfers/items/999/available"
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
            "/transfers/items/"
            f"{transfer_item_id}/available"
        )
    )

    assert response.status_code == 422

    service.get_available_quantity.assert_not_called()


def test_should_cancel_transfer(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    existing_transfer = create_transfer(
        status="ACTIVE",
    )

    cancelled_transfer = create_transfer(
        status="CANCELLED",
    )

    service.get_transfer.return_value = (
        existing_transfer
    )

    service.cancel_transfer.return_value = (
        cancelled_transfer
    )

    response = client.post(
        "/transfers/10/cancel",
        json={
            "justification": (
                "Transferência lançada "
                "incorretamente."
            ),
        },
    )

    assert response.status_code == 200

    assert response.json()[
        "status"
    ] == "CANCELLED"

    service.get_transfer.assert_called_once_with(
        10
    )

    service.cancel_transfer.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once_with(
        user_id=30,
        action="CANCEL",
        module="TRANSFER",
        entity_type="Transfer",
        entity_id=10,
        description=(
            "Transferência cancelada."
        ),
        old_values={
            "status": "ACTIVE",
        },
        new_values={
            "status": "CANCELLED",
        },
        justification=(
            "Transferência lançada "
            "incorretamente."
        ),
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        cancelled_transfer
    )

    session.rollback.assert_not_called()

@pytest.mark.parametrize(
    "payload",
    [
        {},
        {
            "justification": "",
        },
        {
            "justification": "   ",
        },
    ],
)
def test_should_return_422_when_cancel_justification_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, object],
) -> None:
    response = client.post(
        "/transfers/10/cancel",
        json=payload,
    )

    assert response.status_code == 422

    service.get_transfer.assert_not_called()
    service.cancel_transfer.assert_not_called()

def test_should_return_422_when_cancel_payload_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.post(
        "/transfers/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
            "unknown_field": "valor",
        },
    )

    assert response.status_code == 422

    service.get_transfer.assert_not_called()
    service.cancel_transfer.assert_not_called()

def test_should_rollback_when_audit_fails_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    service.get_transfer.return_value = (
        create_transfer(
            status="ACTIVE",
        )
    )

    service.cancel_transfer.return_value = (
        create_transfer(
            status="CANCELLED",
        )
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.post(
        "/transfers/10/cancel",
        json={
            "justification": (
                "Transferência lançada "
                "incorretamente."
            ),
        },
    )

    assert response.status_code == 500

    service.get_transfer.assert_called_once_with(
        10
    )

    service.cancel_transfer.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_strip_cancel_justification(
    client: TestClient,
    service: Mock,
    audit_service: Mock,
) -> None:
    service.get_transfer.return_value = (
        create_transfer(
            status="ACTIVE",
        )
    )

    service.cancel_transfer.return_value = (
        create_transfer(
            status="CANCELLED",
        )
    )

    response = client.post(
        "/transfers/10/cancel",
        json={
            "justification": (
                "  Erro no lançamento.  "
            ),
        },
    )

    assert response.status_code == 200

    assert (
        audit_service.register.call_args.kwargs[
            "justification"
        ]
        == "Erro no lançamento."
    )


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Transferência não encontrada.",
            404,
        ),
        (
            "A transferência já está cancelada.",
            409,
        ),
        (
            (
                "Não é possível cancelar uma "
                "transferência que possui movimentações."
            ),
            400,
        ),
    ],
)
def test_should_convert_business_error_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
    expected_status: int,
) -> None:
    service.get_transfer.return_value = (
        create_transfer(
            status="ACTIVE",
        )
    )

    service.cancel_transfer.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/transfers/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_transfer_id_is_invalid_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
    transfer_id: int,
) -> None:
    response = client.post(
        f"/transfers/{transfer_id}/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 422

    service.cancel_transfer.assert_not_called()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.get_transfer.return_value = (
        create_transfer(
            status="ACTIVE",
        )
    )
    service.cancel_transfer.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/transfers/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()