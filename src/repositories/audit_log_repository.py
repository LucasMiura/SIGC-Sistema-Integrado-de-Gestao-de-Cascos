from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.audit_log import AuditLog


class AuditLogRepository:
    """Responsável pela persistência do histórico de auditoria."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        audit_log_id: int,
    ) -> AuditLog | None:
        statement = select(AuditLog).where(
            AuditLog.id == audit_log_id
        )
        return self.session.scalar(statement)

    def list_by_user(
        self,
        user_id: int,
    ) -> list[AuditLog]:
        statement = (
            select(AuditLog)
            .where(AuditLog.user_id == user_id)
            .order_by(
                AuditLog.created_at,
                AuditLog.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def list_by_entity(
        self,
        entity_type: str,
        entity_id: int,
    ) -> list[AuditLog]:
        statement = (
            select(AuditLog)
            .where(
                AuditLog.entity_type == entity_type,
                AuditLog.entity_id == entity_id,
            )
            .order_by(
                AuditLog.created_at,
                AuditLog.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def list_by_module(
        self,
        module: str,
    ) -> list[AuditLog]:
        statement = (
            select(AuditLog)
            .where(AuditLog.module == module)
            .order_by(
                AuditLog.created_at,
                AuditLog.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        audit_log: AuditLog,
    ) -> AuditLog:
        self.session.add(audit_log)
        self.session.flush()
        return audit_log