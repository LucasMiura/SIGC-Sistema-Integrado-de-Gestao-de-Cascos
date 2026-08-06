from typing import Final

from src.models.user import User
from src.repositories.role_repository import (
    RoleRepository,
)
from src.repositories.user_repository import (
    UserRepository,
)
from src.security.password import (
    hash_password,
    verify_password,
)


FIELD_NOT_PROVIDED: Final = object()


class UserService:
    """
    Regras de negócio relacionadas
    ao gerenciamento de usuários.
    """

    MINIMUM_PASSWORD_LENGTH = 8

    def __init__(
        self,
        repository: UserRepository,
        role_repository: RoleRepository,
    ) -> None:
        self.repository = repository
        self.role_repository = role_repository

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        """
        Busca um usuário pelo identificador.
        """

        if user_id <= 0:
            return None

        return self.repository.get_by_id(
            user_id
        )

    def get_required(
        self,
        user_id: int,
    ) -> User:
        """
        Busca obrigatoriamente um usuário.
        """

        self._validate_positive_id(
            user_id,
            (
                "O identificador do usuário deve ser "
                "maior que zero."
            ),
        )

        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise ValueError(
                "Usuário não encontrado."
            )

        return user

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        """
        Busca um usuário pelo username.
        """

        normalized_username = (
            self._normalize_optional_text(
                username
            )
        )

        if normalized_username is None:
            return None

        return self.repository.get_by_username(
            normalized_username
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Busca um usuário pelo e-mail.
        """

        normalized_email = (
            self._normalize_optional_email(
                email
            )
        )

        if normalized_email is None:
            return None

        return self.repository.get_by_email(
            normalized_email
        )

    def list_all(
        self,
    ) -> list[User]:
        """
        Lista todos os usuários ativos e inativos.
        """

        return self.repository.list_all()

    def create(
        self,
        full_name: str,
        username: str,
        email: str,
        password: str,
        role_id: int,
    ) -> User:
        """
        Cadastra um novo usuário.
        """

        normalized_full_name = (
            self._normalize_required_text(
                full_name,
                "O nome completo é obrigatório.",
            )
        )

        normalized_username = (
            self._normalize_required_text(
                username,
                "O username é obrigatório.",
            )
        )

        normalized_email = (
            self._normalize_required_email(
                email
            )
        )

        self._validate_password(
            password
        )

        self._validate_role_exists(
            role_id
        )

        self._ensure_username_available(
            normalized_username
        )

        self._ensure_email_available(
            normalized_email
        )

        user = User(
            full_name=normalized_full_name,
            username=normalized_username,
            email=normalized_email,
            password_hash=hash_password(
                password
            ),
            role_id=role_id,
            is_active=1,
        )

        return self.repository.add(
            user
        )

    def update(
        self,
        user_id: int,
        *,
        full_name: str | object = (
            FIELD_NOT_PROVIDED
        ),
        username: str | object = (
            FIELD_NOT_PROVIDED
        ),
        email: str | object = (
            FIELD_NOT_PROVIDED
        ),
        role_id: int | object = (
            FIELD_NOT_PROVIDED
        ),
    ) -> User:
        """
        Atualiza somente os campos enviados.

        A senha possui operações próprias e não deve
        ser alterada por este método.
        """

        user = self.get_required(
            user_id
        )

        if full_name is not FIELD_NOT_PROVIDED:
            if not isinstance(
                full_name,
                str,
            ):
                raise ValueError(
                    "O nome completo é obrigatório."
                )

            user.full_name = (
                self._normalize_required_text(
                    full_name,
                    (
                        "O nome completo "
                        "é obrigatório."
                    ),
                )
            )

        if username is not FIELD_NOT_PROVIDED:
            if not isinstance(
                username,
                str,
            ):
                raise ValueError(
                    "O username é obrigatório."
                )

            normalized_username = (
                self._normalize_required_text(
                    username,
                    "O username é obrigatório.",
                )
            )

            if (
                normalized_username
                != user.username
            ):
                self._ensure_username_available(
                    normalized_username,
                    ignored_user_id=user.id,
                )

                user.username = (
                    normalized_username
                )

        if email is not FIELD_NOT_PROVIDED:
            if not isinstance(
                email,
                str,
            ):
                raise ValueError(
                    "O e-mail é obrigatório."
                )

            normalized_email = (
                self._normalize_required_email(
                    email
                )
            )

            if normalized_email != user.email:
                self._ensure_email_available(
                    normalized_email,
                    ignored_user_id=user.id,
                )

                user.email = normalized_email

        if role_id is not FIELD_NOT_PROVIDED:
            if not isinstance(
                role_id,
                int,
            ):
                raise ValueError(
                    (
                        "O identificador do perfil deve "
                        "ser maior que zero."
                    )
                )

            self._validate_role_exists(
                role_id
            )

            user.role_id = role_id

        return self.repository.save(
            user
        )

    def activate(
        self,
        user_id: int,
    ) -> User:
        """
        Reativa um usuário inativo.
        """

        user = self.get_required(
            user_id
        )

        if user.is_active:
            raise ValueError(
                "O usuário já está ativo."
            )

        user.is_active = 1

        return self.repository.save(
            user
        )

    def deactivate(
        self,
        user_id: int,
    ) -> User:
        """
        Desativa um usuário sem excluir
        seu histórico.
        """

        user = self.get_required(
            user_id
        )

        if not user.is_active:
            raise ValueError(
                "O usuário já está inativo."
            )

        user.is_active = 0

        return self.repository.save(
            user
        )

    def reset_password(
        self,
        user_id: int,
        new_password: str,
    ) -> User:
        """
        Redefine a senha de um usuário.

        Esta operação será posteriormente restrita
        ao Administrador Master pela autorização.
        """

        user = self.get_required(
            user_id
        )

        self._validate_password(
            new_password
        )

        if verify_password(
            new_password,
            user.password_hash,
        ):
            raise ValueError(
                (
                    "A nova senha deve ser diferente "
                    "da senha atual."
                )
            )

        user.password_hash = hash_password(
            new_password
        )

        return self.repository.save(
            user
        )

    def change_password(
        self,
        user_id: int,
        current_password: str,
        new_password: str,
    ) -> User:
        """
        Permite que o usuário altere
        sua própria senha.
        """

        user = self.get_required(
            user_id
        )

        if not current_password:
            raise ValueError(
                "A senha atual é obrigatória."
            )

        if not verify_password(
            current_password,
            user.password_hash,
        ):
            raise ValueError(
                "A senha atual está incorreta."
            )

        self._validate_password(
            new_password
        )

        if verify_password(
            new_password,
            user.password_hash,
        ):
            raise ValueError(
                (
                    "A nova senha deve ser diferente "
                    "da senha atual."
                )
            )

        user.password_hash = hash_password(
            new_password
        )

        return self.repository.save(
            user
        )

    def _validate_role_exists(
        self,
        role_id: int,
    ) -> None:
        self._validate_positive_id(
            role_id,
            (
                "O identificador do perfil deve ser "
                "maior que zero."
            ),
        )

        role = self.role_repository.get_by_id(
            role_id
        )

        if role is None:
            raise ValueError(
                "Perfil de acesso não encontrado."
            )

    def _ensure_username_available(
        self,
        username: str,
        ignored_user_id: int | None = None,
    ) -> None:
        existing_user = (
            self.repository.get_by_username(
                username
            )
        )

        if (
            existing_user is not None
            and existing_user.id
            != ignored_user_id
        ):
            raise ValueError(
                (
                    "Já existe um usuário com este "
                    "username."
                )
            )

    def _ensure_email_available(
        self,
        email: str,
        ignored_user_id: int | None = None,
    ) -> None:
        existing_user = (
            self.repository.get_by_email(
                email
            )
        )

        if (
            existing_user is not None
            and existing_user.id
            != ignored_user_id
        ):
            raise ValueError(
                (
                    "Já existe um usuário com este "
                    "e-mail."
                )
            )

    @classmethod
    def _validate_password(
        cls,
        password: str,
    ) -> None:
        if not password:
            raise ValueError(
                "A senha é obrigatória."
            )

        if (
            len(password)
            < cls.MINIMUM_PASSWORD_LENGTH
        ):
            raise ValueError(
                (
                    "A senha deve possuir pelo menos "
                    "8 caracteres."
                )
            )

    @staticmethod
    def _normalize_required_text(
        value: str,
        error_message: str,
    ) -> str:
        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                error_message
            )

        return normalized_value

    @classmethod
    def _normalize_required_email(
        cls,
        email: str,
    ) -> str:
        normalized_email = (
            cls._normalize_optional_email(
                email
            )
        )

        if normalized_email is None:
            raise ValueError(
                "O e-mail é obrigatório."
            )

        if (
            "@" not in normalized_email
            or normalized_email.startswith("@")
            or normalized_email.endswith("@")
        ):
            raise ValueError(
                "O e-mail informado é inválido."
            )

        return normalized_email

    @staticmethod
    def _normalize_optional_email(
        email: str,
    ) -> str | None:
        normalized_email = (
            email.strip().lower()
        )

        return normalized_email or None

    @staticmethod
    def _normalize_optional_text(
        value: str,
    ) -> str | None:
        normalized_value = value.strip()

        return normalized_value or None

    @staticmethod
    def _validate_positive_id(
        value: int,
        error_message: str,
    ) -> None:
        if value <= 0:
            raise ValueError(
                error_message
            )