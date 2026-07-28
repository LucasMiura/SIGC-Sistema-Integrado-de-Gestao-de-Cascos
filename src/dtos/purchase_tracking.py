from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PurchaseItemTrackingDTO:
    """Visão consolidada do ciclo de um item de compra."""

    purchase_item_id: int
    part_id: int
    part_code: str
    part_name: str
    quantity_purchased: int
    quantity_available_for_outbound: int
    quantity_outbound: int
    quantity_returned_by_customer: int
    quantity_pending_customer_return: int
    quantity_available_for_supplier_return: int
    quantity_returned_to_supplier: int
    quantity_pending_supplier_return: int
    lifecycle_status: str


@dataclass(frozen=True, slots=True)
class PurchaseTrackingDTO:
    """Visão consolidada de uma compra e de seus itens."""

    purchase_id: int
    supplier_id: int
    supplier_name: str
    invoice_number: str
    invoice_series: str | None
    issue_date: str
    purchase_status: str
    items: tuple[PurchaseItemTrackingDTO, ...]
