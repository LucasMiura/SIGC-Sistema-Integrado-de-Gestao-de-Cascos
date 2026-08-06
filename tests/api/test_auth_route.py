from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.auth_route import (
    get_auth_service,
    router,
)
from src.database.connection import get_session
from src.services.auth_service import (
    AuthenticationResult,
    AuthService,
)


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=AuthService,
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

    def override_get_auth_service():
        return service

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_auth_service
    ] = override_get_auth_service

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
    full_name: str = "Lucas Miura",
    username: str = "lucas.miura",
    email: str = "lucas@example.com",
    role_id: int = 1,
    is_active: int = 1,
    last_login_at: str | None = (
        "2026-08-06T10:30:00"
    ),
    created_at: str = (
        "2026-08-06T09:00:00"
    ),
    updated_at: str = (
        "2026-08-06T10:30:00"
    ),
) -> SimpleNamespace:
    return SimpleNamespace(
        id=user_id,
        full_name=full_name,
        username=username,
        email=email,
        password_hash=(
            "protected-password-hash"
        ),
        role_id=role_id,
        is_active=is_active,
        last_login_at=last_login_at,
        created_at=created_at,
        updated_at=updated_at,
    )


def expected_user_response() -> dict:
    return {
        "id": 10,
        "full_name": "Lucas Miura",
        "username": "lucas.miura",
        "email": "lucas@example.com",
        "role_id": 1,
        "is_active": 1,
        "last_login_at": (
            "2026-08-06T10:30:00"
        ),
        "created_at": (
            "2026-08-06T09:00:00"
        ),
        "updated_at": (
            "2026-08-06T10:30:00"
        ),
    }


def test_should_login_successfully(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    user = create_user()

    result = AuthenticationResult(
        access_token="jwt-access-token",
        token_type="bearer",
        user=user,
    )

    service.authenticate.return_value = (
        result
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas.miura",
            "password": "SenhaSegura123",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "access_token": "jwt-access-token",
        "token_type": "bearer",
        "user": expected_user_response(),
    }

    response_body = response.json()

    assert "password" not in response_body

    assert (
        "password_hash"
        not in response_body
    )

    assert (
        "password_hash"
        not in response_body["user"]
    )

    service.authenticate.assert_called_once_with(
        login="lucas.miura",
        password="SenhaSegura123",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )

    session.rollback.assert_not_called()


def test_should_login_with_email(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    user = create_user()

    service.authenticate.return_value = (
        AuthenticationResult(
            access_token=(
                "jwt-email-access-token"
            ),
            token_type="bearer",
            user=user,
        )
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas@example.com",
            "password": "SenhaSegura123",
        },
    )

    assert response.status_code == 200

    assert response.json()[
        "access_token"
    ] == "jwt-email-access-token"

    service.authenticate.assert_called_once_with(
        login="lucas@example.com",
        password="SenhaSegura123",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {
            "password": "SenhaSegura123",
        },
        {
            "login": "lucas.miura",
        },
        {
            "login": "",
            "password": "SenhaSegura123",
        },
        {
            "login": "   ",
            "password": "SenhaSegura123",
        },
        {
            "login": "lucas.miura",
            "password": "",
        },
        {
            "login": "lucas.miura",
            "password": "SenhaSegura123",
            "unexpected_field": "value",
        },
    ],
)
def test_should_return_422_when_login_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
) -> None:
    response = client.post(
        "/auth/login",
        json=payload,
    )

    assert response.status_code == 422

    service.authenticate.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_401_when_credentials_are_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "Username, e-mail ou senha inválidos."
    )

    service.authenticate.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas.miura",
            "password": "SenhaErrada",
        },
    )

    assert response.status_code == 401

    assert response.json() == {
        "detail": message,
    }

    assert response.headers[
        "www-authenticate"
    ] == "Bearer"

    service.authenticate.assert_called_once_with(
        login="lucas.miura",
        password="SenhaErrada",
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_403_when_user_is_inactive(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = "O usuário está inativo."

    service.authenticate.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas.miura",
            "password": "SenhaSegura123",
        },
    )

    assert response.status_code == 403

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_for_other_business_error(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    message = (
        "Erro de autenticação."
    )

    service.authenticate.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas.miura",
            "password": "SenhaSegura123",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.authenticate.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas.miura",
            "password": "SenhaSegura123",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_rollback_when_response_validation_fails(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    invalid_user = SimpleNamespace(
        id=10,
        full_name="Lucas Miura",
        username="lucas.miura",
        email="lucas@example.com",
        role_id=1,
        is_active=1,
        last_login_at=None,
        created_at=None,
        updated_at=None,
    )

    service.authenticate.return_value = (
        AuthenticationResult(
            access_token="jwt-access-token",
            token_type="bearer",
            user=invalid_user,
        )
    )

    response = client.post(
        "/auth/login",
        json={
            "login": "lucas.miura",
            "password": "SenhaSegura123",
        },
    )

    assert response.status_code == 500

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        invalid_user
    )

    session.rollback.assert_called_once_with()