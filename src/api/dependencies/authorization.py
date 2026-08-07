from collections.abc import Callable
from typing import Annotated

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from src.api.dependencies.auth import (
    CurrentUserDependency,
)
from src.database.connection import get_session
from src.models.user import User
from src.repositories.role_repository import (
    RoleRepository,
)


ROLE_ADMIN = "Administrador Master"
ROLE_BUYER = "Comprador"
ROLE_SELLER = "Vendedor"


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def require_roles(
    *allowed_roles: str,
) -> Callable[..., User]:
    """
    Cria uma dependência que permite acesso
    somente aos perfis informados.

    O perfil Administrador Master não recebe
    acesso automático: ele deve ser informado
    explicitamente quando a operação permitir
    seu acesso.

    Isso deixa a autorização visível na própria
    declaração de cada endpoint.
    """

    normalized_allowed_roles = {
        role.strip()
        for role in allowed_roles
        if role.strip()
    }

    if not normalized_allowed_roles:
        raise ValueError(
            (
                "Pelo menos um perfil de acesso "
                "deve ser informado."
            )
        )

    def dependency(
        current_user: CurrentUserDependency,
        session: SessionDependency,
    ) -> User:
        role_repository = RoleRepository(
            session
        )

        role = role_repository.get_by_id(
            current_user.role_id
        )

        if role is None:
            raise HTTPException(
                status_code=(
                    status.HTTP_403_FORBIDDEN
                ),
                detail=(
                    "O perfil do usuário autenticado "
                    "não foi encontrado."
                ),
            )

        role_name = (
            role.name.strip()
            if role.name is not None
            else ""
        )

        if not role_name:
            raise HTTPException(
                status_code=(
                    status.HTTP_403_FORBIDDEN
                ),
                detail=(
                    "O perfil do usuário autenticado "
                    "é inválido."
                ),
            )

        if (
            role_name
            not in normalized_allowed_roles
        ):
            raise HTTPException(
                status_code=(
                    status.HTTP_403_FORBIDDEN
                ),
                detail=(
                    "O usuário autenticado não possui "
                    "permissão para realizar esta "
                    "operação."
                ),
            )

        return current_user

    return dependency


AdminUserDependency = Annotated[
    User,
    Depends(
        require_roles(
            ROLE_ADMIN,
        )
    ),
]


AdminOrBuyerUserDependency = Annotated[
    User,
    Depends(
        require_roles(
            ROLE_ADMIN,
            ROLE_BUYER,
        )
    ),
]


AdminOrSellerUserDependency = Annotated[
    User,
    Depends(
        require_roles(
            ROLE_ADMIN,
            ROLE_SELLER,
        )
    ),
]


OperationalUserDependency = Annotated[
    User,
    Depends(
        require_roles(
            ROLE_ADMIN,
            ROLE_BUYER,
            ROLE_SELLER,
        )
    ),
]