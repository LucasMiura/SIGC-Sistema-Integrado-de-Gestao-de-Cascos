from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.audit_log_repository import (
    AuditLogRepository,
)
from src.services.audit_service import AuditService


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_audit_service(
    session: SessionDependency,
) -> AuditService:
    """
    Monta o serviço central de auditoria
    utilizando a mesma sessão da operação.
    """

    repository = AuditLogRepository(
        session
    )

    return AuditService(
        repository
    )


AuditServiceDependency = Annotated[
    AuditService,
    Depends(get_audit_service),
]