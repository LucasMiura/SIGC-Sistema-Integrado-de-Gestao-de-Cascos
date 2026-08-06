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
from src.schemas.role_schema import (
    RoleCreateRequest,
    RoleResponse,
)
from src.services.role_service import (
    RoleService,
)


router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_role_service(
    session: SessionDependency,
) -> RoleService:
    """
    Monta o serviço de perfis de acesso
    com seu repositório.
    """

    repository = RoleRepository(
        session
    )

    return RoleService(
        repository
    )


RoleServiceDependency = Annotated[
    RoleService,
    Depends(get_role_service),
]


def raise_role_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio dos perfis
    em respostas HTTP.
    """

    message = str(error)

    if message == "Perfil de acesso não encontrado.":
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    if message == (
        "Já existe um perfil com este nome."
    ):
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
    response_model=RoleResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar perfil de acesso",
)
def create_role(
    request: Annotated[
        RoleCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: RoleServiceDependency,
) -> RoleResponse:
    """
    Cadastra um novo perfil de acesso.
    """

    try:
        role = service.create(
            name=request.name,
            description=request.description,
        )

        session.commit()
        session.refresh(
            role
        )

        return RoleResponse.model_validate(
            role
        )

    except ValueError as error:
        session.rollback()

        raise_role_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[RoleResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar perfis de acesso",
)
def list_roles(
    service: RoleServiceDependency,
) -> list[RoleResponse]:
    """
    Lista todos os perfis cadastrados.
    """

    roles = service.list_all()

    return [
        RoleResponse.model_validate(
            role
        )
        for role in roles
    ]


@router.get(
    "/{role_id}",
    response_model=RoleResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar perfil de acesso",
)
def get_role(
    service: RoleServiceDependency,
    role_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do perfil de acesso"
        ),
    ),
) -> RoleResponse:
    """
    Consulta um perfil pelo identificador.
    """

    role = service.get_by_id(
        role_id
    )

    if role is None:
        raise_role_http_exception(
            ValueError(
                "Perfil de acesso não encontrado."
            )
        )

    return RoleResponse.model_validate(
        role
    )