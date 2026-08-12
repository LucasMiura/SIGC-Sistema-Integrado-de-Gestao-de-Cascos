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
    ROLE_ADMIN,
)
from src.api.dependencies.audit import (
    get_audit_service,
)
from src.api.routes.audit_route import (
    router,
)
from src.database.connection import (
    get_session,
)
from src.services.audit_service import (
    AuditService,
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
    Cria um AuditService simulado.
    """

    return Mock(
        spec=AuditService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    """
    Cria aplicação isolada simulando
    um Administrador Master autenticado.
    """

    test_app = FastAPI()

    admin_user = SimpleNamespace(
        id=1,
        username="admin",
        role_id=1,
        is_active=1,
    )

    admin_role = SimpleNamespace(
        id=1,
        name=ROLE_ADMIN,
    )

    def override_get_session():
        yield session

    def override_get_audit_service():
        return service

    def override_get_current_user():
        return admin_user

    session.scalar.return_value = (
        admin_role
    )

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

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
    """
    Cria o cliente HTTP.
    """

    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_audit_log(
    *,
    audit_log_id: int = 1,
    user_id: int = 10,
    action: str = "CREATE",
    module: str = "PURCHASE",
    entity_type: str = "Purchase",
    entity_id: int = 20,
) -> SimpleNamespace:
    """
    Cria um registro de auditoria simulado.
    """

    return SimpleNamespace(
        id=audit_log_id,
        user_id=user_id,
        action=action,
        module=module,
        entity_type=entity_type,
        entity_id=entity_id,
        description="Compra cadastrada.",
        old_values=None,
        new_values=(
            '{"status":"RECEIVED"}'
        ),
        justification=None,
        created_at=(
            "2026-08-10T14:30:00"
        ),
    )


def test_should_get_audit_log(
    client: TestClient,
    service: Mock,
) -> None:
    audit_log = create_audit_log()

    service.get_by_id.return_value = (
        audit_log
    )

    response = client.get(
        "/audit-logs/1"
    )

    assert response.status_code == 200

    assert response.json()[
        "id"
    ] == 1

    assert response.json()[
        "action"
    ] == "CREATE"

    service.get_by_id.assert_called_once_with(
        1
    )


def test_should_return_404_when_audit_log_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_by_id.side_effect = (
        ValueError(
            "Registro de auditoria não encontrado."
        )
    )

    response = client.get(
        "/audit-logs/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": (
            "Registro de auditoria não encontrado."
        ),
    }


@pytest.mark.parametrize(
    "audit_log_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_audit_log_id_is_invalid(
    client: TestClient,
    service: Mock,
    audit_log_id: int,
) -> None:
    response = client.get(
        f"/audit-logs/{audit_log_id}"
    )

    assert response.status_code == 422

    service.get_by_id.assert_not_called()


def test_should_list_audit_logs_by_user(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_by_user.return_value = [
        create_audit_log(),
        create_audit_log(
            audit_log_id=2,
        ),
    ]

    response = client.get(
        "/audit-logs/by-user/10"
    )

    assert response.status_code == 200

    assert len(
        response.json()
    ) == 2

    service.list_by_user.assert_called_once_with(
        10
    )


def test_should_list_audit_logs_by_module(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_by_module.return_value = [
        create_audit_log()
    ]

    response = client.get(
        "/audit-logs/by-module/PURCHASE"
    )

    assert response.status_code == 200

    service.list_by_module.assert_called_once_with(
        "PURCHASE"
    )


def test_should_list_audit_logs_by_entity(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_by_entity.return_value = [
        create_audit_log()
    ]

    response = client.get(
        "/audit-logs/by-entity/Purchase/20"
    )

    assert response.status_code == 200

    service.list_by_entity.assert_called_once_with(
        entity_type="Purchase",
        entity_id=20,
    )


def test_should_return_empty_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_by_user.return_value = []

    response = client.get(
        "/audit-logs/by-user/10"
    )

    assert response.status_code == 200
    assert response.json() == []


def test_should_return_401_without_authentication(
    session: Mock,
    service: Mock,
) -> None:
    test_app = FastAPI()

    def override_get_session():
        yield session

    def override_get_audit_service():
        return service

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_audit_service
    ] = override_get_audit_service

    test_app.include_router(
        router
    )

    test_client = TestClient(
        test_app,
        raise_server_exceptions=False,
    )

    response = test_client.get(
        "/audit-logs/1"
    )

    assert response.status_code == 401

    service.get_by_id.assert_not_called()


def test_should_return_403_for_non_admin_user(
    session: Mock,
    service: Mock,
) -> None:
    test_app = FastAPI()

    buyer_user = SimpleNamespace(
        id=2,
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

    def override_get_audit_service():
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
        get_audit_service
    ] = override_get_audit_service

    test_app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    test_app.include_router(
        router
    )

    test_client = TestClient(
        test_app,
        raise_server_exceptions=False,
    )

    response = test_client.get(
        "/audit-logs/1"
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O usuário autenticado não possui "
            "permissão para realizar esta "
            "operação."
        ),
    }

    service.get_by_id.assert_not_called()