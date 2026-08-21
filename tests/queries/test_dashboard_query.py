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


def test_should_build_stock_position_by_part(
    query: DashboardQuery,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    part = SimpleNamespace(
        id=20,
        supplier_id=5,
        part_code="ABC123",
        name="Compressor de ar",
    )

    purchase_item = SimpleNamespace(
        id=10,
        quantity_available=4,
    )

    purchase = SimpleNamespace(
        id=1,
    )

    supplier = SimpleNamespace(
        id=5,
    )

    transfer_item = SimpleNamespace(
        id=30,
        quantity_available=2,
    )

    transfer = SimpleNamespace(
        id=2,
    )

    workshop_item = SimpleNamespace(
        id=100,
        part_id=20,
        quantity=5,
    )

    workshop_outbound = (
        SimpleNamespace(
            id=50,
            destination_type=(
                "WORK_ORDER"
            ),
        )
    )

    sale_item = SimpleNamespace(
        id=101,
        part_id=20,
        quantity=4,
    )

    sale_outbound = (
        SimpleNamespace(
            id=51,
            destination_type="SALE",
        )
    )

    query.session.scalars.return_value.all.return_value = [
        part
    ]

    query.session.execute.return_value.all.return_value = [
        (
            workshop_item,
            workshop_outbound,
        ),
        (
            sale_item,
            sale_outbound,
        ),
    ]

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
            "_get_customer_return_"
            "quantities_by_outbound"
        ),
        Mock(
            return_value={
                100: 2,
                101: 1,
            }
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
                {
                    10: 2,
                },
                {
                    30: 1,
                },
            )
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_supplier_return_quantities",
        Mock(
            return_value={
                10: 1,
            }
        ),
    )

    monkeypatch.setattr(
        query,
        "_get_transfer_return_quantities",
        Mock(
            return_value={
                30: 0,
            }
        ),
    )

    result = (
        query.get_stock_position()
    )

    assert len(result) == 1

    item = result[0]

    assert item.part_id == 20
    assert item.part_code == "ABC123"

    assert item.stock_quantity == 6

    assert (
        item.workshop_pending_quantity
        == 3
    )

    assert (
        item.customer_pending_quantity
        == 3
    )

    assert (
        item.workshop_returned_quantity
        == 2
    )

    assert (
        item.customer_returned_quantity
        == 1
    )

    assert (
        item.available_core_quantity
        == 2
    )