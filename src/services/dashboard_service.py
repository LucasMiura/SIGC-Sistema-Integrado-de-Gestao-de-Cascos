from datetime import date

from src.dtos.dashboard import (
    DashboardSummaryDTO,
)
from src.queries.dashboard_query import (
    DashboardQuery,
)


class DashboardService:
    """
    Regras de entrada e validação dos
    filtros utilizados pelo dashboard.
    """

    ALLOWED_ORIGIN_TYPES = {
        "PURCHASE",
        "TRANSFER",
    }

    ALLOWED_DEADLINE_STATUSES = {
        "NORMAL",
        "ATTENTION",
        "URGENT",
        "OVERDUE",
    }

    def __init__(
        self,
        query: DashboardQuery,
    ) -> None:
        self.query = query

    def get_summary(
        self,
        *,
        supplier_id: int | None = None,
        part_id: int | None = None,
        origin_type: str | None = None,
        deadline_status: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> DashboardSummaryDTO:
        """
        Retorna o resumo geral do dashboard.
        """

        if (
            supplier_id is not None
            and supplier_id <= 0
        ):
            raise ValueError(
                "O identificador do fornecedor "
                "deve ser maior que zero."
            )

        if (
            part_id is not None
            and part_id <= 0
        ):
            raise ValueError(
                "O identificador da peça "
                "deve ser maior que zero."
            )

        normalized_origin_type = (
            self._normalize_optional_upper_text(
                origin_type
            )
        )

        if (
            normalized_origin_type is not None
            and normalized_origin_type
            not in self.ALLOWED_ORIGIN_TYPES
        ):
            raise ValueError(
                "A origem deve ser "
                "PURCHASE ou TRANSFER."
            )

        normalized_deadline_status = (
            self._normalize_optional_upper_text(
                deadline_status
            )
        )

        if (
            normalized_deadline_status is not None
            and normalized_deadline_status
            not in self.ALLOWED_DEADLINE_STATUSES
        ):
            raise ValueError(
                "O status de prazo deve ser "
                "NORMAL, ATTENTION, URGENT "
                "ou OVERDUE."
            )

        normalized_date_from = (
            self._normalize_optional_date(
                date_from,
                field_name="data inicial",
            )
        )

        normalized_date_to = (
            self._normalize_optional_date(
                date_to,
                field_name="data final",
            )
        )

        if (
            normalized_date_from is not None
            and normalized_date_to is not None
            and normalized_date_from
            > normalized_date_to
        ):
            raise ValueError(
                "A data inicial não pode ser "
                "posterior à data final."
            )

        return self.query.get_summary(
            supplier_id=supplier_id,
            part_id=part_id,
            origin_type=(
                normalized_origin_type
            ),
            deadline_status=(
                normalized_deadline_status
            ),
            date_from=normalized_date_from,
            date_to=normalized_date_to,
        )

    @staticmethod
    def _normalize_optional_upper_text(
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized_value = (
            value.strip().upper()
        )

        return normalized_value or None

    @staticmethod
    def _normalize_optional_date(
        value: str | None,
        *,
        field_name: str,
    ) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        try:
            parsed_date = date.fromisoformat(
                normalized_value
            )

        except ValueError as error:
            raise ValueError(
                f"A {field_name} deve estar "
                "no formato YYYY-MM-DD."
            ) from error

        return parsed_date.isoformat()