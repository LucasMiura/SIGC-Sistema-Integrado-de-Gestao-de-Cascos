from datetime import (
    date,
    timedelta,
)
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from sqlalchemy.orm import Session

from src.queries.dashboard_query import (
    DashboardQuery,
)


@pytest.fixture
def query() -> DashboardQuery:
    """
    Cria a Query com sessão simulada.
    """

    return DashboardQuery(
        Mock(
            spec=Session
        )
    )


@pytest.mark.parametrize(
    (
        "days_remaining",
        "expected_status",
    ),
    [
        (
            31,
            "NORMAL",
        ),
        (
            30,
            "ATTENTION",
        ),
        (
            8,
            "ATTENTION",
        ),
        (
            7,
            "URGENT",
        ),
        (
            0,
            "URGENT",
        ),
        (
            -1,
            "OVERDUE",
        ),
    ],
)
def test_should_resolve_deadline_status(
    query: DashboardQuery,
    days_remaining: int,
    expected_status: str,
) -> None:
    today = date.today()

    deadline_date = (
        today
        + timedelta(
            days=days_remaining
        )
    )

    result = (
        query
        ._resolve_deadline_status(
            deadline_date=deadline_date,
            today=today,
        )
    )

    assert result == expected_status


def test_should_build_purchase_dashboard_indicators(
    query: DashboardQuery,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    today = date.today()

    purchase_item = SimpleNamespace(
        id=10,
        quantity_purchased=10,
        quantity_available=2,
    )

    purchase = SimpleNamespace(
        id=1,
        issue_date=today.isoformat(),
    )

    part = SimpleNamespace(
        id=20,
        supplier_id=5,
        return_deadline_days=40,
    )

    supplier = SimpleNamespace(
        id=5,
    )

    monkeypatch.setattr(
        query,
        "_get_purchase_rows",
        Mock(
            return_value=[
                (
                    purchase_item,
                    purchase,
                    part,
                    supplier,
                )
            ]
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_rows",
        Mock(
            return_value=[]
        ),
    )

    monkeypatch.setattr(
        query,
        (
            "_get_outbound_and_"
            "customer_return_quantities"
        ),
        Mock(
            return_value=(
                {
                    10: 8,
                },
                {},
                {
                    10: 5,
                },
                {},
            )
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_supplier_return_quantities",
        Mock(
            return_value={
                10: 2,
            }
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_return_quantities",
        Mock(
            return_value={}
        ),
    )

    result = query.get_summary()

    assert result.total_origin_count == 1
    assert result.total_available_quantity == 2

    assert (
        result.deadline.normal_quantity
        == 8
    )

    assert (
        result.deadline.attention_quantity
        == 0
    )

    assert (
        result.deadline.urgent_quantity
        == 0
    )

    assert (
        result.deadline.overdue_quantity
        == 0
    )

    assert (
        result.customer_returns
        .outbound_quantity
        == 8
    )

    assert (
        result.customer_returns
        .returned_quantity
        == 5
    )

    assert (
        result.customer_returns
        .pending_quantity
        == 3
    )

    assert (
        result.customer_returns
        .pending_origin_count
        == 0
    )

    assert (
        result.customer_returns
        .partial_origin_count
        == 1
    )

    assert (
        result.customer_returns
        .completed_origin_count
        == 0
    )

    assert (
        result.supplier_returns
        .available_quantity
        == 3
    )

    assert (
        result.supplier_returns
        .returned_quantity
        == 2
    )

    assert (
        result.supplier_returns
        .pending_quantity
        == 8
    )

    assert (
        result.transfer_returns
        .pending_quantity
        == 0
    )


def test_should_build_transfer_dashboard_indicators(
    query: DashboardQuery,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    today = date.today()

    transfer_item = SimpleNamespace(
        id=30,
        quantity=8,
        quantity_available=1,
        return_deadline_days=5,
    )

    transfer = SimpleNamespace(
        id=2,
        issue_date=today.isoformat(),
    )

    part = SimpleNamespace(
        id=40,
        supplier_id=5,
    )

    monkeypatch.setattr(
        query,
        "_get_purchase_rows",
        Mock(
            return_value=[]
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_rows",
        Mock(
            return_value=[
                (
                    transfer_item,
                    transfer,
                    part,
                )
            ]
        ),
    )

    monkeypatch.setattr(
        query,
        (
            "_get_outbound_and_"
            "customer_return_quantities"
        ),
        Mock(
            return_value=(
                {},
                {
                    30: 6,
                },
                {},
                {
                    30: 4,
                },
            )
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_supplier_return_quantities",
        Mock(
            return_value={}
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_return_quantities",
        Mock(
            return_value={
                30: 3,
            }
        ),
    )

    result = query.get_summary()

    assert result.total_origin_count == 1
    assert result.total_available_quantity == 1

    assert (
        result.deadline.urgent_quantity
        == 5
    )

    assert (
        result.customer_returns
        .outbound_quantity
        == 6
    )

    assert (
        result.customer_returns
        .returned_quantity
        == 4
    )

    assert (
        result.customer_returns
        .pending_quantity
        == 2
    )

    assert (
        result.customer_returns
        .partial_origin_count
        == 1
    )

    assert (
        result.transfer_returns
        .available_quantity
        == 1
    )

    assert (
        result.transfer_returns
        .returned_quantity
        == 3
    )

    assert (
        result.transfer_returns
        .pending_quantity
        == 5
    )


def test_should_exclude_origin_when_deadline_filter_does_not_match(
    query: DashboardQuery,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    today = date.today()

    purchase_item = SimpleNamespace(
        id=10,
        quantity_purchased=10,
        quantity_available=10,
    )

    purchase = SimpleNamespace(
        id=1,
        issue_date=today.isoformat(),
    )

    part = SimpleNamespace(
        id=20,
        supplier_id=5,
        return_deadline_days=60,
    )

    supplier = SimpleNamespace(
        id=5,
    )

    monkeypatch.setattr(
        query,
        "_get_purchase_rows",
        Mock(
            return_value=[
                (
                    purchase_item,
                    purchase,
                    part,
                    supplier,
                )
            ]
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_rows",
        Mock(
            return_value=[]
        ),
    )

    monkeypatch.setattr(
        query,
        (
            "_get_outbound_and_"
            "customer_return_quantities"
        ),
        Mock(
            return_value=(
                {},
                {},
                {},
                {},
            )
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_supplier_return_quantities",
        Mock(
            return_value={}
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_return_quantities",
        Mock(
            return_value={}
        ),
    )

    result = query.get_summary(
        deadline_status="URGENT"
    )

    assert result.total_origin_count == 0
    assert result.total_available_quantity == 0

    assert (
        result.deadline.normal_quantity
        == 0
    )

    assert (
        result.deadline.urgent_quantity
        == 0
    )