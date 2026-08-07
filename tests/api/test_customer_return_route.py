from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.customer_return_route import (
    get_customer_return_service,
    router,
)
from src.database.connection import get_session
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_SELLER,
)


@pytest.fixture
def session() -> Mock:
    """
    Cria uma sessão de banco simulada.
    """

    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    """
    Cria um CustomerReturnService simulado.
    """

    return Mock(
        spec=CustomerReturnService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    """
    Cria uma aplicação isolada simulando
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

    def override_get_customer_return_service():
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
        get_customer_return_service
    ] = override_get_customer_return_service

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
    """
    Cria o cliente HTTP da aplicação de teste.
    """

    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_customer_return(
    customer_return_id: int = 10,
    return_type: str = "WORK_ORDER",
    reference_number: str = "OS-12345",
    customer_name: str = "Cliente Teste",
    created_by: int = 30,
    created_at: str = "2026-07-30T10:00:00",
    updated_at: str = "2026-07-30T10:00:00",
    status: str = "ACTIVE",
    notes: str | None = "Devolução de teste.",
) -> SimpleNamespace:
    """
    Cria uma devolução simulada.
    """

    return SimpleNamespace(
        id=customer_return_id,
        return_type=return_type,
        reference_number=reference_number,
        customer_name=customer_name,
        created_by=created_by,
        created_at=created_at,
        updated_at=updated_at,
        status=status,
        notes=notes,
    )


def create_customer_return_item(
    customer_return_item_id: int = 20,
    customer_return_id: int = 10,
    part_id: int = 40,
    quantity: int = 3,
    created_at: str = "2026-07-30T10:05:00",
) -> SimpleNamespace:
    """
    Cria um item de devolução simulado.
    """

    return SimpleNamespace(
        id=customer_return_item_id,
        customer_return_id=customer_return_id,
        part_id=part_id,
        quantity=quantity,
        created_at=created_at,
    )


def test_should_create_customer_return(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    customer_return = create_customer_return()

    service.create_customer_return.return_value = (
        customer_return
    )

    response = client.post(
        "/customer-returns",
        json={
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
            "status": "ACTIVE",
            "notes": "Devolução de teste.",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "return_type": "WORK_ORDER",
        "reference_number": "OS-12345",
        "customer_name": "Cliente Teste",
        "created_by": 30,
        "created_at": "2026-07-30T10:00:00",
        "updated_at": "2026-07-30T10:00:00",
        "status": "ACTIVE",
        "notes": "Devolução de teste.",
    }

    service.create_customer_return.assert_called_once_with(
        return_type="WORK_ORDER",
        reference_number="OS-12345",
        customer_name="Cliente Teste",
        created_by=30,
        status="ACTIVE",
        notes="Devolução de teste.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        customer_return
    )

    session.rollback.assert_not_called()


def test_should_create_sale_customer_return(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    customer_return = create_customer_return(
        return_type="SALE",
        reference_number="NFV-12345",
    )

    service.create_customer_return.return_value = (
        customer_return
    )

    response = client.post(
        "/customer-returns",
        json={
            "return_type": "SALE",
            "reference_number": "NFV-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 201

    assert response.json()[
        "return_type"
    ] == "SALE"

    assert response.json()[
        "reference_number"
    ] == "NFV-12345"

    service.create_customer_return.assert_called_once_with(
        return_type="SALE",
        reference_number="NFV-12345",
        customer_name="Cliente Teste",
        created_by=30,
        status="ACTIVE",
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        customer_return
    )


def test_should_create_customer_return_without_notes(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    customer_return = create_customer_return(
        notes=None,
    )

    service.create_customer_return.return_value = (
        customer_return
    )

    response = client.post(
        "/customer-returns",
        json={
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 201

    assert response.json()["notes"] is None

    service.create_customer_return.assert_called_once_with(
        return_type="WORK_ORDER",
        reference_number="OS-12345",
        customer_name="Cliente Teste",
        created_by=30,
        status="ACTIVE",
        notes=None,
    )


@pytest.mark.parametrize(
    (
        "payload",
        "missing_field",
    ),
    [
        (
            {
                "reference_number": "OS-12345",
                "customer_name": "Cliente Teste",
            },
            "return_type",
        ),
        (
            {
                "return_type": "WORK_ORDER",
                "customer_name": "Cliente Teste",
            },
            "reference_number",
        ),
        (
            {
                "return_type": "WORK_ORDER",
                "reference_number": "OS-12345",
            },
            "customer_name",
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
        "/customer-returns",
        json=payload,
    )

    assert response.status_code == 422

    assert missing_field in response.text

    service.create_customer_return.assert_not_called()

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
            "return_type",
            "TRANSFER",
        ),
        (
            "status",
            "FINISHED",
        ),
    ],
)
def test_should_return_422_when_create_enum_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    value: str,
) -> None:
    payload = {
        "return_type": "WORK_ORDER",
        "reference_number": "OS-12345",
        "customer_name": "Cliente Teste",
        "status": "ACTIVE",
    }

    payload[field] = value

    response = client.post(
        "/customer-returns",
        json=payload,
    )

    assert response.status_code == 422

    service.create_customer_return.assert_not_called()

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
            "reference_number",
            "",
        ),
        (
            "reference_number",
            "   ",
        ),
        (
            "customer_name",
            "",
        ),
        (
            "customer_name",
            "   ",
        ),
    ],
)
def test_should_return_422_when_required_text_is_empty(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    value: str,
) -> None:
    payload = {
        "return_type": "WORK_ORDER",
        "reference_number": "OS-12345",
        "customer_name": "Cliente Teste",
    }

    payload[field] = value

    response = client.post(
        "/customer-returns",
        json=payload,
    )

    assert response.status_code == 422

    service.create_customer_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/customer-returns",
        json={
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service.create_customer_return.assert_not_called()

    session.commit.assert_not_called()
    session.rollback.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        "Saída original não encontrada.",
        "Peça não encontrada.",
    ],
)
def test_should_return_404_when_related_resource_is_not_found_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create_customer_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/customer-returns",
        json={
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 404

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
            "A referência informada não corresponde "
            "ao tipo de devolução."
        ),
        "A saída original não está ativa.",
        (
            "O tipo de devolução deve ser "
            "WORK_ORDER ou SALE."
        ),
    ],
)
def test_should_return_400_when_business_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create_customer_return.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/customer-returns",
        json={
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
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
    service.create_customer_return.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/customer-returns",
        json={
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_customer_returns(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_customer_returns.return_value = [
        create_customer_return(),
        create_customer_return(
            customer_return_id=11,
            return_type="SALE",
            reference_number="NFV-98765",
            customer_name="Outro Cliente",
            notes=None,
        ),
    ]

    response = client.get(
        "/customer-returns"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 10,
            "return_type": "WORK_ORDER",
            "reference_number": "OS-12345",
            "customer_name": "Cliente Teste",
            "created_by": 30,
            "created_at": "2026-07-30T10:00:00",
            "updated_at": "2026-07-30T10:00:00",
            "status": "ACTIVE",
            "notes": "Devolução de teste.",
        },
        {
            "id": 11,
            "return_type": "SALE",
            "reference_number": "NFV-98765",
            "customer_name": "Outro Cliente",
            "created_by": 30,
            "created_at": "2026-07-30T10:00:00",
            "updated_at": "2026-07-30T10:00:00",
            "status": "ACTIVE",
            "notes": None,
        },
    ]

    service.list_customer_returns.assert_called_once_with()


def test_should_return_empty_customer_return_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_customer_returns.return_value = []

    response = client.get(
        "/customer-returns"
    )

    assert response.status_code == 200

    assert response.json() == []

    service.list_customer_returns.assert_called_once_with()


def test_should_get_customer_return(
    client: TestClient,
    service: Mock,
) -> None:
    customer_return = create_customer_return()

    service.get_customer_return.return_value = (
        customer_return
    )

    response = client.get(
        "/customer-returns/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "return_type": "WORK_ORDER",
        "reference_number": "OS-12345",
        "customer_name": "Cliente Teste",
        "created_by": 30,
        "created_at": "2026-07-30T10:00:00",
        "updated_at": "2026-07-30T10:00:00",
        "status": "ACTIVE",
        "notes": "Devolução de teste.",
    }

    service.get_customer_return.assert_called_once_with(
        10
    )


def test_should_return_404_when_customer_return_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_customer_return.side_effect = (
        ValueError(
            "Devolução do cliente não encontrada."
        )
    )

    response = client.get(
        "/customer-returns/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": (
            "Devolução do cliente não encontrada."
        ),
    }

    service.get_customer_return.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "customer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_customer_return_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    customer_return_id: int,
) -> None:
    response = client.get(
        (
            "/customer-returns/"
            f"{customer_return_id}"
        )
    )

    assert response.status_code == 422

    service.get_customer_return.assert_not_called()


def test_should_add_customer_return_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    customer_return_item = (
        create_customer_return_item()
    )

    service.add_item.return_value = (
        customer_return_item
    )

    response = client.post(
        "/customer-returns/10/items",
        json={
            "part_id": 40,
            "quantity": 3,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 20,
        "customer_return_id": 10,
        "part_id": 40,
        "quantity": 3,
        "created_at": "2026-07-30T10:05:00",
    }

    service.add_item.assert_called_once_with(
        customer_return_id=10,
        part_id=40,
        quantity=3,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        customer_return_item
    )

    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Devolução do cliente não encontrada.",
            404,
        ),
        (
            "Peça não encontrada.",
            404,
        ),
        (
            "Saída original não encontrada.",
            404,
        ),
        (
            (
                "Não é possível adicionar itens a uma "
                "devolução que não esteja ativa."
            ),
            400,
        ),
        (
            (
                "A peça não pertence à saída original "
                "informada."
            ),
            400,
        ),
        (
            (
                "A quantidade devolvida é superior "
                "à quantidade pendente da saída original."
            ),
            400,
        ),
        (
            "A saída original não está ativa.",
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
        "/customer-returns/10/items",
        json={
            "part_id": 40,
            "quantity": 3,
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    service.add_item.assert_called_once_with(
        customer_return_id=10,
        part_id=40,
        quantity=3,
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "customer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_customer_return_id_is_invalid_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    customer_return_id: int,
) -> None:
    response = client.post(
        (
            "/customer-returns/"
            f"{customer_return_id}/items"
        ),
        json={
            "part_id": 40,
            "quantity": 3,
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
            "quantity": 3,
        },
        {
            "part_id": 40,
        },
        {
            "part_id": 0,
            "quantity": 3,
        },
        {
            "part_id": -1,
            "quantity": 3,
        },
        {
            "part_id": 40,
            "quantity": 0,
        },
        {
            "part_id": 40,
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
        "/customer-returns/10/items",
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
        "/customer-returns/10/items",
        json={
            "part_id": 40,
            "quantity": 3,
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
        "/customer-returns/10/items",
        json={
            "part_id": 40,
            "quantity": 3,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_customer_return_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_customer_return_items.return_value = [
        create_customer_return_item(),
        create_customer_return_item(
            customer_return_item_id=21,
            part_id=41,
            quantity=2,
        ),
    ]

    response = client.get(
        "/customer-returns/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 20,
            "customer_return_id": 10,
            "part_id": 40,
            "quantity": 3,
            "created_at": "2026-07-30T10:05:00",
        },
        {
            "id": 21,
            "customer_return_id": 10,
            "part_id": 41,
            "quantity": 2,
            "created_at": "2026-07-30T10:05:00",
        },
    ]

    service.list_customer_return_items.assert_called_once_with(
        10
    )


def test_should_return_empty_customer_return_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_customer_return_items.return_value = []

    response = client.get(
        "/customer-returns/10/items"
    )

    assert response.status_code == 200

    assert response.json() == []

    service.list_customer_return_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_customer_return_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_customer_return_items.side_effect = (
        ValueError(
            "Devolução do cliente não encontrada."
        )
    )

    response = client.get(
        "/customer-returns/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": (
            "Devolução do cliente não encontrada."
        ),
    }

    service.list_customer_return_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "customer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_customer_return_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    customer_return_id: int,
) -> None:
    response = client.get(
        (
            "/customer-returns/"
            f"{customer_return_id}/items"
        )
    )

    assert response.status_code == 422

    service.list_customer_return_items.assert_not_called()

def test_should_allow_buyer_to_list_customer_returns(
    session: Mock,
    service: Mock,
) -> None:
    test_app = FastAPI()

    buyer_user = SimpleNamespace(
        id=20,
        username="comprador",
        role_id=2,
        is_active=1,
    )

    buyer_role = SimpleNamespace(
        id=2,
        name="Comprador",
    )

    def override_get_session():
        yield session

    def override_get_customer_return_service():
        return service

    def override_get_current_user():
        return buyer_user

    session.scalar.return_value = (
        buyer_role
    )

    service.list_customer_returns.return_value = []

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_customer_return_service
    ] = override_get_customer_return_service

    test_app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    test_app.include_router(
        router
    )

    client = TestClient(
        test_app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/customer-returns"
    )

    assert response.status_code == 200

    service.list_customer_returns.assert_called_once_with()