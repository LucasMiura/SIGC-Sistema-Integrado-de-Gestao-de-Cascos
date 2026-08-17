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
        purchase_status="RECEIVED",
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


def test_should_return_purchase_tracking_by_invoice() -> None:
    query = Mock(
        spec=PurchaseTrackingQuery
    )

    expected_tracking = (
        create_tracking_dto()
    )

    query.get_by_invoice.return_value = (
        expected_tracking
    )

    service = PurchaseTrackingService(
        query
    )

    result = (
        service
        .get_purchase_tracking_by_invoice(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
        )
    )

    assert result == expected_tracking

    query.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )


def test_should_normalize_invoice_tracking_fields() -> None:
    query = Mock(
        spec=PurchaseTrackingQuery
    )

    expected_tracking = (
        create_tracking_dto()
    )

    query.get_by_invoice.return_value = (
        expected_tracking
    )

    service = PurchaseTrackingService(
        query
    )

    result = (
        service
        .get_purchase_tracking_by_invoice(
            supplier_id=1,
            invoice_number="  NF-12345  ",
            invoice_series="  1  ",
        )
    )

    assert result == expected_tracking

    query.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )


def test_should_normalize_empty_invoice_series_to_none() -> None:
    query = Mock(
        spec=PurchaseTrackingQuery
    )

    expected_tracking = (
        create_tracking_dto()
    )

    query.get_by_invoice.return_value = (
        expected_tracking
    )

    service = PurchaseTrackingService(
        query
    )

    service.get_purchase_tracking_by_invoice(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="   ",
    )

    query.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

def test_should_normalize_empty_invoice_series_to_none() -> None:
    query = Mock(
        spec=PurchaseTrackingQuery
    )

    expected_tracking = (
        create_tracking_dto()
    )

    query.get_by_invoice.return_value = (
        expected_tracking
    )

    service = PurchaseTrackingService(
        query
    )

    service.get_purchase_tracking_by_invoice(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="   ",
    )

    query.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )


def test_should_reject_empty_invoice_number_on_tracking() -> None:
    query = Mock(
        spec=PurchaseTrackingQuery
    )

    service = PurchaseTrackingService(
        query
    )

    with pytest.raises(
        ValueError,
        match=(
            "O número da Nota Fiscal "
            "é obrigatório."
        ),
    ):
        service.get_purchase_tracking_by_invoice(
            supplier_id=1,
            invoice_number="   ",
        )

    query.get_by_invoice.assert_not_called()


def test_should_raise_error_when_invoice_is_not_found() -> None:
    query = Mock(
        spec=PurchaseTrackingQuery
    )

    query.get_by_invoice.return_value = None

    service = PurchaseTrackingService(
        query
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.get_purchase_tracking_by_invoice(
            supplier_id=1,
            invoice_number="NF-INEXISTENTE",
            invoice_series="1",
        )

    query.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-INEXISTENTE",
        invoice_series="1",
    )