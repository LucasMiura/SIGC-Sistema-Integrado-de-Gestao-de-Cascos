from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.repositories.role_repository import (
    RoleRepository,
)
from src.repositories.user_repository import (
    UserRepository,
)
from src.services.user_service import (
    FIELD_NOT_PROVIDED,
    UserService,
)


@pytest.fixture
def user_repository() -> Mock:
    repository = Mock(
        spec=UserRepository,
    )

    repository.add.side_effect = (
        lambda user: user
    )

    repository.save.side_effect = (
        lambda user: user
    )

    return repository


@pytest.fixture
def role_repository() -> Mock:
    return Mock(
        spec=RoleRepository,
    )


@pytest.fixture
def service(
    user_repository: Mock,
    role_repository: Mock,
) -> UserService:
    return UserService(
        repository=user_repository,
        role_repository=role_repository,
    )


def create_user(
    user_id: int = 10,
    full_name: str = "Lucas Miura",
    username: str = "lucas.miura",
    email: str = "lucas@example.com",
    password_hash: str = "stored-password-hash",
    role_id: int = 1,
    is_active: int = 1,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=user_id,
        full_name=full_name,
        username=username,
        email=email,
        password_hash=password_hash,
        role_id=role_id,
        is_active=is_active,
        last_login_at=None,
    )


def create_role(
    role_id: int = 1,
    name: str = "Administrador Master",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=role_id,
        name=name,
        description=None,
    )


def configure_valid_creation(
    user_repository: Mock,
    role_repository: Mock,
) -> None:
    role_repository.get_by_id.return_value = (
        create_role()
    )

    user_repository.get_by_username.return_value = (
        None
    )

    user_repository.get_by_email.return_value = (
        None
    )


def test_should_get_user_by_id(
    service: UserService,
    user_repository: Mock,
) -> None:
    expected = create_user()

    user_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_by_id(
        10
    )

    assert result == expected

    user_repository.get_by_id.assert_called_once_with(
        10
    )


@pytest.mark.parametrize(
    "user_id",
    [
        0,
        -1,
    ],
)
def test_should_return_none_for_invalid_id_on_optional_get(
    service: UserService,
    user_repository: Mock,
    user_id: int,
) -> None:
    result = service.get_by_id(
        user_id
    )

    assert result is None

    user_repository.get_by_id.assert_not_called()


def test_should_get_required_user(
    service: UserService,
    user_repository: Mock,
) -> None:
    expected = create_user()

    user_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_required(
        10
    )

    assert result == expected


@pytest.mark.parametrize(
    "user_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_id_on_required_get(
    service: UserService,
    user_repository: Mock,
    user_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário deve ser "
            "maior que zero."
        ),
    ):
        service.get_required(
            user_id
        )

    user_repository.get_by_id.assert_not_called()


def test_should_reject_missing_required_user(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Usuário não encontrado.",
    ):
        service.get_required(
            10
        )


def test_should_get_user_by_normalized_username(
    service: UserService,
    user_repository: Mock,
) -> None:
    expected = create_user()

    user_repository.get_by_username.return_value = (
        expected
    )

    result = service.get_by_username(
        " lucas.miura "
    )

    assert result == expected

    user_repository.get_by_username.assert_called_once_with(
        "lucas.miura"
    )


@pytest.mark.parametrize(
    "username",
    [
        "",
        "   ",
    ],
)
def test_should_return_none_for_blank_username(
    service: UserService,
    user_repository: Mock,
    username: str,
) -> None:
    result = service.get_by_username(
        username
    )

    assert result is None

    user_repository.get_by_username.assert_not_called()


def test_should_get_user_by_normalized_email(
    service: UserService,
    user_repository: Mock,
) -> None:
    expected = create_user()

    user_repository.get_by_email.return_value = (
        expected
    )

    result = service.get_by_email(
        " LUCAS@EXAMPLE.COM "
    )

    assert result == expected

    user_repository.get_by_email.assert_called_once_with(
        "lucas@example.com"
    )


@pytest.mark.parametrize(
    "email",
    [
        "",
        "   ",
    ],
)
def test_should_return_none_for_blank_email(
    service: UserService,
    user_repository: Mock,
    email: str,
) -> None:
    result = service.get_by_email(
        email
    )

    assert result is None

    user_repository.get_by_email.assert_not_called()


def test_should_list_all_users(
    service: UserService,
    user_repository: Mock,
) -> None:
    expected = [
        create_user(),
        create_user(
            user_id=11,
            username="maria.silva",
            email="maria@example.com",
        ),
    ]

    user_repository.list_all.return_value = (
        expected
    )

    result = service.list_all()

    assert result == expected

    user_repository.list_all.assert_called_once_with()


def test_should_create_user(
    service: UserService,
    user_repository: Mock,
    role_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_valid_creation(
        user_repository,
        role_repository,
    )

    hash_mock = Mock(
        return_value="new-password-hash",
    )

    monkeypatch.setattr(
        "src.services.user_service.hash_password",
        hash_mock,
    )

    created = service.create(
        full_name=" Lucas do Nascimento Miura ",
        username=" lucas.miura ",
        email=" LUCAS@EXAMPLE.COM ",
        password="senha123",
        role_id=1,
    )

    assert (
        created.full_name
        == "Lucas do Nascimento Miura"
    )

    assert created.username == "lucas.miura"
    assert created.email == "lucas@example.com"
    assert created.password_hash == "new-password-hash"
    assert created.role_id == 1
    assert created.is_active == 1

    role_repository.get_by_id.assert_called_once_with(
        1
    )

    user_repository.get_by_username.assert_called_once_with(
        "lucas.miura"
    )

    user_repository.get_by_email.assert_called_once_with(
        "lucas@example.com"
    )

    hash_mock.assert_called_once_with(
        "senha123"
    )

    user_repository.add.assert_called_once_with(
        created
    )


@pytest.mark.parametrize(
    (
        "field_name",
        "field_value",
        "expected_message",
    ),
    [
        (
            "full_name",
            "",
            "O nome completo é obrigatório.",
        ),
        (
            "full_name",
            "   ",
            "O nome completo é obrigatório.",
        ),
        (
            "username",
            "",
            "O username é obrigatório.",
        ),
        (
            "username",
            "   ",
            "O username é obrigatório.",
        ),
        (
            "email",
            "",
            "O e-mail é obrigatório.",
        ),
        (
            "email",
            "   ",
            "O e-mail é obrigatório.",
        ),
    ],
)
def test_should_reject_blank_required_field_on_create(
    service: UserService,
    user_repository: Mock,
    field_name: str,
    field_value: str,
    expected_message: str,
) -> None:
    payload = {
        "full_name": "Lucas Miura",
        "username": "lucas.miura",
        "email": "lucas@example.com",
        "password": "senha123",
        "role_id": 1,
    }

    payload[field_name] = field_value

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create(
            **payload,
        )

    user_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "email",
    [
        "email-invalido",
        "@example.com",
        "lucas@",
    ],
)
def test_should_reject_invalid_email_on_create(
    service: UserService,
    user_repository: Mock,
    email: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="O e-mail informado é inválido.",
    ):
        service.create(
            full_name="Lucas Miura",
            username="lucas.miura",
            email=email,
            password="senha123",
            role_id=1,
        )

    user_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "password",
    [
        "",
        "1234567",
    ],
)
def test_should_reject_invalid_password_on_create(
    service: UserService,
    user_repository: Mock,
    password: str,
) -> None:
    expected_message = (
        "A senha é obrigatória."
        if not password
        else (
            "A senha deve possuir pelo menos "
            "8 caracteres."
        )
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create(
            full_name="Lucas Miura",
            username="lucas.miura",
            email="lucas@example.com",
            password=password,
            role_id=1,
        )

    user_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "role_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_role_id_on_create(
    service: UserService,
    user_repository: Mock,
    role_repository: Mock,
    role_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do perfil deve ser "
            "maior que zero."
        ),
    ):
        service.create(
            full_name="Lucas Miura",
            username="lucas.miura",
            email="lucas@example.com",
            password="senha123",
            role_id=role_id,
        )

    role_repository.get_by_id.assert_not_called()
    user_repository.add.assert_not_called()


def test_should_reject_missing_role_on_create(
    service: UserService,
    user_repository: Mock,
    role_repository: Mock,
) -> None:
    role_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Perfil de acesso não encontrado.",
    ):
        service.create(
            full_name="Lucas Miura",
            username="lucas.miura",
            email="lucas@example.com",
            password="senha123",
            role_id=99,
        )

    user_repository.add.assert_not_called()


def test_should_reject_duplicated_username_on_create(
    service: UserService,
    user_repository: Mock,
    role_repository: Mock,
) -> None:
    role_repository.get_by_id.return_value = (
        create_role()
    )

    user_repository.get_by_username.return_value = (
        create_user()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe um usuário com este "
            "username."
        ),
    ):
        service.create(
            full_name="Lucas Miura",
            username="lucas.miura",
            email="lucas@example.com",
            password="senha123",
            role_id=1,
        )

    user_repository.get_by_email.assert_not_called()
    user_repository.add.assert_not_called()


def test_should_reject_duplicated_email_on_create(
    service: UserService,
    user_repository: Mock,
    role_repository: Mock,
) -> None:
    role_repository.get_by_id.return_value = (
        create_role()
    )

    user_repository.get_by_username.return_value = (
        None
    )

    user_repository.get_by_email.return_value = (
        create_user()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe um usuário com este "
            "e-mail."
        ),
    ):
        service.create(
            full_name="Lucas Miura",
            username="novo.usuario",
            email="lucas@example.com",
            password="senha123",
            role_id=1,
        )

    user_repository.add.assert_not_called()


def test_should_update_all_user_fields(
    service: UserService,
    user_repository: Mock,
    role_repository: Mock,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    user_repository.get_by_username.return_value = (
        None
    )

    user_repository.get_by_email.return_value = (
        None
    )

    role_repository.get_by_id.return_value = (
        create_role(
            role_id=2,
            name="Comprador",
        )
    )

    updated = service.update(
        10,
        full_name=" Lucas Atualizado ",
        username=" lucas.atualizado ",
        email=" NOVO@EXAMPLE.COM ",
        role_id=2,
    )

    assert updated.full_name == "Lucas Atualizado"
    assert updated.username == "lucas.atualizado"
    assert updated.email == "novo@example.com"
    assert updated.role_id == 2

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_update_only_provided_field(
    service: UserService,
    user_repository: Mock,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    updated = service.update(
        10,
        full_name="Lucas Atualizado",
    )

    assert updated.full_name == "Lucas Atualizado"
    assert updated.username == "lucas.miura"
    assert updated.email == "lucas@example.com"
    assert updated.role_id == 1

    user_repository.get_by_username.assert_not_called()
    user_repository.get_by_email.assert_not_called()


def test_should_allow_same_username_and_email_on_update(
    service: UserService,
    user_repository: Mock,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    updated = service.update(
        10,
        username="lucas.miura",
        email="LUCAS@EXAMPLE.COM",
    )

    assert updated.username == "lucas.miura"
    assert updated.email == "lucas@example.com"

    user_repository.get_by_username.assert_not_called()
    user_repository.get_by_email.assert_not_called()


def test_should_allow_repository_result_for_same_user_on_username_update(
    service: UserService,
    user_repository: Mock,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    user_repository.get_by_username.return_value = (
        user
    )

    updated = service.update(
        10,
        username="novo.username",
    )

    assert updated.username == "novo.username"


def test_should_reject_username_used_by_another_user_on_update(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    user_repository.get_by_username.return_value = (
        create_user(
            user_id=99,
            username="outro.usuario",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe um usuário com este "
            "username."
        ),
    ):
        service.update(
            10,
            username="outro.usuario",
        )

    user_repository.save.assert_not_called()


def test_should_reject_email_used_by_another_user_on_update(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    user_repository.get_by_email.return_value = (
        create_user(
            user_id=99,
            email="outro@example.com",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe um usuário com este "
            "e-mail."
        ),
    ):
        service.update(
            10,
            email="outro@example.com",
        )

    user_repository.save.assert_not_called()


def test_should_reject_invalid_update_field_type(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    with pytest.raises(
        ValueError,
        match="O nome completo é obrigatório.",
    ):
        service.update(
            10,
            full_name=None,
        )

    user_repository.save.assert_not_called()


def test_should_preserve_all_fields_when_update_receives_no_changes(
    service: UserService,
    user_repository: Mock,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    result = service.update(
        10,
        full_name=FIELD_NOT_PROVIDED,
        username=FIELD_NOT_PROVIDED,
        email=FIELD_NOT_PROVIDED,
        role_id=FIELD_NOT_PROVIDED,
    )

    assert result == user

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_activate_inactive_user(
    service: UserService,
    user_repository: Mock,
) -> None:
    user = create_user(
        is_active=0,
    )

    user_repository.get_by_id.return_value = (
        user
    )

    result = service.activate(
        10
    )

    assert result.is_active == 1

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_reject_activating_active_user(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user(
            is_active=1,
        )
    )

    with pytest.raises(
        ValueError,
        match="O usuário já está ativo.",
    ):
        service.activate(
            10
        )

    user_repository.save.assert_not_called()


def test_should_deactivate_active_user(
    service: UserService,
    user_repository: Mock,
) -> None:
    user = create_user(
        is_active=1,
    )

    user_repository.get_by_id.return_value = (
        user
    )

    result = service.deactivate(
        10
    )

    assert result.is_active == 0

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_reject_deactivating_inactive_user(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O usuário já está inativo.",
    ):
        service.deactivate(
            10
        )

    user_repository.save.assert_not_called()


def test_should_reset_password(
    service: UserService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    verify_mock = Mock(
        return_value=False,
    )

    hash_mock = Mock(
        return_value="reset-password-hash",
    )

    monkeypatch.setattr(
        "src.services.user_service.verify_password",
        verify_mock,
    )

    monkeypatch.setattr(
        "src.services.user_service.hash_password",
        hash_mock,
    )

    result = service.reset_password(
        user_id=10,
        new_password="novaSenha123",
    )

    assert (
        result.password_hash
        == "reset-password-hash"
    )

    verify_mock.assert_called_once_with(
        "novaSenha123",
        "stored-password-hash",
    )

    hash_mock.assert_called_once_with(
        "novaSenha123"
    )

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_reject_same_password_on_reset(
    service: UserService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    monkeypatch.setattr(
        "src.services.user_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    with pytest.raises(
        ValueError,
        match=(
            "A nova senha deve ser diferente "
            "da senha atual."
        ),
    ):
        service.reset_password(
            user_id=10,
            new_password="senhaAtual123",
        )

    user_repository.save.assert_not_called()


def test_should_change_password(
    service: UserService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user = create_user()

    user_repository.get_by_id.return_value = (
        user
    )

    verify_mock = Mock(
        side_effect=[
            True,
            False,
        ],
    )

    hash_mock = Mock(
        return_value="changed-password-hash",
    )

    monkeypatch.setattr(
        "src.services.user_service.verify_password",
        verify_mock,
    )

    monkeypatch.setattr(
        "src.services.user_service.hash_password",
        hash_mock,
    )

    result = service.change_password(
        user_id=10,
        current_password="senhaAtual123",
        new_password="senhaNova123",
    )

    assert (
        result.password_hash
        == "changed-password-hash"
    )

    assert verify_mock.call_count == 2

    verify_mock.assert_any_call(
        "senhaAtual123",
        "stored-password-hash",
    )

    verify_mock.assert_any_call(
        "senhaNova123",
        "stored-password-hash",
    )

    hash_mock.assert_called_once_with(
        "senhaNova123"
    )

    user_repository.save.assert_called_once_with(
        user
    )


def test_should_reject_blank_current_password(
    service: UserService,
    user_repository: Mock,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    with pytest.raises(
        ValueError,
        match="A senha atual é obrigatória.",
    ):
        service.change_password(
            user_id=10,
            current_password="",
            new_password="senhaNova123",
        )

    user_repository.save.assert_not_called()


def test_should_reject_incorrect_current_password(
    service: UserService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    monkeypatch.setattr(
        "src.services.user_service.verify_password",
        Mock(
            return_value=False,
        ),
    )

    with pytest.raises(
        ValueError,
        match="A senha atual está incorreta.",
    ):
        service.change_password(
            user_id=10,
            current_password="senhaErrada",
            new_password="senhaNova123",
        )

    user_repository.save.assert_not_called()


def test_should_reject_short_new_password_on_change(
    service: UserService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    monkeypatch.setattr(
        "src.services.user_service.verify_password",
        Mock(
            return_value=True,
        ),
    )

    with pytest.raises(
        ValueError,
        match=(
            "A senha deve possuir pelo menos "
            "8 caracteres."
        ),
    ):
        service.change_password(
            user_id=10,
            current_password="senhaAtual123",
            new_password="1234567",
        )

    user_repository.save.assert_not_called()


def test_should_reject_same_new_password_on_change(
    service: UserService,
    user_repository: Mock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    user_repository.get_by_id.return_value = (
        create_user()
    )

    verify_mock = Mock(
        side_effect=[
            True,
            True,
        ],
    )

    monkeypatch.setattr(
        "src.services.user_service.verify_password",
        verify_mock,
    )

    with pytest.raises(
        ValueError,
        match=(
            "A nova senha deve ser diferente "
            "da senha atual."
        ),
    ):
        service.change_password(
            user_id=10,
            current_password="senhaAtual123",
            new_password="senhaAtual123",
        )

    user_repository.save.assert_not_called()