from typing import NoReturn

from fastapi import (
    APIRouter,
    HTTPException,
    Path,
    status,
)

from src.api.dependencies.authorization import (
    AdminUserDependency,
)
from src.schemas.audit_schema import (
    AuditLogResponse,
)
from src.api.dependencies.audit import (
    AuditServiceDependency,
)


router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit"],
)


def raise_audit_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio da auditoria
    em respostas HTTP.
    """

    message = str(error)

    if message == (
        "Registro de auditoria não encontrado."
    ):
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    ) from error


@router.get(
    "/by-user/{user_id}",
    response_model=list[AuditLogResponse],
    status_code=status.HTTP_200_OK,
    summary="Consultar auditoria por usuário",
)
def list_audit_logs_by_user(
    service: AuditServiceDependency,
    _current_user: AdminUserDependency,
    user_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do usuário responsável"
        ),
    ),
) -> list[AuditLogResponse]:
    """
    Lista registros de auditoria associados
    a determinado usuário.

    Operação exclusiva do Administrador Master.
    """

    try:
        audit_logs = service.list_by_user(
            user_id
        )

        return [
            AuditLogResponse.model_validate(
                audit_log
            )
            for audit_log in audit_logs
        ]

    except ValueError as error:
        raise_audit_http_exception(
            error
        )


@router.get(
    "/by-module/{module}",
    response_model=list[AuditLogResponse],
    status_code=status.HTTP_200_OK,
    summary="Consultar auditoria por módulo",
)
def list_audit_logs_by_module(
    service: AuditServiceDependency,
    _current_user: AdminUserDependency,
    module: str = Path(
        ...,
        min_length=1,
        max_length=100,
        description=(
            "Módulo do sistema auditado"
        ),
    ),
) -> list[AuditLogResponse]:
    """
    Lista os registros pertencentes
    a determinado módulo.

    Operação exclusiva do Administrador Master.
    """

    try:
        audit_logs = service.list_by_module(
            module
        )

        return [
            AuditLogResponse.model_validate(
                audit_log
            )
            for audit_log in audit_logs
        ]

    except ValueError as error:
        raise_audit_http_exception(
            error
        )


@router.get(
    (
        "/by-entity/"
        "{entity_type}/"
        "{entity_id}"
    ),
    response_model=list[AuditLogResponse],
    status_code=status.HTTP_200_OK,
    summary="Consultar histórico de uma entidade",
)
def list_audit_logs_by_entity(
    service: AuditServiceDependency,
    _current_user: AdminUserDependency,
    entity_type: str = Path(
        ...,
        min_length=1,
        max_length=100,
        description=(
            "Tipo da entidade auditada"
        ),
    ),
    entity_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da entidade auditada"
        ),
    ),
) -> list[AuditLogResponse]:
    """
    Retorna o histórico de uma entidade
    específica do SIGC.

    Operação exclusiva do Administrador Master.
    """

    try:
        audit_logs = service.list_by_entity(
            entity_type=entity_type,
            entity_id=entity_id,
        )

        return [
            AuditLogResponse.model_validate(
                audit_log
            )
            for audit_log in audit_logs
        ]

    except ValueError as error:
        raise_audit_http_exception(
            error
        )


@router.get(
    "/{audit_log_id}",
    response_model=AuditLogResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar registro de auditoria",
)
def get_audit_log(
    service: AuditServiceDependency,
    _current_user: AdminUserDependency,
    audit_log_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador do registro de auditoria"
        ),
    ),
) -> AuditLogResponse:
    """
    Consulta um registro específico
    de auditoria.

    Operação exclusiva do Administrador Master.
    """

    try:
        audit_log = service.get_by_id(
            audit_log_id
        )

        return AuditLogResponse.model_validate(
            audit_log
        )

    except ValueError as error:
        raise_audit_http_exception(
            error
        )