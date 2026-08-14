from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.user_route import (
    get_user_service,
    router,
)
from src.database.connection import get_session
from src.services.user_service import (
    UserService,
)
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_ADMIN,
)
from src.api.dependencies.audit import (
    get_audit_service,
)
from src.services.audit_service import (
    AuditService,
)


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=UserService,
    )

@pytest.fixture
def audit_service() -> Mock:
    return Mock(
        spec=AuditService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> FastAPI:
    test_app = FastAPI()

    admin_user = SimpleNamespace(
        id=10,
        full_name="Lucas Miura",
        username="lucas.miura",
        email="lucas@example.com",
        password_hash=(
            "protected-password-hash"
        ),
        role_id=1,
        is_active=1,
        last_login_at=None,
        created_at=(
            "2026-08-06T09:00:00"
        ),
        updated_at=(
            "2026-08-06T09:00:00"
        ),
    )

    admin_role = SimpleNamespace(
        id=1,
        name=ROLE_ADMIN,
    )

    def override_get_session():
        yield session

    def override_get_user_service():
        return service

    def override_get_audit_service():
        return audit_service

    def override_get_current_user():
        return admin_user

    session.scalar.return_value = (
        admin_role
    )

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_user_service
    ] = override_get_user_service

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
    last_login_at: str | None = None,
    created_at: str = "2026-08-06T09:00:00",
    updated_at: str = "2026-08-06T09:00:00",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=user_id,
        full_name=full_name,
        username=username,
        email=email,
        password_hash="protected-password-hash",
        role_id=role_id,
        is_active=is_active,
        last_login_at=last_login_at,
        created_at=created_at,
        updated_at=updated_at,
    )


def expected_user_response(
    user_id: int = 10,
    full_name: str = "Lucas Miura",
    username: str = "lucas.miura",
    email: str = "lucas@example.com",
    role_id: int = 1,
    is_active: int = 1,
    last_login_at: str | None = None,
) -> dict:
    return {
        "id": user_id,
        "full_name": full_name,
        "username": username,
        "email": email,
        "role_id": role_id,
        "is_active": is_active,
        "last_login_at": last_login_at,
        "created_at": "2026-08-06T09:00:00",
        "updated_at": "2026-08-06T09:00:00",
    }


def test_should_create_user(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user()

    service.create.return_value = user

    response = client.post(
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": 1,
        },
    )

    assert response.status_code == 201

    assert response.json() == (
        expected_user_response()
    )

    assert "password" not in response.json()
    assert "password_hash" not in response.json()

    service.create.assert_called_once_with(
        full_name="Lucas Miura",
        username="lucas.miura",
        email="lucas@example.com",
        password="SenhaSegura123",
        role_id=1,
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="CREATE",
        module="USER",
        entity_type="User",
        entity_id=10,
        description="Usuário cadastrado.",
        new_values={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "role_id": 1,
            "is_active": 1,
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )

    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "missing_field",
    ),
    [
        (
            {
                "username": "lucas.miura",
                "email": "lucas@example.com",
                "password": "SenhaSegura123",
                "role_id": 1,
            },
            "full_name",
        ),
        (
            {
                "full_name": "Lucas Miura",
                "email": "lucas@example.com",
                "password": "SenhaSegura123",
                "role_id": 1,
            },
            "username",
        ),
        (
            {
                "full_name": "Lucas Miura",
                "username": "lucas.miura",
                "password": "SenhaSegura123",
                "role_id": 1,
            },
            "email",
        ),
        (
            {
                "full_name": "Lucas Miura",
                "username": "lucas.miura",
                "email": "lucas@example.com",
                "role_id": 1,
            },
            "password",
        ),
        (
            {
                "full_name": "Lucas Miura",
                "username": "lucas.miura",
                "email": "lucas@example.com",
                "password": "SenhaSegura123",
            },
            "role_id",
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
        "/users",
        json=payload,
    )

    assert response.status_code == 422
    assert missing_field in response.text

    service.create.assert_not_called()

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
            "full_name",
            "",
        ),
        (
            "full_name",
            "   ",
        ),
        (
            "username",
            "",
        ),
        (
            "username",
            "   ",
        ),
        (
            "email",
            "",
        ),
        (
            "email",
            "   ",
        ),
        (
            "password",
            "1234567",
        ),
    ],
)
def test_should_return_422_when_create_text_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    value: str,
) -> None:
    payload = {
        "full_name": "Lucas Miura",
        "username": "lucas.miura",
        "email": "lucas@example.com",
        "password": "SenhaSegura123",
        "role_id": 1,
    }

    payload[field] = value

    response = client.post(
        "/users",
        json=payload,
    )

    assert response.status_code == 422

    service.create.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    "role_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_role_id_is_invalid_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    role_id: int,
) -> None:
    response = client.post(
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": role_id,
        },
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
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": 1,
            "is_active": 1,
        },
    )

    assert response.status_code == 422

    service.create.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        "Perfil de acesso não encontrado.",
    ],
)
def test_should_return_404_when_related_resource_is_not_found_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": 99,
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
            "Já existe um usuário com este "
            "username."
        ),
        (
            "Já existe um usuário com este "
            "e-mail."
        ),
    ],
)
def test_should_return_409_when_user_data_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": 1,
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
        "O e-mail informado é inválido.",
        (
            "A senha deve possuir pelo menos "
            "8 caracteres."
        ),
        "O username é obrigatório.",
    ],
)
def test_should_return_400_when_business_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
) -> None:
    service.create.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": 1,
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
        "/users",
        json={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "password": "SenhaSegura123",
            "role_id": 1,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_users(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_all.return_value = [
        create_user(),
        create_user(
            user_id=11,
            full_name="Maria Silva",
            username="maria.silva",
            email="maria@example.com",
            role_id=2,
            is_active=0,
            last_login_at="2026-08-05T18:00:00",
        ),
    ]

    response = client.get(
        "/users"
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_user_response(),
        expected_user_response(
            user_id=11,
            full_name="Maria Silva",
            username="maria.silva",
            email="maria@example.com",
            role_id=2,
            is_active=0,
            last_login_at="2026-08-05T18:00:00",
        ),
    ]

    service.list_all.assert_called_once_with()


def test_should_return_empty_user_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_all.return_value = []

    response = client.get(
        "/users"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_all.assert_called_once_with()


def test_should_get_user(
    client: TestClient,
    service: Mock,
) -> None:
    user = create_user()

    service.get_required.return_value = user

    response = client.get(
        "/users/10"
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_user_response()
    )

    service.get_required.assert_called_once_with(
        10
    )


def test_should_return_404_when_user_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    message = "Usuário não encontrado."

    service.get_required.side_effect = (
        ValueError(message)
    )

    response = client.get(
        "/users/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message,
    }

    service.get_required.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "user_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_user_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    user_id: int,
) -> None:
    response = client.get(
        f"/users/{user_id}"
    )

    assert response.status_code == 422

    service.get_required.assert_not_called()


def test_should_update_user(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user(
        full_name="Lucas Atualizado",
        username="lucas.atualizado",
        email="novo@example.com",
        role_id=2,
    )

    service.get_required.return_value = (
        create_user()
    )

    service.update.return_value = user

    response = client.put(
        "/users/10",
        json={
            "full_name": "Lucas Atualizado",
            "username": "lucas.atualizado",
            "email": "novo@example.com",
            "role_id": 2,
        },
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_user_response(
            full_name="Lucas Atualizado",
            username="lucas.atualizado",
            email="novo@example.com",
            role_id=2,
        )
    )

    service.update.assert_called_once_with(
        10,
        full_name="Lucas Atualizado",
        username="lucas.atualizado",
        email="novo@example.com",
        role_id=2,
    )

    service.get_required.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="UPDATE",
        module="USER",
        entity_type="User",
        entity_id=10,
        description="Usuário atualizado.",
        old_values={
            "full_name": "Lucas Miura",
            "username": "lucas.miura",
            "email": "lucas@example.com",
            "role_id": 1,
        },
        new_values={
            "full_name": "Lucas Atualizado",
            "username": "lucas.atualizado",
            "email": "novo@example.com",
            "role_id": 2,
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )

    session.rollback.assert_not_called()


def test_should_update_only_provided_user_field(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user(
        full_name="Novo Nome",
    )

    service.get_required.return_value = (
        create_user()
    )

    service.update.return_value = user

    response = client.put(
        "/users/10",
        json={
            "full_name": "Novo Nome",
        },
    )

    assert response.status_code == 200

    service.update.assert_called_once_with(
        10,
        full_name="Novo Nome",
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="UPDATE",
        module="USER",
        entity_type="User",
        entity_id=10,
        description="Usuário atualizado.",
        old_values={
            "full_name": "Lucas Miura",
        },
        new_values={
            "full_name": "Novo Nome",
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )


def test_should_allow_empty_update_payload(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user()

    service.update.return_value = user

    response = client.put(
        "/users/10",
        json={},
    )

    assert response.status_code == 200

    service.update.assert_called_once_with(
        10
    )

    service.get_required.assert_not_called()

    audit_service.register.assert_not_called()

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )


@pytest.mark.parametrize(
    (
        "payload",
        "expected_status",
    ),
    [
        (
            {
                "full_name": "",
            },
            422,
        ),
        (
            {
                "username": "   ",
            },
            422,
        ),
        (
            {
                "email": "",
            },
            422,
        ),
        (
            {
                "role_id": 0,
            },
            422,
        ),
        (
            {
                "unexpected_field": "value",
            },
            422,
        ),
    ],
)
def test_should_return_422_when_update_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
    expected_status: int,
) -> None:
    response = client.put(
        "/users/10",
        json=payload,
    )

    assert response.status_code == expected_status

    service.update.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Usuário não encontrado.",
            404,
        ),
        (
            "Perfil de acesso não encontrado.",
            404,
        ),
        (
            (
                "Já existe um usuário com este "
                "username."
            ),
            409,
        ),
        (
            (
                "Já existe um usuário com este "
                "e-mail."
            ),
            409,
        ),
        (
            "O e-mail informado é inválido.",
            400,
        ),
    ],
)
def test_should_convert_business_error_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
    expected_status: int,
) -> None:
    service.update.side_effect = (
        ValueError(message)
    )

    response = client.put(
        "/users/10",
        json={
            "full_name": "Novo Nome",
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.put(
        "/users/10",
        json={
            "full_name": "Novo Nome",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_activate_user(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user(
        is_active=1,
    )

    service.activate.return_value = user

    response = client.patch(
        "/users/10/activate"
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_user_response(
            is_active=1,
        )
    )

    service.activate.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="ACTIVATE",
        module="USER",
        entity_type="User",
        entity_id=10,
        description="Usuário ativado.",
        old_values={
            "is_active": 0,
        },
        new_values={
            "is_active": 1,
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )


def test_should_deactivate_user(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user(
        is_active=0,
    )

    service.deactivate.return_value = user

    response = client.patch(
        "/users/10/deactivate",
        json={
            "justification": (
                "Usuário desligado da empresa."
            ),
        },
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_user_response(
            is_active=0,
        )
    )

    service.deactivate.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="DEACTIVATE",
        module="USER",
        entity_type="User",
        entity_id=10,
        description="Usuário desativado.",
        old_values={
            "is_active": 1,
        },
        new_values={
            "is_active": 0,
        },
        justification=(
            "Usuário desligado da empresa."
        ),
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
            "justification": "",
        },
        {
            "justification": "   ",
        },
    ],
)
def test_should_return_422_when_deactivate_justification_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, object],
) -> None:
    response = client.patch(
        "/users/10/deactivate",
        json=payload,
    )

    assert response.status_code == 422

    service.deactivate.assert_not_called()


@pytest.mark.parametrize(
    (
        "endpoint",
        "service_method",
        "message",
        "expected_status",
    ),
    [
        (
            "/users/10/activate",
            "activate",
            "Usuário não encontrado.",
            404,
        ),
        (
            "/users/10/activate",
            "activate",
            "O usuário já está ativo.",
            400,
        ),
        (
            "/users/10/deactivate",
            "deactivate",
            "Usuário não encontrado.",
            404,
        ),
        (
            "/users/10/deactivate",
            "deactivate",
            "O usuário já está inativo.",
            400,
        ),
    ],
)
def test_should_convert_business_error_on_user_status_change(
    client: TestClient,
    session: Mock,
    service: Mock,
    endpoint: str,
    service_method: str,
    message: str,
    expected_status: int,
) -> None:
    method_mock = getattr(
        service,
        service_method,
    )

    method_mock.side_effect = (
        ValueError(message)
    )

    if endpoint.endswith(
        "/deactivate"
    ):
        response = client.patch(
            endpoint,
            json={
                "justification": (
                    "Desativação de teste."
                ),
            },
        )
    else:
        response = client.patch(
            endpoint
        )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "endpoint",
    [
        "/users/0/activate",
        "/users/-1/activate",
        "/users/0/deactivate",
        "/users/-1/deactivate",
    ],
)
def test_should_return_422_when_user_id_is_invalid_on_status_change(
    client: TestClient,
    session: Mock,
    service: Mock,
    endpoint: str,
) -> None:
    if endpoint.endswith(
        "/deactivate"
    ):
        response = client.patch(
            endpoint,
            json={
                "justification": (
                    "Desativação de teste."
                ),
            },
        )
    else:
        response = client.patch(
            endpoint
        )

    assert response.status_code == 422

    service.activate.assert_not_called()
    service.deactivate.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_reset_user_password(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user()

    service.reset_password.return_value = user

    response = client.patch(
        "/users/10/reset-password",
        json={
            "new_password": "NovaSenhaSegura123",
        },
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_user_response()
    )

    assert "password_hash" not in response.json()

    service.reset_password.assert_called_once_with(
        user_id=10,
        new_password="NovaSenhaSegura123",
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="RESET_PASSWORD",
        module="USER",
        entity_type="User",
        entity_id=10,
        description=(
            "Senha do usuário redefinida "
            "administrativamente."
        ),
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
            "new_password": "",
        },
        {
            "new_password": "1234567",
        },
        {
            "new_password": "NovaSenha123",
            "unexpected_field": "value",
        },
    ],
)
def test_should_return_422_when_reset_password_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
) -> None:
    response = client.patch(
        "/users/10/reset-password",
        json=payload,
    )

    assert response.status_code == 422

    service.reset_password.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Usuário não encontrado.",
            404,
        ),
        (
            (
                "A nova senha deve ser diferente "
                "da senha atual."
            ),
            400,
        ),
        (
            (
                "A senha deve possuir pelo menos "
                "8 caracteres."
            ),
            400,
        ),
    ],
)
def test_should_convert_business_error_on_reset_password(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
    expected_status: int,
) -> None:
    service.reset_password.side_effect = (
        ValueError(message)
    )

    response = client.patch(
        "/users/10/reset-password",
        json={
            "new_password": "NovaSenhaSegura123",
        },
    )

    assert response.status_code == expected_status

    assert response.json() == {
        "detail": message,
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_change_user_password(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    user = create_user()

    service.change_password.return_value = user

    response = client.patch(
        "/users/me/change-password",
        json={
            "current_password": "SenhaAtual123",
            "new_password": "SenhaNova123",
        },
    )

    assert response.status_code == 200

    assert response.json() == (
        expected_user_response()
    )

    service.change_password.assert_called_once_with(
        user_id=10,
        current_password="SenhaAtual123",
        new_password="SenhaNova123",
    )

    audit_service.register.assert_called_once_with(
        user_id=10,
        action="CHANGE_PASSWORD",
        module="USER",
        entity_type="User",
        entity_id=10,
        description=(
            "Usuário alterou a própria senha."
        ),
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        user
    )

def test_should_rollback_when_audit_fails_on_deactivate(
    client: TestClient,
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> None:
    service.deactivate.return_value = (
        create_user(
            is_active=0,
        )
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.patch(
        "/users/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 500

    service.deactivate.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()

@pytest.mark.parametrize(
    "payload",
    [
        {},
        {
            "new_password": "SenhaNova123",
        },
        {
            "current_password": "SenhaAtual123",
        },
        {
            "current_password": "",
            "new_password": "SenhaNova123",
        },
        {
            "current_password": "SenhaAtual123",
            "new_password": "1234567",
        },
        {
            "current_password": "SenhaAtual123",
            "new_password": "SenhaNova123",
            "unexpected_field": "value",
        },
    ],
)
def test_should_return_422_when_change_password_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict,
) -> None:
    response = client.patch(
        "/users/me/change-password",
        json=payload,
    )

    assert response.status_code == 422

    service.change_password.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "message",
        "expected_status",
    ),
    [
        (
            "Usuário não encontrado.",
            404,
        ),
        (
            "A senha atual está incorreta.",
            400,
        ),
        (
            (
                "A nova senha deve ser diferente "
                "da senha atual."
            ),
            400,
        ),
        (
            (
                "A senha deve possuir pelo menos "
                "8 caracteres."
            ),
            400,
        ),
    ],
)
def test_should_convert_business_error_on_change_password(
    client: TestClient,
    session: Mock,
    service: Mock,
    message: str,
    expected_status: int,
) -> None:
    service.change_password.side_effect = (
        ValueError(message)
    )

    response = client.patch(
        "/users/me/change-password",
        json={
            "current_password": "SenhaAtual123",
            "new_password": "SenhaNova123",
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
    "endpoint",
    [
        "/users/0/reset-password",
        "/users/-1/reset-password",
    ],
)
def test_should_return_422_when_user_id_is_invalid_on_password_operation(
    client: TestClient,
    session: Mock,
    service: Mock,
    endpoint: str,
) -> None:
    payload = (
        {
            "new_password": "NovaSenhaSegura123",
        }
        if endpoint.endswith(
            "reset-password"
        )
        else {
            "current_password": "SenhaAtual123",
            "new_password": "SenhaNova123",
        }
    )

    response = client.patch(
        endpoint,
        json=payload,
    )

    assert response.status_code == 422

    service.reset_password.assert_not_called()
    service.change_password.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "endpoint",
        "service_method",
        "payload",
    ),
    [
        (
            "/users/10/activate",
            "activate",
            None,
        ),
        (
            "/users/10/deactivate",
            "deactivate",
            {
                "justification": "Desativação de teste.",
            },
        ),
        (
            "/users/10/reset-password",
            "reset_password",
            {
                "new_password": (
                    "NovaSenhaSegura123"
                ),
            },
        ),
        (
            "/users/me/change-password",
            "change_password",
            {
                "current_password": (
                    "SenhaAtual123"
                ),
                "new_password": (
                    "SenhaNova123"
                ),
            },
        ),
    ],
)
def test_should_rollback_when_unexpected_error_occurs_on_patch_operation(
    client: TestClient,
    session: Mock,
    service: Mock,
    endpoint: str,
    service_method: str,
    payload: dict | None,
) -> None:
    method_mock = getattr(
        service,
        service_method,
    )

    method_mock.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    if payload is None:
        response = client.patch(
            endpoint
        )

    else:
        response = client.patch(
            endpoint,
            json=payload,
        )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_return_401_without_authentication() -> None:
    test_app = FastAPI()

    test_app.include_router(
        router
    )

    client = TestClient(
        test_app,
        raise_server_exceptions=False,
    )

    response = client.get(
        "/users"
    )

    assert response.status_code == 401


def test_should_return_403_when_non_admin_lists_users(
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

    def override_get_user_service():
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
        get_user_service
    ] = override_get_user_service

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
        "/users"
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