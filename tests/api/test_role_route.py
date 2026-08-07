from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.role_route import (
    get_role_service,
    router,
)
from src.database.connection import get_session
from src.services.role_service import (
    RoleService,
)
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_ADMIN,
)


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=RoleService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
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

    def override_get_role_service():
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
        get_role_service
    ] = override_get_role_service

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
    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_role(
    role_id: int = 1,
    name: str | None = "Administrador Master",
    description: str | None = (
        "Perfil administrativo completo."
    ),
    created_at: str = "2026-08-06T09:00:00",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=role_id,
        name=name,
        description=description,
        created_at=created_at,
    )


def expected_role_response(
    role_id: int = 1,
    name: str | None = "Administrador Master",
    description: str | None = (
        "Perfil administrativo completo."
    ),
) -> dict:
    return {
        "id": role_id,
        "name": name,
        "description": description,
        "created_at": "2026-08-06T09:00:00",
    }


def test_should_create_role(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    role = create_role()

    service.create.return_value = role

    response = client.post(
        "/roles",
        json={
            "name": "Administrador Master",
            "description": (
                "Perfil administrativo completo."
            ),
        },
    )

    assert response.status_code == 201

    assert response.json() == (
        expected_role_response()
    )

    service.create.assert_called_once_with(
        name="Administrador Master",
        description=(
            "Perfil administrativo completo."
        ),
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        role
    )

    session.rollback.assert_not_called()


def test_should_create_role_without_description(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    role = create_role(
        name="Comprador",
        description=None,
    )

    service.create.return_value = role

    response = client.post(
        "/roles",
        json={
            "name": "Comprador",
        },
    )

    assert response.status_code == 201

    assert response.json() == (
        expected_role_response(
            name="Comprador",
            description=None,
        )
    )

    service.create.assert_called_once_with(
        name="Comprador",
        description=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        role
    )


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {
            "description": "Sem nome.",
        },
        {
            "name": "",
        },
        {
            "name": "   ",
        },
    ],
)
def test_should_return_422_when_create_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
) -> None:
    response = client.post(
        "/roles",
        json=payload,
    )

    assert response.status_code == 422

    service.create.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/roles",
        json={
            "name": "Vendedor",
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service.create.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_409_when_role_name_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "Já existe um perfil com este nome."
    )

    service.create.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/roles",
        json={
            "name": "Administrador Master",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_business_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "O nome do perfil é obrigatório."
    )

    service.create.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/roles",
        json={
            "name": "Perfil",
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
    service.create.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/roles",
        json={
            "name": "Administrador Master",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_roles(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_all.return_value = [
        create_role(),
        create_role(
            role_id=2,
            name="Comprador",
            description=(
                "Perfil responsável por compras."
            ),
        ),
        create_role(
            role_id=3,
            name="Vendedor",
            description=None,
        ),
    ]

    response = client.get(
        "/roles"
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_role_response(),
        expected_role_response(
            role_id=2,
            name="Comprador",
            description=(
                "Perfil responsável por compras."
            ),
        ),
        expected_role_response(
            role_id=3,
            name="Vendedor",
            description=None,
        ),
    ]

    service.list_all.assert_called_once_with()


def test_should_return_empty_role_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_all.return_value = []

    response = client.get(
        "/roles"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_all.assert_called_once_with()


def test_should_get_role(
    client: TestClient,
    service: Mock,
) -> None:
    role = create_role()

    service.get_by_id.return_value = role

    response = client.get(
        "/roles/1"
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_role_response()
    )

    service.get_by_id.assert_called_once_with(
        1
    )


def test_should_return_404_when_role_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_by_id.return_value = None

    response = client.get(
        "/roles/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": (
            "Perfil de acesso não encontrado."
        ),
    }

    service.get_by_id.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "role_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_role_id_is_invalid(
    client: TestClient,
    service: Mock,
    role_id: int,
) -> None:
    response = client.get(
        f"/roles/{role_id}"
    )

    assert response.status_code == 422

    service.get_by_id.assert_not_called()

def test_should_return_401_without_authentication(
    service: Mock,
) -> None:
    test_app = FastAPI()

    test_app.include_router(
        router
    )

    client = TestClient(
        test_app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/roles"
    )

    assert response.status_code == 401

    service.list_all.assert_not_called()


def test_should_return_403_for_non_admin_user(
    session: Mock,
    service: Mock,
) -> None:
    from src.api.dependencies.auth import (
        get_current_user,
    )

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

    def override_get_role_service():
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
        get_role_service
    ] = override_get_role_service

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
        "/roles"
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O usuário autenticado não possui "
            "permissão para realizar esta "
            "operação."
        ),
    }

    service.list_all.assert_not_called()