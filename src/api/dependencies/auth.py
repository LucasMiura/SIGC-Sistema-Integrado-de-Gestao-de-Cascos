from typing import Annotated

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.models.user import User
from src.repositories.user_repository import (
    UserRepository,
)
from src.security.token import (
    ExpiredTokenError,
    InvalidAccessTokenError,
    decode_access_token,
)


bearer_scheme = HTTPBearer(
    auto_error=False,
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


BearerCredentialsDependency = Annotated[
    HTTPAuthorizationCredentials | None,
    Depends(bearer_scheme),
]


def raise_invalid_authentication(
    detail: str = "Token de acesso inválido.",
) -> None:
    """
    Retorna uma resposta padronizada para
    falhas de autenticação.
    """

    raise HTTPException(
        status_code=(
            status.HTTP_401_UNAUTHORIZED
        ),
        detail=detail,
        headers={
            "WWW-Authenticate": "Bearer",
        },
    )


def get_current_user(
    credentials: BearerCredentialsDependency,
    session: SessionDependency,
) -> User:
    """
    Identifica o usuário autenticado
    através do token Bearer.

    O usuário é consultado novamente no banco
    para que alterações de status tenham efeito
    imediatamente.
    """

    if credentials is None:
        raise_invalid_authentication(
            "Token de acesso não informado."
        )

    token = credentials.credentials

    try:
        payload = decode_access_token(
            token
        )

    except ExpiredTokenError:
        raise_invalid_authentication(
            "Token de acesso expirado."
        )

    except InvalidAccessTokenError:
        raise_invalid_authentication(
            "Token de acesso inválido."
        )

    user_id = payload["user_id"]

    repository = UserRepository(
        session
    )

    user = repository.get_by_id(
        user_id
    )

    if user is None:
        raise_invalid_authentication(
            "Usuário autenticado não encontrado."
        )

    if not user.is_active:
        raise HTTPException(
            status_code=(
                status.HTTP_403_FORBIDDEN
            ),
            detail=(
                "O usuário autenticado está inativo."
            ),
        )

    return user


CurrentUserDependency = Annotated[
    User,
    Depends(get_current_user),
]