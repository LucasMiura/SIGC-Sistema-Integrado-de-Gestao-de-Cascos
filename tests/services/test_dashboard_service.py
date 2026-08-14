from unittest.mock import Mock

import pytest

from src.dtos.dashboard import (
    DashboardCustomerReturnIndicatorsDTO,
    DashboardDeadlineIndicatorsDTO,
    DashboardSummaryDTO,
    DashboardSupplierReturnIndicatorsDTO,
    DashboardTransferReturnIndicatorsDTO,
)
from src.queries.dashboard_query import (
    DashboardQuery,
)
from src.services.dashboard_service import (
    DashboardService,
)


def create_summary_dto() -> DashboardSummaryDTO:
    """
    Cria um resumo simulado para os testes.
    """

    return DashboardSummaryDTO(
        total_origin_count=10,
        total_available_quantity=30,
        deadline=(
            DashboardDeadlineIndicatorsDTO(
                normal_quantity=10,
                attention_quantity=8,
                urgent_quantity=5,
                overdue_quantity=2,
            )
        ),
        customer_returns=(
            DashboardCustomerReturnIndicatorsDTO(
                outbound_quantity=20,
                returned_quantity=12,
                pending_quantity=8,
                pending_origin_count=2,
                partial_origin_count=1,
                completed_origin_count=3,
            )
        ),
        supplier_returns=(
            DashboardSupplierReturnIndicatorsDTO(
                available_quantity=7,
                returned_quantity=5,
                pending_quantity=15,
            )
        ),
        transfer_returns=(
            DashboardTransferReturnIndicatorsDTO(
                available_quantity=3,
                returned_quantity=4,
                pending_quantity=6,
            )
        ),
    )


def test_should_return_dashboard_summary() -> None:
    query = Mock(
        spec=DashboardQuery
    )

    expected = create_summary_dto()

    query.get_summary.return_value = (
        expected
    )

    service = DashboardService(
        query
    )

    result = service.get_summary()

    assert result == expected

    query.get_summary.assert_called_once_with(
        supplier_id=None,
        part_id=None,
        origin_type=None,
        deadline_status=None,
        date_from=None,
        date_to=None,
    )


def test_should_normalize_dashboard_filters() -> None:
    query = Mock(
        spec=DashboardQuery
    )

    query.get_summary.return_value = (
        create_summary_dto()
    )

    service = DashboardService(
        query
    )

    service.get_summary(
        supplier_id=10,
        part_id=20,
        origin_type="  purchase  ",
        deadline_status="  urgent  ",
        date_from=" 2026-08-01 ",
        date_to=" 2026-08-31 ",
    )

    query.get_summary.assert_called_once_with(
        supplier_id=10,
        part_id=20,
        origin_type="PURCHASE",
        deadline_status="URGENT",
        date_from="2026-08-01",
        date_to="2026-08-31",
    )


@pytest.mark.parametrize(
    (
        "supplier_id",
        "part_id",
        "expected_message",
    ),
    [
        (
            0,
            None,
            (
                "O identificador do fornecedor "
                "deve ser maior que zero."
            ),
        ),
        (
            None,
            0,
            (
                "O identificador da peça "
                "deve ser maior que zero."
            ),
        ),
    ],
)
def test_should_reject_invalid_identifiers(
    supplier_id: int | None,
    part_id: int | None,
    expected_message: str,
) -> None:
    query = Mock(
        spec=DashboardQuery
    )

    service = DashboardService(
        query
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.get_summary(
            supplier_id=supplier_id,
            part_id=part_id,
        )

    query.get_summary.assert_not_called()


def test_should_reject_invalid_origin_type() -> None:
    query = Mock(
        spec=DashboardQuery
    )

    service = DashboardService(
        query
    )

    with pytest.raises(
        ValueError,
        match=(
            "A origem deve ser "
            "PURCHASE ou TRANSFER."
        ),
    ):
        service.get_summary(
            origin_type="OUTBOUND"
        )

    query.get_summary.assert_not_called()


def test_should_reject_invalid_deadline_status() -> None:
    query = Mock(
        spec=DashboardQuery
    )

    service = DashboardService(
        query
    )

    with pytest.raises(
        ValueError,
        match=(
            "O status de prazo deve ser "
            "NORMAL, ATTENTION, URGENT "
            "ou OVERDUE."
        ),
    ):
        service.get_summary(
            deadline_status="INVALID"
        )

    query.get_summary.assert_not_called()


@pytest.mark.parametrize(
    (
        "field",
        "value",
        "expected_message",
    ),
    [
        (
            "date_from",
            "01/08/2026",
            (
                "A data inicial deve estar "
                "no formato YYYY-MM-DD."
            ),
        ),
        (
            "date_to",
            "31/08/2026",
            (
                "A data final deve estar "
                "no formato YYYY-MM-DD."
            ),
        ),
    ],
)
def test_should_reject_invalid_date_format(
    field: str,
    value: str,
    expected_message: str,
) -> None:
    query = Mock(
        spec=DashboardQuery
    )

    service = DashboardService(
        query
    )

    kwargs = {
        field: value,
    }

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.get_summary(
            **kwargs
        )

    query.get_summary.assert_not_called()


def test_should_reject_inverted_date_range() -> None:
    query = Mock(
        spec=DashboardQuery
    )

    service = DashboardService(
        query
    )

    with pytest.raises(
        ValueError,
        match=(
            "A data inicial não pode ser "
            "posterior à data final."
        ),
    ):
        service.get_summary(
            date_from="2026-08-31",
            date_to="2026-08-01",
        )

    query.get_summary.assert_not_called()


def test_should_convert_blank_optional_filters_to_none() -> None:
    query = Mock(
        spec=DashboardQuery
    )

    query.get_summary.return_value = (
        create_summary_dto()
    )

    service = DashboardService(
        query
    )

    service.get_summary(
        origin_type="   ",
        deadline_status="   ",
        date_from="   ",
        date_to="   ",
    )

    query.get_summary.assert_called_once_with(
        supplier_id=None,
        part_id=None,
        origin_type=None,
        deadline_status=None,
        date_from=None,
        date_to=None,
    )