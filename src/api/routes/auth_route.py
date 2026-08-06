from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    status,
)
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.user_repository import (
    UserRepository,
)
from src.schemas.auth_schema import (
    LoginRequest,
    LoginResponse,
)
from src.schemas.user_schema import (
    UserResponse,
)
from src.services.auth_service import (
    AuthService,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_auth_service(
    session: SessionDependency,
) -> AuthService:
    """
    Monta o serviço de autenticação
    com seu repositório.
    """

    user_repository = UserRepository(
        session
    )

    return AuthService(
        user_repository=user_repository,
    )


AuthServiceDependency = Annotated[
    AuthService,
    Depends(get_auth_service),
]


def raise_auth_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de autenticação
    em respostas HTTP.
    """

    message = str(error)

    if message == (
        "Username, e-mail ou senha inválidos."
    ):
        raise HTTPException(
            status_code=(
                status.HTTP_401_UNAUTHORIZED
            ),
            detail=message,
            headers={
                "WWW-Authenticate": "Bearer",
            },
        ) from error

    if message == "O usuário está inativo.":
        raise HTTPException(
            status_code=(
                status.HTTP_403_FORBIDDEN
            ),
            detail=message,
        ) from error

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    ) from error


@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
    summary="Autenticar usuário",
)
def login(
    request: Annotated[
        LoginRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: AuthServiceDependency,
) -> LoginResponse:
    """
    Autentica um usuário por username ou e-mail
    e retorna um token JWT de acesso.
    """

    try:
        result = service.authenticate(
            login=request.login,
            password=request.password,
        )

        session.commit()

        session.refresh(
            result.user
        )

        user_response = (
            UserResponse.model_validate(
                result.user
            )
        )

        return LoginResponse(
            access_token=(
                result.access_token
            ),
            token_type=result.token_type,
            user=user_response,
        )

    except ValidationError:
        session.rollback()
        raise

    except ValueError as error:
        session.rollback()

        raise_auth_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise