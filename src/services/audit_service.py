import json
from typing import Any

from src.models.audit_log import AuditLog
from src.repositories.audit_log_repository import (
    AuditLogRepository,
)


class AuditService:
    """
    Centraliza a criação dos registros
    permanentes de auditoria do SIGC.
    """

    def __init__(
        self,
        repository: AuditLogRepository,
    ) -> None:
        self.repository = repository

    def register(
        self,
        *,
        user_id: int,
        action: str,
        module: str,
        entity_type: str,
        entity_id: int,
        description: str | None = None,
        old_values: dict[str, Any] | None = None,
        new_values: dict[str, Any] | None = None,
        justification: str | None = None,
    ) -> AuditLog:
        """
        Registra um novo evento de auditoria.

        O histórico é somente de inclusão:
        registros existentes não são alterados
        nem removidos por este serviço.
        """

        self._validate_positive_id(
            user_id,
            (
                "O identificador do usuário "
                "da auditoria deve ser maior que zero."
            ),
        )

        self._validate_positive_id(
            entity_id,
            (
                "O identificador da entidade "
                "auditada deve ser maior que zero."
            ),
        )

        normalized_action = (
            self._normalize_required_text(
                action,
                "A ação da auditoria é obrigatória.",
            )
        )

        normalized_module = (
            self._normalize_required_text(
                module,
                "O módulo da auditoria é obrigatório.",
            )
        )

        normalized_entity_type = (
            self._normalize_required_text(
                entity_type,
                (
                    "O tipo da entidade auditada "
                    "é obrigatório."
                ),
            )
        )

        normalized_description = (
            self._normalize_optional_text(
                description
            )
        )

        normalized_justification = (
            self._normalize_optional_text(
                justification
            )
        )

        audit_log = AuditLog(
            user_id=user_id,
            action=normalized_action,
            module=normalized_module,
            entity_type=normalized_entity_type,
            entity_id=entity_id,
            description=normalized_description,
            old_values=self._serialize_values(
                old_values
            ),
            new_values=self._serialize_values(
                new_values
            ),
            justification=normalized_justification,
        )

        return self.repository.add(
            audit_log
        )

    def get_by_id(
        self,
        audit_log_id: int,
    ) -> AuditLog:
        """
        Busca obrigatoriamente um registro
        de auditoria.
        """

        self._validate_positive_id(
            audit_log_id,
            (
                "O identificador da auditoria "
                "deve ser maior que zero."
            ),
        )

        audit_log = self.repository.get_by_id(
            audit_log_id
        )

        if audit_log is None:
            raise ValueError(
                "Registro de auditoria não encontrado."
            )

        return audit_log

    def list_by_user(
        self,
        user_id: int,
    ) -> list[AuditLog]:
        """Lista auditorias de um usuário."""

        self._validate_positive_id(
            user_id,
            (
                "O identificador do usuário "
                "deve ser maior que zero."
            ),
        )

        return self.repository.list_by_user(
            user_id
        )

    def list_by_entity(
        self,
        *,
        entity_type: str,
        entity_id: int,
    ) -> list[AuditLog]:
        """
        Lista o histórico de uma determinada
        entidade do sistema.
        """

        normalized_entity_type = (
            self._normalize_required_text(
                entity_type,
                (
                    "O tipo da entidade auditada "
                    "é obrigatório."
                ),
            )
        )

        self._validate_positive_id(
            entity_id,
            (
                "O identificador da entidade "
                "auditada deve ser maior que zero."
            ),
        )

        return self.repository.list_by_entity(
            normalized_entity_type,
            entity_id,
        )

    def list_by_module(
        self,
        module: str,
    ) -> list[AuditLog]:
        """Lista auditorias de um módulo."""

        normalized_module = (
            self._normalize_required_text(
                module,
                "O módulo da auditoria é obrigatório.",
            )
        )

        return self.repository.list_by_module(
            normalized_module
        )

    @staticmethod
    def _serialize_values(
        values: dict[str, Any] | None,
    ) -> str | None:
        """
        Converte os valores históricos para JSON
        com representação determinística.
        """

        if values is None:
            return None

        return json.dumps(
            values,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        )

    @staticmethod
    def _validate_positive_id(
        value: int,
        message: str,
    ) -> None:
        """Valida um identificador positivo."""

        if (
            not isinstance(value, int)
            or isinstance(value, bool)
            or value <= 0
        ):
            raise ValueError(
                message
            )

    @staticmethod
    def _normalize_required_text(
        value: str,
        empty_message: str,
    ) -> str:
        """Normaliza um texto obrigatório."""

        if not isinstance(value, str):
            raise ValueError(
                empty_message
            )

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                empty_message
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """Normaliza um texto opcional."""

        if value is None:
            return None

        if not isinstance(value, str):
            raise ValueError(
                "O texto informado é inválido."
            )

        normalized_value = value.strip()

        return normalized_value or None