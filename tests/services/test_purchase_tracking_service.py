from unittest.mock import Mock

import pytest

from src.dtos.purchase_tracking import PurchaseTrackingDTO
from src.queries.purchase_tracking_query import PurchaseTrackingQuery
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)


def create_tracking_dto() -> PurchaseTrackingDTO:
    """Cria um DTO de acompanhamento para os testes."""

    return PurchaseTrackingDTO(
        purchase_id=1,
        supplier_id=1,
        supplier_name="Fornecedor Teste",
        invoice_number="12345",
        invoice_series="1",
        issue_date="2026-07-28",
        purchase_status="ACTIVE",
        items=(),
    )


def test_should_return_purchase_tracking() -> None:
    query = Mock(spec=PurchaseTrackingQuery)
    expected_tracking = create_tracking_dto()

    query.get_by_purchase_id.return_value = expected_tracking

    service = PurchaseTrackingService(query)

    result = service.get_purchase_tracking(1)

    assert result == expected_tracking

    query.get_by_purchase_id.assert_called_once_with(1)


def test_should_reject_non_positive_purchase_id() -> None:
    query = Mock(spec=PurchaseTrackingQuery)
    service = PurchaseTrackingService(query)

    with pytest.raises(
        ValueError,
        match="O identificador da compra deve ser maior que zero.",
    ):
        service.get_purchase_tracking(0)

    query.get_by_purchase_id.assert_not_called()


def test_should_raise_error_when_purchase_is_not_found() -> None:
    query = Mock(spec=PurchaseTrackingQuery)
    query.get_by_purchase_id.return_value = None

    service = PurchaseTrackingService(query)

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.get_purchase_tracking(999)

    query.get_by_purchase_id.assert_called_once_with(999)