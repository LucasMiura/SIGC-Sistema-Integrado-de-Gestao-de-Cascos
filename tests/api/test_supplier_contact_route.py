from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.supplier_contact_route import (
    get_supplier_contact_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.supplier_contact_service import (
    SupplierContactService,
)


@pytest.fixture
def service_mock() -> Mock:
    """Cria um mock do serviço de contatos."""

    return Mock(spec=SupplierContactService)


@pytest.fixture
def session_mock() -> Mock:
    """Cria um mock da sessão SQLAlchemy."""

    session = Mock()

    session.commit.return_value = None
    session.rollback.return_value = None
    session.refresh.return_value = None

    return session


@pytest.fixture
def client(
    service_mock: Mock,
    session_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo as dependências reais.
    """

    def override_supplier_contact_service() -> Mock:
        return service_mock

    def override_session() -> Generator[Mock, None, None]:
        yield session_mock

    app.dependency_overrides[
        get_supplier_contact_service
    ] = override_supplier_contact_service

    app.dependency_overrides[
        get_session
    ] = override_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_contact(
    *,
    contact_id: int = 10,
    supplier_id: int = 1,
    name: str = "João Silva",
    email: str | None = "joao@fornecedor.com",
    phone: str | None = "(13) 99999-1111",
    position: str | None = "Garantia",
    is_primary: int = 1,
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados
    pelo schema de resposta.
    """

    return SimpleNamespace(
        id=contact_id,
        supplier_id=supplier_id,
        name=name,
        email=email,
        phone=phone,
        position=position,
        is_primary=is_primary,
        is_active=is_active,
        created_at="2026-07-28T15:00:00",
    )


def expected_contact_json(
    *,
    contact_id: int = 10,
    supplier_id: int = 1,
    name: str = "João Silva",
    email: str | None = "joao@fornecedor.com",
    phone: str | None = "(13) 99999-1111",
    position: str | None = "Garantia",
    is_primary: bool = True,
    is_active: bool = True,
) -> dict[str, object]:
    """Retorna o JSON esperado nas respostas."""

    return {
        "id": contact_id,
        "supplier_id": supplier_id,
        "name": name,
        "email": email,
        "phone": phone,
        "position": position,
        "is_primary": is_primary,
        "is_active": is_active,
        "created_at": "2026-07-28T15:00:00",
    }


def test_should_create_supplier_contact_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact()

    service_mock.create.return_value = contact

    response = client.post(
        "/suppliers/1/contacts",
        json={
            "name": "João Silva",
            "email": "joao@fornecedor.com",
            "phone": "(13) 99999-1111",
            "position": "Garantia",
            "is_primary": True,
        },
    )

    assert response.status_code == 201
    assert response.json() == expected_contact_json()

    service_mock.create.assert_called_once_with(
        supplier_id=1,
        name="João Silva",
        email="joao@fornecedor.com",
        phone="(13) 99999-1111",
        position="Garantia",
        is_primary=True,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_list_supplier_contacts(
    client: TestClient,
    service_mock: Mock,
) -> None:
    primary_contact = create_contact()

    secondary_contact = create_contact(
        contact_id=11,
        name="Maria Souza",
        email="maria@fornecedor.com",
        phone=None,
        position="Comercial",
        is_primary=0,
        is_active=1,
    )

    service_mock.list_by_supplier.return_value = [
        primary_contact,
        secondary_contact,
    ]

    response = client.get(
        "/suppliers/1/contacts"
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_contact_json(),
        expected_contact_json(
            contact_id=11,
            name="Maria Souza",
            email="maria@fornecedor.com",
            phone=None,
            position="Comercial",
            is_primary=False,
            is_active=True,
        ),
    ]

    service_mock.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_get_supplier_contact_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    contact = create_contact()

    service_mock.get_required.return_value = contact

    response = client.get(
        "/suppliers/1/contacts/10"
    )

    assert response.status_code == 200
    assert response.json() == expected_contact_json()

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )


def test_should_update_only_informed_contact_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    service_mock.update.return_value = contact

    response = client.put(
        "/suppliers/1/contacts/10",
        json={
            "phone": "(13) 98888-2222",
            "position": "Pós-venda",
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    service_mock.update.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_send_none_to_clear_optional_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        email=None,
        phone=None,
        position=None,
    )

    service_mock.update.return_value = contact

    response = client.put(
        "/suppliers/1/contacts/10",
        json={
            "email": None,
            "phone": None,
            "position": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        email=None,
        phone=None,
        position=None,
    )

    service_mock.update.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
        email=None,
        phone=None,
        position=None,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_deactivate_supplier_contact(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        is_primary=0,
        is_active=0,
    )

    service_mock.deactivate.return_value = contact

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate"
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        is_primary=False,
        is_active=False,
    )

    service_mock.deactivate.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_activate_supplier_contact(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        is_primary=0,
        is_active=1,
    )

    service_mock.activate.return_value = contact

    response = client.patch(
        "/suppliers/1/contacts/10/activate"
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        is_primary=False,
        is_active=True,
    )

    service_mock.activate.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_supplier_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.list_by_supplier.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get(
        "/suppliers/999/contacts"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.list_by_supplier.assert_called_once_with(
        999
    )


def test_should_return_404_when_contact_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Contato não encontrado."
    )

    response = client.get(
        "/suppliers/1/contacts/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contato não encontrado.",
    }

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=999,
    )


def test_should_return_404_when_contact_belongs_to_another_supplier(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "O contato não pertence ao fornecedor informado."
    )

    response = client.get(
        "/suppliers/2/contacts/10"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": (
            "O contato não pertence ao fornecedor informado."
        ),
    }

    service_mock.get_required.assert_called_once_with(
        supplier_id=2,
        contact_id=10,
    )


def test_should_return_400_when_contact_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "O contato já está inativo."
    )

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O contato já está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_contact_is_already_active(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.activate.side_effect = ValueError(
        "O contato já está ativo."
    )

    response = client.patch(
        "/suppliers/1/contacts/10/activate"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O contato já está ativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_rollback_when_update_fails(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "Contato não encontrado."
    )

    response = client.put(
        "/suppliers/1/contacts/999",
        json={
            "phone": "(13) 99999-9999",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contato não encontrado.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_supplier_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.get(
        "/suppliers/0/contacts"
    )

    assert response.status_code == 422

    service_mock.list_by_supplier.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()


def test_should_return_422_for_invalid_contact_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.get(
        "/suppliers/1/contacts/0"
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()


def test_should_return_422_for_invalid_email(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/suppliers/1/contacts",
        json={
            "name": "João Silva",
            "email": "email-invalido",
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()


def test_should_reject_extra_request_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/suppliers/1/contacts",
        json={
            "name": "João Silva",
            "department": "Garantia",
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()