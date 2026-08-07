from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.dependencies.auth import (
    CurrentUserDependency,
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_ADMIN,
    ROLE_BUYER,
    ROLE_SELLER,
    require_roles,
)
from src.database.connection import get_session
from src.models.user import User


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def current_user() -> SimpleNamespace:
    return SimpleNamespace(
        id=10,
        username="lucas.miura",
        role_id=1,
        is_active=1,
    )


def create_role(
    role_id: int = 1,
    name: str | None = ROLE_ADMIN,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=role_id,
        name=name,
    )


def create_app(
    session: Mock,
    current_user: SimpleNamespace,
    *allowed_roles: str,
) -> FastAPI:
    from typing import Annotated

    from fastapi import Depends

    test_app = FastAPI()

    def override_get_session():
        yield session

    def override_get_current_user():
        return current_user

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    role_dependency = require_roles(
        *allowed_roles
    )

    @test_app.get(
        "/protected"
    )
    def protected_route(
        authorized_user: Annotated[
            User,
            Depends(role_dependency),
        ],
    ) -> dict:
        return {
            "user_id": authorized_user.id,
            "username": authorized_user.username,
            "role_id": authorized_user.role_id,
        }

    return test_app


def test_should_allow_administrator(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    role = create_role(
        name=ROLE_ADMIN,
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        role
    )

    repository_class_mock = Mock(
        return_value=repository_mock,
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        repository_class_mock,
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 200

    assert response.json() == {
        "user_id": 10,
        "username": "lucas.miura",
        "role_id": 1,
    }

    repository_class_mock.assert_called_once_with(
        session
    )

    repository_mock.get_by_id.assert_called_once_with(
        1
    )


def test_should_allow_buyer(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    role = create_role(
        role_id=2,
        name=ROLE_BUYER,
    )

    current_user.role_id = 2

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        role
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        Mock(
            return_value=repository_mock,
        ),
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
        ROLE_BUYER,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 200

    assert response.json()[
        "role_id"
    ] == 2


def test_should_allow_seller(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    role = create_role(
        role_id=3,
        name=ROLE_SELLER,
    )

    current_user.role_id = 3

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        role
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        Mock(
            return_value=repository_mock,
        ),
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
        ROLE_SELLER,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 200

    assert response.json()[
        "role_id"
    ] == 3


def test_should_return_403_when_role_is_not_allowed(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    current_user.role_id = 3

    role = create_role(
        role_id=3,
        name=ROLE_SELLER,
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        role
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        Mock(
            return_value=repository_mock,
        ),
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
        ROLE_BUYER,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O usuário autenticado não possui "
            "permissão para realizar esta "
            "operação."
        ),
    }


def test_should_return_403_when_role_does_not_exist(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        None
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        Mock(
            return_value=repository_mock,
        ),
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O perfil do usuário autenticado "
            "não foi encontrado."
        ),
    }


@pytest.mark.parametrize(
    "role_name",
    [
        None,
        "",
        "   ",
    ],
)
def test_should_return_403_when_role_name_is_invalid(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
    role_name: str | None,
) -> None:
    role = create_role(
        name=role_name,
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        role
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        Mock(
            return_value=repository_mock,
        ),
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O perfil do usuário autenticado "
            "é inválido."
        ),
    }


def test_should_preserve_authenticated_user(
    session: Mock,
    current_user: SimpleNamespace,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    role = create_role(
        name=ROLE_ADMIN,
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        role
    )

    monkeypatch.setattr(
        (
            "src.api.dependencies.authorization."
            "RoleRepository"
        ),
        Mock(
            return_value=repository_mock,
        ),
    )

    app = create_app(
        session,
        current_user,
        ROLE_ADMIN,
    )

    client = TestClient(
        app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/protected"
    )

    assert response.status_code == 200

    assert response.json() == {
        "user_id": current_user.id,
        "username": current_user.username,
        "role_id": current_user.role_id,
    }


def test_should_reject_require_roles_without_roles() -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Pelo menos um perfil de acesso "
            "deve ser informado."
        ),
    ):
        require_roles()


def test_should_ignore_blank_allowed_roles() -> None:
    dependency = require_roles(
        "   ",
        ROLE_ADMIN,
        "",
    )

    assert callable(
        dependency
    )


def test_should_reject_only_blank_allowed_roles() -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Pelo menos um perfil de acesso "
            "deve ser informado."
        ),
    ):
        require_roles(
            "",
            "   ",
        )