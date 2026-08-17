from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
)
from src.api.dependencies.audit import (
    AuditServiceDependency,
)
from src.database.connection import get_session
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.part_schema import (
    PartCreateRequest,
    PartDeactivateRequest,
    PartResponse,
    PartUpdateRequest,
)
from src.services.part_service import (
    PartService,
)


router = APIRouter(
    prefix="/parts",
    tags=["Parts"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_part_service(
    session: SessionDependency,
) -> PartService:
    """
    Cria o serviço de peças
    com suas dependências.
    """

    part_repository = PartRepository(
        session
    )

    supplier_repository = SupplierRepository(
        session
    )

    return PartService(
        part_repository=part_repository,
        supplier_repository=supplier_repository,
    )


PartServiceDependency = Annotated[
    PartService,
    Depends(get_part_service),
]


def raise_part_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio
    em respostas HTTP.
    """

    message = str(error)

    not_found_messages = {
        "Peça não encontrada.",
        "Fornecedor não encontrado.",
    }

    if message in not_found_messages:
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    if message == (
        "Já existe uma peça com este código "
        "para o fornecedor informado."
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
    response_model=PartResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar peça",
)
def create_part(
    request: Annotated[
        PartCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PartServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    audit_service: AuditServiceDependency,
) -> PartResponse:
    """
    Cadastra uma peça controlada pelo SIGC.
    """

    try:
        part = service.create(
            supplier_id=request.supplier_id,
            part_code=request.part_code,
            name=request.name,
            description=request.description,
            return_deadline_days=(
                request.return_deadline_days
            ),
        )

        audit_service.register(
            user_id=current_user.id,
            action="CREATE",
            module="PART",
            entity_type="Part",
            entity_id=part.id,
            description="Peça cadastrada.",
            new_values={
                "supplier_id": part.supplier_id,
                "part_code": part.part_code,
                "name": part.name,
                "description": part.description,
                "return_deadline_days": (
                    part.return_deadline_days
                ),
                "is_active": part.is_active,
            },
        )

        session.commit()

        session.refresh(
            part
        )

        return PartResponse.model_validate(
            part
        )

    except ValueError as error:
        session.rollback()

        raise_part_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[PartResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar peças",
)
def list_parts(
    service: PartServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra as peças pelo identificador "
            "do fornecedor"
        ),
    ),
) -> list[PartResponse]:
    """
    Lista todas as peças ou filtra
    por fornecedor.
    """

    try:
        if supplier_id is None:
            parts = service.list_all()

        else:
            parts = service.list_by_supplier(
                supplier_id
            )

        return [
            PartResponse.model_validate(
                part
            )
            for part in parts
        ]

    except ValueError as error:
        raise_part_http_exception(
            error
        )


@router.get(
    "/{part_id}",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar peça",
)
def get_part(
    service: PartServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """
    Consulta uma peça pelo identificador.
    """

    try:
        part = service.get_required(
            part_id
        )

        return PartResponse.model_validate(
            part
        )

    except ValueError as error:
        raise_part_http_exception(
            error
        )


@router.patch(
    "/{part_id}",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar peça",
)
def update_part(
    request: Annotated[
        PartUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PartServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    audit_service: AuditServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """
    Atualiza parcialmente uma peça existente.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True
        )

        old_values = None

        if update_data:
            existing_part = service.get_required(
                part_id
            )

            old_values = {
                field: getattr(
                    existing_part,
                    field,
                )
                for field in update_data
            }

        part = service.update(
            part_id=part_id,
            **update_data,
        )

        if update_data:
            new_values = {
                field: getattr(
                    part,
                    field,
                )
                for field in update_data
            }

            audit_service.register(
                user_id=current_user.id,
                action="UPDATE",
                module="PART",
                entity_type="Part",
                entity_id=part.id,
                description="Peça atualizada.",
                old_values=old_values,
                new_values=new_values,
            )

        session.commit()

        session.refresh(
            part
        )

        return PartResponse.model_validate(
            part
        )

    except ValueError as error:
        session.rollback()

        raise_part_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{part_id}/activate",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar peça",
)
def activate_part(
    session: SessionDependency,
    service: PartServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    audit_service: AuditServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """
    Ativa uma peça inativa.
    """

    try:
        part = service.activate(
            part_id
        )

        audit_service.register(
            user_id=current_user.id,
            action="ACTIVATE",
            module="PART",
            entity_type="Part",
            entity_id=part.id,
            description="Peça ativada.",
            old_values={
                "is_active": 0,
            },
            new_values={
                "is_active": 1,
            },
        )

        session.commit()

        session.refresh(
            part
        )

        return PartResponse.model_validate(
            part
        )

    except ValueError as error:
        session.rollback()

        raise_part_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{part_id}/deactivate",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar peça",
)
def deactivate_part(
    request: Annotated[
        PartDeactivateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PartServiceDependency,
    current_user: AdminOrBuyerUserDependency,
    audit_service: AuditServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """
    Desativa uma peça ativa.
    """

    try:
        part = service.deactivate(
            part_id
        )

        audit_service.register(
            user_id=current_user.id,
            action="DEACTIVATE",
            module="PART",
            entity_type="Part",
            entity_id=part.id,
            description="Peça desativada.",
            old_values={
                "is_active": 1,
            },
            new_values={
                "is_active": 0,
            },
            justification=(
                request.justification
            ),
        )

        session.commit()

        session.refresh(
            part
        )

        return PartResponse.model_validate(
            part
        )

    except ValueError as error:
        session.rollback()

        raise_part_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise