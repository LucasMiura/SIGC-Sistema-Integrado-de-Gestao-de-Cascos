from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.dependencies.audit import (
    get_audit_service,
)

from src.api.routes.supplier_route import (
    get_supplier_service,
)
from src.services.audit_service import (
    AuditService,
)
from src.database.connection import get_session
from src.main import app
from src.services.supplier_service import SupplierService
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_BUYER,
)


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock do serviço de fornecedores.
    """

    return Mock(spec=SupplierService)


@pytest.fixture
def session_mock() -> Mock:
    """
    Cria um mock da sessão SQLAlchemy.
    """

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
    Cria o cliente HTTP simulando um Comprador
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

    def override_supplier_service() -> Mock:
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
        get_supplier_service
    ] = override_supplier_service

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


def create_supplier(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    document: str | None = "12.345.678/0001-90",
    address: str | None = "Registro/SP",
    notes: str | None = "Fornecedor de teste",
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados pelo schema.
    """

    return SimpleNamespace(
        id=supplier_id,
        name=name,
        document=document,
        address=address,
        notes=notes,
        is_active=is_active,
        created_at="2026-07-28T10:00:00",
        updated_at="2026-07-28T10:00:00",
    )


def expected_supplier_json(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    document: str | None = "12.345.678/0001-90",
    address: str | None = "Registro/SP",
    notes: str | None = "Fornecedor de teste",
    is_active: int = 1,
) -> dict[str, object]:
    """
    Retorna o JSON esperado nas respostas.
    """

    return {
        "id": supplier_id,
        "name": name,
        "document": document,
        "address": address,
        "notes": notes,
        "is_active": is_active,
        "created_at": "2026-07-28T10:00:00",
        "updated_at": "2026-07-28T10:00:00",
    }


def test_should_create_supplier_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    supplier = create_supplier()

    service_mock.create.return_value = supplier

    response = client.post(
        "/suppliers",
        json={
            "name": "Fornecedor Teste",
            "document": "12.345.678/0001-90",
            "address": "Registro/SP",
            "notes": "Fornecedor de teste",
        },
    )

    assert response.status_code == 201
    assert response.json() == expected_supplier_json()

    service_mock.create.assert_called_once_with(
        name="Fornecedor Teste",
        document="12.345.678/0001-90",
        address="Registro/SP",
        notes="Fornecedor de teste",
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="CREATE",
        module="SUPPLIER",
        entity_type="Supplier",
        entity_id=1,
        description="Fornecedor cadastrado.",
        new_values={
            "name": "Fornecedor Teste",
            "document": "12.345.678/0001-90",
            "address": "Registro/SP",
            "notes": "Fornecedor de teste",
            "is_active": 1,
        },
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_list_suppliers(
    client: TestClient,
    service_mock: Mock,
) -> None:
    first_supplier = create_supplier()

    second_supplier = create_supplier(
        supplier_id=2,
        name="Segundo Fornecedor",
        document=None,
        address=None,
        notes=None,
        is_active=0,
    )

    service_mock.list_all.return_value = [
        first_supplier,
        second_supplier,
    ]

    response = client.get("/suppliers")

    assert response.status_code == 200

    assert response.json() == [
        expected_supplier_json(),
        expected_supplier_json(
            supplier_id=2,
            name="Segundo Fornecedor",
            document=None,
            address=None,
            notes=None,
            is_active=0,
        ),
    ]

    service_mock.list_all.assert_called_once_with()


def test_should_get_supplier_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    supplier = create_supplier()

    service_mock.get_required.return_value = supplier

    response = client.get("/suppliers/1")

    assert response.status_code == 200
    assert response.json() == expected_supplier_json()

    service_mock.get_required.assert_called_once_with(1)


def test_should_return_404_when_supplier_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get("/suppliers/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.get_required.assert_called_once_with(999)


def test_should_update_only_informed_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    original_supplier = create_supplier()

    supplier = create_supplier(
        address="Novo endereço",
        notes=None,
    )

    service_mock.get_required.return_value = (
        original_supplier
    )

    service_mock.update.return_value = supplier

    response = client.put(
        "/suppliers/1",
        json={
            "address": "Novo endereço",
            "notes": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        address="Novo endereço",
        notes=None,
    )

    service_mock.get_required.assert_called_once_with(
        1
    )

    service_mock.update.assert_called_once_with(
        1,
        address="Novo endereço",
        notes=None,
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="UPDATE",
        module="SUPPLIER",
        entity_type="Supplier",
        entity_id=1,
        description="Fornecedor atualizado.",
        old_values={
            "address": "Registro/SP",
            "notes": "Fornecedor de teste",
        },
        new_values={
            "address": "Novo endereço",
            "notes": None,
        },
    )

    session_mock.commit.assert_called_once_with()

    session_mock.refresh.assert_called_once_with(
        supplier
    )

    session_mock.rollback.assert_not_called()


def test_should_rollback_when_audit_fails_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    original_supplier = create_supplier()

    updated_supplier = create_supplier(
        address="Novo endereço",
    )

    service_mock.get_required.return_value = (
        original_supplier
    )

    service_mock.update.return_value = (
        updated_supplier
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.put(
        "/suppliers/1",
        json={
            "address": "Novo endereço",
        },
    )

    assert response.status_code == 500

    service_mock.get_required.assert_called_once_with(
        1
    )

    service_mock.update.assert_called_once_with(
        1,
        address="Novo endereço",
    )

    audit_service.register.assert_called_once()

    session_mock.rollback.assert_called_once_with()

    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_409_for_duplicate_document(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "Já existe um fornecedor com este documento."
    )

    response = client.post(
        "/suppliers",
        json={
            "name": "Fornecedor Duplicado",
            "document": "12.345.678/0001-90",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe um fornecedor com este documento."
        ),
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_deactivate_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    supplier = create_supplier(
        is_active=0,
    )

    service_mock.deactivate.return_value = (
        supplier
    )

    response = client.patch(
        "/suppliers/1/deactivate",
        json={
            "justification": (
                "Fornecedor não será mais utilizado."
            ),
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        is_active=0,
    )

    service_mock.deactivate.assert_called_once_with(
        1
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="DEACTIVATE",
        module="SUPPLIER",
        entity_type="Supplier",
        entity_id=1,
        description="Fornecedor desativado.",
        old_values={
            "is_active": 1,
        },
        new_values={
            "is_active": 0,
        },
        justification=(
            "Fornecedor não será mais utilizado."
        ),
    )

    session_mock.commit.assert_called_once_with()

    session_mock.refresh.assert_called_once_with(
        supplier
    )

    session_mock.rollback.assert_not_called()


def test_should_activate_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    supplier = create_supplier(
        is_active=1,
    )

    service_mock.activate.return_value = supplier

    response = client.patch(
        "/suppliers/1/activate",
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        is_active=1,
    )

    service_mock.activate.assert_called_once_with(1)

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="ACTIVATE",
        module="SUPPLIER",
        entity_type="Supplier",
        entity_id=1,
        description="Fornecedor ativado.",
        old_values={
            "is_active": 0,
        },
        new_values={
            "is_active": 1,
        },
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_return_400_when_supplier_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "O fornecedor já está inativo."
    )

    response = client.patch(
        "/suppliers/1/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor já está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()


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
        "/suppliers/1/deactivate",
        json=payload,
    )

    assert response.status_code == 422

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
        "/suppliers/1/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

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
    supplier = create_supplier(
        is_active=0,
    )

    service_mock.deactivate.return_value = (
        supplier
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.patch(
        "/suppliers/1/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 500

    service_mock.deactivate.assert_called_once_with(
        1
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
        "/suppliers/0",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()

def test_should_return_401_when_supplier_route_has_no_authentication(
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    def override_supplier_service() -> Mock:
        return service_mock

    def override_session():
        yield session_mock

    app.dependency_overrides[
        get_supplier_service
    ] = override_supplier_service

    app.dependency_overrides[
        get_session
    ] = override_session

    try:
        with TestClient(app) as test_client:
            response = test_client.get(
                "/suppliers"
            )

        assert response.status_code == 401

        service_mock.list_all.assert_not_called()

    finally:
        app.dependency_overrides.clear()


def test_should_return_403_when_seller_accesses_suppliers(
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

    def override_supplier_service() -> Mock:
        return service_mock

    def override_session():
        yield session_mock

    def override_get_current_user():
        return seller_user

    session_mock.scalar.return_value = (
        seller_role
    )

    app.dependency_overrides[
        get_supplier_service
    ] = override_supplier_service

    app.dependency_overrides[
        get_session
    ] = override_session

    app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    try:
        with TestClient(app) as test_client:
            response = test_client.get(
                "/suppliers"
            )

        assert response.status_code == 403

        assert response.json() == {
            "detail": (
                "O usuário autenticado não possui "
                "permissão para realizar esta "
                "operação."
            ),
        }

        service_mock.list_all.assert_not_called()

    finally:
        app.dependency_overrides.clear()