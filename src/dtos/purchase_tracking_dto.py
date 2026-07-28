from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PurchaseTrackingDTO:
    """Dados consolidados de acompanhamento de um item de compra."""

    purchase_item_id: int
    purchase_id: int

    invoice_number: str
    invoice_series: str | None
    issue_date: str
    purchase_status: str

    supplier_id: int
    supplier_name: str

    part_id: int
    part_code: str
    part_name: str

    quantity_purchased: int
    quantity_available: int
    quantity_sent: int

    quantity_customer_returned: int
    quantity_pending_customer_return: int

    quantity_available_supplier_return: int
    quantity_supplier_returned: int

    quantity_pending_completion: int
    tracking_status: str