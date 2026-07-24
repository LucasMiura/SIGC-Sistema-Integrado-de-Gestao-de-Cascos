from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.security.password import hash_password


class UserService:
    """Regras de negócio relacionadas a usuários."""

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        normalized_username = username.strip()

        if not normalized_username:
            return None

        return self.repository.get_by_username(
            normalized_username
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        normalized_email = email.strip().lower()

        if not normalized_email:
            return None

        return self.repository.get_by_email(
            normalized_email
        )

    def list_all(self) -> list[User]:
        return self.repository.list_all()

    def create(
        self,
        full_name: str,
        username: str,
        email: str,
        password: str,
        role_id: int,
    ) -> User:
        normalized_full_name = full_name.strip()
        normalized_username = username.strip()
        normalized_email = email.strip().lower()

        if not normalized_full_name:
            raise ValueError(
                "O nome completo é obrigatório."
            )

        if not normalized_username:
            raise ValueError(
                "O username é obrigatório."
            )

        if not normalized_email:
            raise ValueError(
                "O e-mail é obrigatório."
            )

        if not password:
            raise ValueError(
                "A senha é obrigatória."
            )

        if len(password) < 8:
            raise ValueError(
                "A senha deve possuir pelo menos 8 caracteres."
            )

        existing_username = (
            self.repository.get_by_username(
                normalized_username
            )
        )

        if existing_username is not None:
            raise ValueError(
                "Já existe um usuário com este username."
            )

        existing_email = (
            self.repository.get_by_email(
                normalized_email
            )
        )

        if existing_email is not None:
            raise ValueError(
                "Já existe um usuário com este e-mail."
            )

        user = User(
            full_name=normalized_full_name,
            username=normalized_username,
            email=normalized_email,
            password_hash=hash_password(password),
            role_id=role_id,
            is_active=1,
        )

        def deactivate(
            self,
            user_id: int,
        ) -> User:
            user = self.repository.get_by_id(user_id)

            if user is None:
                raise ValueError(
                    "Usuário não encontrado."
                )

            if not user.is_active:
                raise ValueError(
                    "O usuário já está inativo."
                )

            user.is_active = 0

            return self.repository.save(user)

        def activate(
            self,
            user_id: int,
        ) -> User:
            user = self.repository.get_by_id(user_id)

            if user is None:
                raise ValueError(
                    "Usuário não encontrado."
                )

            if user.is_active:
                raise ValueError(
                    "O usuário já está ativo."
                )

            user.is_active = 1

            return self.repository.save(user)

        return self.repository.add(user)