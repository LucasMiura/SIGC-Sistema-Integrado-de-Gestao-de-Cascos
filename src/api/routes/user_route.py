from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.role_repository import (
    RoleRepository,
)
from src.repositories.user_repository import (
    UserRepository,
)
from src.schemas.user_schema import (
    UserChangePasswordRequest,
    UserCreateRequest,
    UserResetPasswordRequest,
    UserResponse,
    UserUpdateRequest,
)
from src.services.user_service import (
    UserService,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_user_service(
    session: SessionDependency,
) -> UserService:
    """
    Monta o serviço de usuários
    com seus repositórios.
    """

    user_repository = UserRepository(
        session
    )

    role_repository = RoleRepository(
        session
    )

    return UserService(
        repository=user_repository,
        role_repository=role_repository,
    )


UserServiceDependency = Annotated[
    UserService,
    Depends(get_user_service),
]


NOT_FOUND_MESSAGES = {
    "Usuário não encontrado.",
    "Perfil de acesso não encontrado.",
}


CONFLICT_MESSAGES = {
    (
        "Já existe um usuário com este "
        "username."
    ),
    (
        "Já existe um usuário com este "
        "e-mail."
    ),
}


def raise_user_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio dos usuários
    em respostas HTTP.
    """

    message = str(error)

    if message in NOT_FOUND_MESSAGES:
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    if message in CONFLICT_MESSAGES:
        raise HTTPException(
            status_code=(
                status.HTTP_409_CONFLICT
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
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar usuário",
)
def create_user(
    request: Annotated[
        UserCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: UserServiceDependency,
) -> UserResponse:
    """
    Cadastra um novo usuário ativo.

    A senha é transformada em hash pelo service
    e nunca é devolvida na resposta da API.
    """

    try:
        user = service.create(
            full_name=request.full_name,
            username=request.username,
            email=request.email,
            password=request.password,
            role_id=request.role_id,
        )

        session.commit()
        session.refresh(
            user
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        session.rollback()

        raise_user_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar usuários",
)
def list_users(
    service: UserServiceDependency,
) -> list[UserResponse]:
    """
    Lista usuários ativos e inativos.

    Usuários históricos não são excluídos
    fisicamente do SIGC.
    """

    users = service.list_all()

    return [
        UserResponse.model_validate(
            user
        )
        for user in users
    ]


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar usuário",
)
def get_user(
    service: UserServiceDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário"
        ),
    ),
) -> UserResponse:
    """
    Consulta um usuário pelo identificador.
    """

    try:
        user = service.get_required(
            user_id
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        raise_user_http_exception(
            error
        )


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar usuário",
)
def update_user(
    request: Annotated[
        UserUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: UserServiceDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário"
        ),
    ),
) -> UserResponse:
    """
    Atualiza somente os campos enviados.

    A senha não pode ser modificada por esta
    operação.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True,
        )

        user = service.update(
            user_id,
            **update_data,
        )

        session.commit()
        session.refresh(
            user
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        session.rollback()

        raise_user_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{user_id}/activate",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar usuário",
)
def activate_user(
    session: SessionDependency,
    service: UserServiceDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário"
        ),
    ),
) -> UserResponse:
    """
    Reativa um usuário inativo.
    """

    try:
        user = service.activate(
            user_id
        )

        session.commit()
        session.refresh(
            user
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        session.rollback()

        raise_user_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{user_id}/deactivate",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar usuário",
)
def deactivate_user(
    session: SessionDependency,
    service: UserServiceDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário"
        ),
    ),
) -> UserResponse:
    """
    Desativa um usuário sem excluir
    seu histórico.
    """

    try:
        user = service.deactivate(
            user_id
        )

        session.commit()
        session.refresh(
            user
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        session.rollback()

        raise_user_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{user_id}/reset-password",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Redefinir senha do usuário",
)
def reset_user_password(
    request: Annotated[
        UserResetPasswordRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: UserServiceDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário"
        ),
    ),
) -> UserResponse:
    """
    Redefine administrativamente a senha.

    A autorização para esta operação será
    adicionada posteriormente.
    """

    try:
        user = service.reset_password(
            user_id=user_id,
            new_password=(
                request.new_password
            ),
        )

        session.commit()
        session.refresh(
            user
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        session.rollback()

        raise_user_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{user_id}/change-password",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Alterar própria senha",
)
def change_user_password(
    request: Annotated[
        UserChangePasswordRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: UserServiceDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário"
        ),
    ),
) -> UserResponse:
    """
    Altera a senha mediante confirmação
    da senha atual.

    Após a implementação da autenticação,
    o identificador será obtido do usuário
    autenticado, e não livremente informado.
    """

    try:
        user = service.change_password(
            user_id=user_id,
            current_password=(
                request.current_password
            ),
            new_password=(
                request.new_password
            ),
        )

        session.commit()
        session.refresh(
            user
        )

        return UserResponse.model_validate(
            user
        )

    except ValueError as error:
        session.rollback()

        raise_user_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise