from typing import Literal

from pydantic import BaseModel, ConfigDict

from src.schemas.purchase_schema import (
    PurchaseStatus,
)

from src.dtos.purchase_tracking import (
    PurchaseItemTrackingDTO,
    PurchaseTrackingDTO,
)


PurchaseItemLifecycleStatus = Literal[
    "AVAILABLE_FOR_OUTBOUND",
    "PENDING_CUSTOMER_RETURN",
    "PARTIALLY_RETURNED_BY_CUSTOMER",
    "AVAILABLE_FOR_SUPPLIER_RETURN",
    "PARTIALLY_RETURNED_TO_SUPPLIER",
    "COMPLETED",
]

class PurchaseItemTrackingResponse(BaseModel):
    """Representa um item no acompanhamento de uma compra."""

    model_config = ConfigDict(frozen=True)

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

    lifecycle_status: PurchaseItemLifecycleStatus

    @classmethod
    def from_dto(
        cls,
        dto: PurchaseItemTrackingDTO,
    ) -> "PurchaseItemTrackingResponse":
        """Converte um DTO de item para um schema de resposta."""

        return cls(
            purchase_item_id=dto.purchase_item_id,
            part_id=dto.part_id,
            part_code=dto.part_code,
            part_name=dto.part_name,
            quantity_purchased=dto.quantity_purchased,
            quantity_available_for_outbound=(
                dto.quantity_available_for_outbound
            ),
            quantity_outbound=dto.quantity_outbound,
            quantity_returned_by_customer=(
                dto.quantity_returned_by_customer
            ),
            quantity_pending_customer_return=(
                dto.quantity_pending_customer_return
            ),
            quantity_available_for_supplier_return=(
                dto.quantity_available_for_supplier_return
            ),
            quantity_returned_to_supplier=(
                dto.quantity_returned_to_supplier
            ),
            quantity_pending_supplier_return=(
                dto.quantity_pending_supplier_return
            ),
            lifecycle_status=dto.lifecycle_status,
        )


class PurchaseTrackingResponse(BaseModel):
    """Representa o acompanhamento consolidado de uma compra."""

    model_config = ConfigDict(frozen=True)

    purchase_id: int

    supplier_id: int
    supplier_name: str

    invoice_number: str
    invoice_series: str | None
    issue_date: str
    purchase_status: PurchaseStatus

    items: tuple[PurchaseItemTrackingResponse, ...]

    @classmethod
    def from_dto(
        cls,
        dto: PurchaseTrackingDTO,
    ) -> "PurchaseTrackingResponse":
        """Converte o DTO consolidado para uma resposta da API."""

        return cls(
            purchase_id=dto.purchase_id,
            supplier_id=dto.supplier_id,
            supplier_name=dto.supplier_name,
            invoice_number=dto.invoice_number,
            invoice_series=dto.invoice_series,
            issue_date=dto.issue_date,
            purchase_status=dto.purchase_status,
            items=tuple(
                PurchaseItemTrackingResponse.from_dto(item)
                for item in dto.items
            ),
        )