from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.repositories.user_repository import (
    UserRepository,
)
from src.services.auth_service import (
    AuthenticationResult,
    AuthService,
)


@pytest.fixture
def user_repository() -> Mock:
    repository = Mock(
        spec=UserRepository,
    )

    repository.save.side_effect = (
        lambda user: user
    )

    return repository


@pytest.fixture
def service(
    user_repository: Mock,
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
    )


def create_user(
    user_id: int = 10,
    full_name: str = "Lucas Miura",
    username: str = "lucas.miura",
    email: str = "lucas@example.com",
    password_hash: str = "stored-password-hash",
    role_id: int = 1,
    is_active: int = 1,
    last_login_at: str | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=user_id,
        full_name=full_name,
        username=username,
        email=email,
        password_hash=password_hash,
        role_id=role_id,
        is_active=is_active,
        last_login_at=last_login_at,
        created_at="2026-08-06T09:00:00",
        updated_at="2026-08-06T09:00:00",
    )


def test_should_authenticate_by_username(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    user_repository.get_by_username.return_value = (
        user
    )

    verify_password_mock = Mock(
        return_value=True,
    )

    create_token_mock = Mock(
        return_value="access-token",
    )

    now_iso_mock = Mock(
        return_value="2026-08-06T10:30:00",
    )

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        verify_password_mock,
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        create_token_mock,
    )

    monkeypatch.setattr(
        "src.services.auth_service.now_iso",
        now_iso_mock,
    )

    result = service.authenticate(
        login=" lucas.miura ",
        password="SenhaSegura123",
    )

    assert isinstance(
        result,
        AuthenticationResult,
    )

    assert result.access_token == "access-token"
    assert result.token_type == "bearer"
    assert result.user == user

    assert (
        user.last_login_at
        == "2026-08-06T10:30:00"
    )

    user_repository.get_by_username.assert_called_once_with(
        "lucas.miura"
    )

    user_repository.get_by_email.assert_not_called()

    verify_password_mock.assert_called_once_with(
        "SenhaSegura123",
        "stored-password-hash",
    )

    create_token_mock.assert_called_once_with(
        user_id=10,
        role_id=1,
    )

    now_iso_mock.assert_called_once_with()

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_authenticate_by_email(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    user_repository.get_by_username.return_value = (
        None
    )

    user_repository.get_by_email.return_value = (
        user
    )

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        Mock(
            return_value="email-access-token",
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.now_iso",
        Mock(
            return_value="2026-08-06T10:35:00",
        ),
    )

    result = service.authenticate(
        login=" LUCAS@EXAMPLE.COM ",
        password="SenhaSegura123",
    )

    assert result.access_token == (
        "email-access-token"
    )

    assert result.user == user

    user_repository.get_by_username.assert_called_once_with(
        "LUCAS@EXAMPLE.COM"
    )

    user_repository.get_by_email.assert_called_once_with(
        "lucas@example.com"
    )

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_prefer_username_before_email(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user(
        username="usuario@example.com",
    )

    user_repository.get_by_username.return_value = (
        user
    )

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        Mock(
            return_value="access-token",
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.now_iso",
        Mock(
            return_value="2026-08-06T10:40:00",
        ),
    )

    result = service.authenticate(
        login="usuario@example.com",
        password="SenhaSegura123",
    )

    assert result.user == user

    user_repository.get_by_username.assert_called_once_with(
        "usuario@example.com"
    )

    user_repository.get_by_email.assert_not_called()


@pytest.mark.parametrize(
    "login",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_login(
    service: AuthService,
    user_repository: Mock,
    login: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Username, e-mail ou senha "
            "inválidos."
        ),
    ):
        service.authenticate(
            login=login,
            password="SenhaSegura123",
        )

    user_repository.get_by_username.assert_not_called()
    user_repository.get_by_email.assert_not_called()
    user_repository.save.assert_not_called()


@pytest.mark.parametrize(
    "password",
    [
        "",
        None,
    ],
)
def test_should_reject_blank_password(
    service: AuthService,
    user_repository: Mock,
    password: str | None,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Username, e-mail ou senha "
            "inválidos."
        ),
    ):
        service.authenticate(
            login="lucas.miura",
            password=password,
        )

    user_repository.get_by_username.assert_not_called()
    user_repository.get_by_email.assert_not_called()
    user_repository.save.assert_not_called()


def test_should_reject_unknown_user(
    service: AuthService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_username.return_value = (
        None
    )

    user_repository.get_by_email.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match=(
            "Username, e-mail ou senha "
            "inválidos."
        ),
    ):
        service.authenticate(
            login="usuario.inexistente",
            password="SenhaSegura123",
        )

    user_repository.get_by_username.assert_called_once_with(
        "usuario.inexistente"
    )

    user_repository.get_by_email.assert_called_once_with(
        "usuario.inexistente"
    )

    user_repository.save.assert_not_called()


def test_should_reject_incorrect_password(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    user_repository.get_by_username.return_value = (
        user
    )

    verify_password_mock = Mock(
        return_value=False,
    )

    create_token_mock = Mock()

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        verify_password_mock,
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        create_token_mock,
    )

    with pytest.raises(
        ValueError,
        match=(
            "Username, e-mail ou senha "
            "inválidos."
        ),
    ):
        service.authenticate(
            login="lucas.miura",
            password="SenhaErrada",
        )

    verify_password_mock.assert_called_once_with(
        "SenhaErrada",
        "stored-password-hash",
    )

    create_token_mock.assert_not_called()
    user_repository.save.assert_not_called()


def test_should_reject_inactive_user(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user(
        is_active=0,
    )

    user_repository.get_by_username.return_value = (
        user
    )

    verify_password_mock = Mock(
        return_value=True,
    )

    create_token_mock = Mock()

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        verify_password_mock,
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        create_token_mock,
    )

    with pytest.raises(
        ValueError,
        match="O usuário está inativo.",
    ):
        service.authenticate(
            login="lucas.miura",
            password="SenhaSegura123",
        )

    verify_password_mock.assert_called_once_with(
        "SenhaSegura123",
        "stored-password-hash",
    )

    create_token_mock.assert_not_called()
    user_repository.save.assert_not_called()


def test_should_update_last_login_after_token_creation(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user(
        last_login_at=None,
    )

    user_repository.get_by_username.return_value = (
        user
    )

    operation_order: list[str] = []

    def create_token(
        user_id: int,
        role_id: int,
    ) -> str:
        assert user.last_login_at is None

        operation_order.append(
            "token"
        )

        return "access-token"

    def save_user(
        saved_user: SimpleNamespace,
    ) -> SimpleNamespace:
        assert (
            saved_user.last_login_at
            == "2026-08-06T10:45:00"
        )

        operation_order.append(
            "save"
        )

        return saved_user

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        create_token,
    )

    monkeypatch.setattr(
        "src.services.auth_service.now_iso",
        Mock(
            return_value="2026-08-06T10:45:00",
        ),
    )

    user_repository.save.side_effect = (
        save_user
    )

    service.authenticate(
        login="lucas.miura",
        password="SenhaSegura123",
    )

    assert operation_order == [
        "token",
        "save",
    ]


def test_should_return_user_saved_by_repository(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    saved_user = create_user(
        full_name="Usuário Persistido",
        last_login_at=(
            "2026-08-06T10:50:00"
        ),
    )

    user_repository.get_by_username.return_value = (
        user
    )

    user_repository.save.side_effect = None

    user_repository.save.return_value = (
        saved_user
    )

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        Mock(
            return_value="access-token",
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.now_iso",
        Mock(
            return_value="2026-08-06T10:50:00",
        ),
    )

    result = service.authenticate(
        login="lucas.miura",
        password="SenhaSegura123",
    )

    assert result.user == saved_user
    assert (
        result.user.full_name
        == "Usuário Persistido"
    )


def test_should_propagate_token_configuration_error_without_saving_user(
    service: AuthService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    user_repository.get_by_username.return_value = (
        user
    )

    monkeypatch.setattr(
        "src.services.auth_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    monkeypatch.setattr(
        "src.services.auth_service.create_access_token",
        Mock(
            side_effect=RuntimeError(
                (
                    "A variável SIGC_JWT_SECRET_KEY "
                    "não foi configurada."
                )
            ),
        ),
    )

    with pytest.raises(
        RuntimeError,
        match="SIGC_JWT_SECRET_KEY",
    ):
        service.authenticate(
            login="lucas.miura",
            password="SenhaSegura123",
        )

    assert user.last_login_at is None

    user_repository.save.assert_not_called()