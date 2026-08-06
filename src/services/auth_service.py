from dataclasses import dataclass

from src.core.time import now_iso
from src.models.user import User
from src.repositories.user_repository import (
    UserRepository,
)
from src.security.password import (
    verify_password,
)
from src.security.token import (
    create_access_token,
)


@dataclass(frozen=True)
class AuthenticationResult:
    """
    Resultado interno de uma autenticação
    realizada com sucesso.
    """

    access_token: str
    token_type: str
    user: User


class AuthService:
    """
    Regras de negócio relacionadas
    à autenticação dos usuários.
    """

    INVALID_CREDENTIALS_MESSAGE = (
        "Username, e-mail ou senha inválidos."
    )

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:
        self.user_repository = (
            user_repository
        )

    def authenticate(
        self,
        login: str,
        password: str,
    ) -> AuthenticationResult:
        """
        Autentica um usuário por username ou e-mail.
        """

        normalized_login = (
            self._normalize_required_login(
                login
            )
        )

        if not password:
            raise ValueError(
                self.INVALID_CREDENTIALS_MESSAGE
            )

        user = self._find_user_by_login(
            normalized_login
        )

        if user is None:
            raise ValueError(
                self.INVALID_CREDENTIALS_MESSAGE
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError(
                self.INVALID_CREDENTIALS_MESSAGE
            )

        if not user.is_active:
            raise ValueError(
                "O usuário está inativo."
            )

        access_token = create_access_token(
            user_id=user.id,
            role_id=user.role_id,
        )

        user.last_login_at = now_iso()

        saved_user = self.user_repository.save(
            user
        )

        return AuthenticationResult(
            access_token=access_token,
            token_type="bearer",
            user=saved_user,
        )

    def _find_user_by_login(
        self,
        normalized_login: str,
    ) -> User | None:
        """
        Busca primeiro por username e,
        em seguida, por e-mail.
        """

        user = self.user_repository.get_by_username(
            normalized_login
        )

        if user is not None:
            return user

        normalized_email = (
            normalized_login.lower()
        )

        return self.user_repository.get_by_email(
            normalized_email
        )

    @staticmethod
    def _normalize_required_login(
        login: str,
    ) -> str:
        normalized_login = login.strip()

        if not normalized_login:
            raise ValueError(
                (
                    "Username, e-mail ou senha "
                    "inválidos."
                )
            )

        return normalized_login