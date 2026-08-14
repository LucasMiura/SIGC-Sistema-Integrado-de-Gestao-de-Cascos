from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from src.api.dependencies.audit import (
    get_audit_service,
)

from src.api.routes.supplier_contact_route import (
    get_supplier_contact_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.supplier_contact_service import (
    SupplierContactService,
)
from src.services.audit_service import (
    AuditService,
)
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_BUYER,
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
def audit_service() -> Mock:
    """
    Cria um mock do serviço de auditoria.
    """

    return Mock(
        spec=AuditService,
    )

@pytest.fixture
def client(
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente simulando um Comprador
    autenticado.
    """

    buyer_user = SimpleNamespace(
        id=2,
        username="comprador",
        role_id=2,
        is_active=1,
    )

    buyer_role = SimpleNamespace(
        id=2,
        name=ROLE_BUYER,
    )

    def override_supplier_contact_service() -> Mock:
        return service_mock

    def override_audit_service() -> Mock:
        return audit_service

    def override_session() -> Generator[
        Mock,
        None,
        None,
    ]:
        yield session_mock

    def override_get_current_user():
        return buyer_user

    session_mock.scalar.return_value = (
        buyer_role
    )

    app.dependency_overrides[
        get_supplier_contact_service
    ] = override_supplier_contact_service

    app.dependency_overrides[
        get_audit_service
    ] = override_audit_service

    app.dependency_overrides[
        get_session
    ] = override_session

    app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    with TestClient(
        app,
        raise_server_exceptions=False,
    ) as test_client:
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
    audit_service: Mock,
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

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="CREATE",
        module="SUPPLIER_CONTACT",
        entity_type="SupplierContact",
        entity_id=10,
        description=(
            "Contato de fornecedor cadastrado."
        ),
        new_values={
            "supplier_id": 1,
            "name": "João Silva",
            "email": "joao@fornecedor.com",
            "phone": "(13) 99999-1111",
            "position": "Garantia",
            "is_primary": 1,
            "is_active": 1,
        },
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
    audit_service: Mock,
) -> None:
    original_contact = create_contact()

    contact = create_contact(
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    service_mock.get_required.return_value = (
        original_contact
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

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    service_mock.update.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="UPDATE",
        module="SUPPLIER_CONTACT",
        entity_type="SupplierContact",
        entity_id=10,
        description=(
            "Contato de fornecedor atualizado."
        ),
        old_values={
            "phone": "(13) 99999-1111",
            "position": "Garantia",
        },
        new_values={
            "phone": "(13) 98888-2222",
            "position": "Pós-venda",
        },
    )

    session_mock.commit.assert_called_once_with()

    session_mock.refresh.assert_called_once_with(
        contact
    )

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
    audit_service: Mock,
) -> None:
    existing_contact = create_contact(
        is_primary=1,
        is_active=1,
    )

    contact = create_contact(
        is_primary=0,
        is_active=0,
    )

    service_mock.get_required.return_value = (
        existing_contact
    )

    service_mock.deactivate.return_value = contact

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate",
        json={
            "justification": (
                "Contato não trabalha mais "
                "com o fornecedor."
            ),
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        is_primary=False,
        is_active=False,
    )

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    service_mock.deactivate.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="DEACTIVATE",
        module="SUPPLIER_CONTACT",
        entity_type="SupplierContact",
        entity_id=10,
        description=(
            "Contato de fornecedor desativado."
        ),
        old_values={
            "is_active": 1,
            "is_primary": 1,
        },
        new_values={
            "is_active": 0,
            "is_primary": 0,
        },
        justification=(
            "Contato não trabalha mais "
            "com o fornecedor."
        ),
    )

    session_mock.commit.assert_called_once_with()

    session_mock.refresh.assert_called_once_with(
        contact
    )

    session_mock.rollback.assert_not_called()


def test_should_activate_supplier_contact(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
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

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="ACTIVATE",
        module="SUPPLIER_CONTACT",
        entity_type="SupplierContact",
        entity_id=10,
        description=(
            "Contato de fornecedor ativado."
        ),
        old_values={
            "is_active": 0,
        },
        new_values={
            "is_active": 1,
        },
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
    service_mock.get_required.return_value = (
        create_contact(
            is_primary=0,
            is_active=0,
        )
    )
    service_mock.deactivate.side_effect = ValueError(
        "O contato já está inativo."
    )

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O contato já está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


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
def test_should_return_422_when_deactivate_justification_is_invalid(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    payload: dict[str, object],
) -> None:
    response = client.patch(
        "/suppliers/1/contacts/10/deactivate",
        json=payload,
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    service_mock.deactivate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_deactivate_has_extra_field(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.patch(
        "/suppliers/1/contacts/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    service_mock.deactivate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_rollback_when_audit_fails_on_deactivate(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    existing_contact = create_contact(
        is_primary=1,
        is_active=1,
    )

    contact = create_contact(
        is_primary=0,
        is_active=0,
    )

    service_mock.get_required.return_value = (
        existing_contact
    )

    service_mock.deactivate.return_value = contact

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 500

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    service_mock.deactivate.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    audit_service.register.assert_called_once()

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

def test_should_rollback_when_audit_fails_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    original_contact = create_contact()

    updated_contact = create_contact(
        phone="(13) 98888-2222",
    )

    service_mock.get_required.return_value = (
        original_contact
    )

    service_mock.update.return_value = (
        updated_contact
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.put(
        "/suppliers/1/contacts/10",
        json={
            "phone": "(13) 98888-2222",
        },
    )

    assert response.status_code == 500

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    service_mock.update.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
        phone="(13) 98888-2222",
    )

    audit_service.register.assert_called_once()

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

def test_should_return_401_without_authentication(
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    def override_service() -> Mock:
        return service_mock

    def override_session():
        yield session_mock

    app.dependency_overrides[
        get_supplier_contact_service
    ] = override_service

    app.dependency_overrides[
        get_session
    ] = override_session

    try:
        with TestClient(app) as test_client:
            response = test_client.get(
                "/suppliers/1/contacts"
            )

        assert response.status_code == 401

        service_mock.list_by_supplier.assert_not_called()

    finally:
        app.dependency_overrides.clear()


def test_should_return_403_when_seller_accesses_supplier_contacts(
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    seller_user = SimpleNamespace(
        id=3,
        username="vendedor",
        role_id=3,
        is_active=1,
    )

    seller_role = SimpleNamespace(
        id=3,
        name="Vendedor",
    )

    def override_service() -> Mock:
        return service_mock

    def override_session():
        yield session_mock

    def override_get_current_user():
        return seller_user

    session_mock.scalar.return_value = (
        seller_role
    )

    app.dependency_overrides[
        get_supplier_contact_service
    ] = override_service

    app.dependency_overrides[
        get_session
    ] = override_session

    app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    try:
        with TestClient(app) as test_client:
            response = test_client.get(
                "/suppliers/1/contacts"
            )

        assert response.status_code == 403

        assert response.json() == {
            "detail": (
                "O usuário autenticado não possui "
                "permissão para realizar esta "
                "operação."
            ),
        }

        service_mock.list_by_supplier.assert_not_called()

    finally:
        app.dependency_overrides.clear()