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
from src.database.connection import get_session


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def app(
    session: Mock,
) -> FastAPI:
    test_app = FastAPI()

    def override_get_session():
        yield session

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    @test_app.get(
        "/protected"
    )
    def protected_route(
        current_user: CurrentUserDependency,
    ) -> dict:
        return {
            "user_id": current_user.id,
            "username": current_user.username,
        }

    return test_app


@pytest.fixture
def client(
    app: FastAPI,
) -> TestClient:
    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_user(
    user_id: int = 10,
    username: str = "lucas.miura",
    is_active: int = 1,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=user_id,
        username=username,
        is_active=is_active,
    )


def test_should_authenticate_current_user(
    client: TestClient,
    session: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    decode_mock = Mock(
        return_value={
            "user_id": 10,
            "role_id": 1,
            "type": "access",
        },
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        user
    )

    repository_class_mock = Mock(
        return_value=repository_mock,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.decode_access_token",
        decode_mock,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.UserRepository",
        repository_class_mock,
    )

    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Bearer valid-token"
            ),
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "user_id": 10,
        "username": "lucas.miura",
    }

    decode_mock.assert_called_once_with(
        "valid-token"
    )

    repository_class_mock.assert_called_once_with(
        session
    )

    repository_mock.get_by_id.assert_called_once_with(
        10
    )


def test_should_return_401_when_token_is_missing(
    client: TestClient,
) -> None:
    response = client.get(
        "/protected"
    )

    assert response.status_code == 401

    assert response.json() == {
        "detail": (
            "Token de acesso não informado."
        ),
    }

    assert response.headers[
        "www-authenticate"
    ] == "Bearer"


def test_should_return_401_when_authorization_scheme_is_invalid(
    client: TestClient,
) -> None:
    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Basic abc123"
            ),
        },
    )

    assert response.status_code == 401

    assert response.json() == {
        "detail": (
            "Token de acesso não informado."
        ),
    }

    assert response.headers[
        "www-authenticate"
    ] == "Bearer"


def test_should_return_401_when_token_is_invalid(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from src.security.token import (
        InvalidAccessTokenError,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.decode_access_token",
        Mock(
            side_effect=(
                InvalidAccessTokenError(
                    "Token de acesso inválido."
                )
            ),
        ),
    )

    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Bearer invalid-token"
            ),
        },
    )

    assert response.status_code == 401

    assert response.json() == {
        "detail": (
            "Token de acesso inválido."
        ),
    }

    assert response.headers[
        "www-authenticate"
    ] == "Bearer"


def test_should_return_401_when_token_is_expired(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from src.security.token import (
        ExpiredTokenError,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.decode_access_token",
        Mock(
            side_effect=(
                ExpiredTokenError(
                    "Token de acesso expirado."
                )
            ),
        ),
    )

    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Bearer expired-token"
            ),
        },
    )

    assert response.status_code == 401

    assert response.json() == {
        "detail": (
            "Token de acesso expirado."
        ),
    }

    assert response.headers[
        "www-authenticate"
    ] == "Bearer"


def test_should_return_401_when_authenticated_user_does_not_exist(
    client: TestClient,
    session: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    decode_mock = Mock(
        return_value={
            "user_id": 999,
            "role_id": 1,
            "type": "access",
        },
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        None
    )

    repository_class_mock = Mock(
        return_value=repository_mock,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.decode_access_token",
        decode_mock,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.UserRepository",
        repository_class_mock,
    )

    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Bearer valid-token"
            ),
        },
    )

    assert response.status_code == 401

    assert response.json() == {
        "detail": (
            "Usuário autenticado não encontrado."
        ),
    }

    repository_class_mock.assert_called_once_with(
        session
    )

    repository_mock.get_by_id.assert_called_once_with(
        999
    )

    assert response.headers[
        "www-authenticate"
    ] == "Bearer"


def test_should_return_403_when_authenticated_user_is_inactive(
    client: TestClient,
    session: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user(
        is_active=0,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.decode_access_token",
        Mock(
            return_value={
                "user_id": 10,
                "role_id": 1,
                "type": "access",
            },
        ),
    )

    repository_mock = Mock()

    repository_mock.get_by_id.return_value = (
        user
    )

    repository_class_mock = Mock(
        return_value=repository_mock,
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.UserRepository",
        repository_class_mock,
    )

    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Bearer valid-token"
            ),
        },
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": (
            "O usuário autenticado está inativo."
        ),
    }

    repository_class_mock.assert_called_once_with(
        session
    )

    repository_mock.get_by_id.assert_called_once_with(
        10
    )


def test_should_return_500_when_repository_fails(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "src.api.dependencies.auth.decode_access_token",
        Mock(
            return_value={
                "user_id": 10,
                "role_id": 1,
                "type": "access",
            },
        ),
    )

    repository_mock = Mock()

    repository_mock.get_by_id.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    monkeypatch.setattr(
        "src.api.dependencies.auth.UserRepository",
        Mock(
            return_value=repository_mock,
        ),
    )

    response = client.get(
        "/protected",
        headers={
            "Authorization": (
                "Bearer valid-token"
            ),
        },
    )

    assert response.status_code == 500