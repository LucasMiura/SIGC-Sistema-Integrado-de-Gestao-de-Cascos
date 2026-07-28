from collections import defaultdict

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.dtos.purchase_tracking import (
    PurchaseItemTrackingDTO,
    PurchaseTrackingDTO,
)
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.models.supplier import Supplier
from src.models.supplier_return_item import SupplierReturnItem


class PurchaseTrackingQuery:
    """Monta visões de acompanhamento sem alterar o banco."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_purchase_id(
        self,
        purchase_id: int,
    ) -> PurchaseTrackingDTO | None:
        header_statement = (
            select(Purchase, Supplier)
            .join(Supplier, Supplier.id == Purchase.supplier_id)
            .where(Purchase.id == purchase_id)
        )
        header = self.session.execute(header_statement).one_or_none()

        if header is None:
            return None

        purchase, supplier = header

        item_statement = (
            select(PurchaseItem, Part)
            .join(Part, Part.id == PurchaseItem.part_id)
            .where(PurchaseItem.purchase_id == purchase_id)
            .order_by(PurchaseItem.id)
        )
        item_rows = self.session.execute(item_statement).all()

        purchase_item_ids = [
            purchase_item.id
            for purchase_item, _part in item_rows
        ]

        outbound_by_purchase_item = self._get_outbound_quantities(
            purchase_item_ids
        )
        returned_by_purchase_item = (
            self._get_customer_returned_quantities(
                purchase_item_ids
            )
        )
        supplier_returned_by_purchase_item = (
            self._get_supplier_returned_quantities(
                purchase_item_ids
            )
        )

        items = tuple(
            self._build_item_dto(
                purchase_item=purchase_item,
                part=part,
                quantity_outbound=outbound_by_purchase_item.get(
                    purchase_item.id,
                    0,
                ),
                quantity_returned_by_customer=(
                    returned_by_purchase_item.get(
                        purchase_item.id,
                        0,
                    )
                ),
                quantity_returned_to_supplier=(
                    supplier_returned_by_purchase_item.get(
                        purchase_item.id,
                        0,
                    )
                ),
            )
            for purchase_item, part in item_rows
        )

        return PurchaseTrackingDTO(
            purchase_id=purchase.id,
            supplier_id=supplier.id,
            supplier_name=supplier.name,
            invoice_number=purchase.invoice_number,
            invoice_series=purchase.invoice_series,
            issue_date=purchase.issue_date,
            purchase_status=purchase.status,
            items=items,
        )

    def _get_outbound_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        if not purchase_item_ids:
            return {}

        statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.purchase_item_id.in_(
                    purchase_item_ids
                )
            )
            .order_by(OutboundPurchaseAllocation.id)
        )
        allocations = self.session.scalars(statement).all()

        quantities: dict[int, int] = defaultdict(int)
        for allocation in allocations:
            quantities[allocation.purchase_item_id] += (
                allocation.quantity_allocated
            )

        return dict(quantities)

    def _get_customer_returned_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        """
        Redistribui as devoluções de clientes pelas origens FIFO
        preservadas em outbound_purchase_allocations.
        """
        if not purchase_item_ids:
            return {}

        outbound_statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.purchase_item_id.in_(
                    purchase_item_ids
                )
            )
            .order_by(
                OutboundPurchaseAllocation.outbound_item_id,
                OutboundPurchaseAllocation.id,
            )
        )
        target_allocations = self.session.scalars(
            outbound_statement
        ).all()

        outbound_item_ids = {
            allocation.outbound_item_id
            for allocation in target_allocations
        }
        if not outbound_item_ids:
            return {}

        all_outbound_statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.outbound_item_id.in_(
                    outbound_item_ids
                )
            )
            .order_by(
                OutboundPurchaseAllocation.outbound_item_id,
                OutboundPurchaseAllocation.id,
            )
        )
        all_outbound_allocations = self.session.scalars(
            all_outbound_statement
        ).all()

        return_statement = (
            select(CustomerReturnAllocation)
            .where(
                CustomerReturnAllocation.outbound_item_id.in_(
                    outbound_item_ids
                )
            )
            .order_by(
                CustomerReturnAllocation.outbound_item_id,
                CustomerReturnAllocation.id,
            )
        )
        customer_returns = self.session.scalars(
            return_statement
        ).all()

        allocations_by_outbound: dict[
            int,
            list[OutboundPurchaseAllocation],
        ] = defaultdict(list)
        for allocation in all_outbound_allocations:
            allocations_by_outbound[
                allocation.outbound_item_id
            ].append(allocation)

        returned_by_outbound: dict[int, int] = defaultdict(int)
        for allocation in customer_returns:
            returned_by_outbound[allocation.outbound_item_id] += (
                allocation.quantity_allocated
            )

        target_ids = set(purchase_item_ids)
        quantities: dict[int, int] = defaultdict(int)

        for outbound_item_id, allocations in (
            allocations_by_outbound.items()
        ):
            remaining = returned_by_outbound.get(
                outbound_item_id,
                0,
            )

            for allocation in allocations:
                if remaining <= 0:
                    break

                allocated_return = min(
                    remaining,
                    allocation.quantity_allocated,
                )

                if allocation.purchase_item_id in target_ids:
                    quantities[allocation.purchase_item_id] += (
                        allocated_return
                    )

                remaining -= allocated_return

        return dict(quantities)

    def _get_supplier_returned_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        if not purchase_item_ids:
            return {}

        statement = (
            select(SupplierReturnItem)
            .where(
                SupplierReturnItem.purchase_item_id.in_(
                    purchase_item_ids
                )
            )
            .order_by(SupplierReturnItem.id)
        )
        items = self.session.scalars(statement).all()

        quantities: dict[int, int] = defaultdict(int)
        for item in items:
            quantities[item.purchase_item_id] += item.quantity

        return dict(quantities)

    @staticmethod
    def _build_item_dto(
        purchase_item: PurchaseItem,
        part: Part,
        quantity_outbound: int,
        quantity_returned_by_customer: int,
        quantity_returned_to_supplier: int,
    ) -> PurchaseItemTrackingDTO:
        pending_customer = max(
            quantity_outbound - quantity_returned_by_customer,
            0,
        )
        available_supplier = max(
            quantity_returned_by_customer
            - quantity_returned_to_supplier,
            0,
        )
        pending_supplier = max(
            purchase_item.quantity_purchased
            - quantity_returned_to_supplier,
            0,
        )

        status = PurchaseTrackingQuery._resolve_lifecycle_status(
            quantity_purchased=purchase_item.quantity_purchased,
            quantity_outbound=quantity_outbound,
            quantity_returned_by_customer=(
                quantity_returned_by_customer
            ),
            quantity_returned_to_supplier=(
                quantity_returned_to_supplier
            ),
        )

        return PurchaseItemTrackingDTO(
            purchase_item_id=purchase_item.id,
            part_id=part.id,
            part_code=part.part_code,
            part_name=part.name,
            quantity_purchased=purchase_item.quantity_purchased,
            quantity_available_for_outbound=(
                purchase_item.quantity_available
            ),
            quantity_outbound=quantity_outbound,
            quantity_returned_by_customer=(
                quantity_returned_by_customer
            ),
            quantity_pending_customer_return=pending_customer,
            quantity_available_for_supplier_return=(
                available_supplier
            ),
            quantity_returned_to_supplier=(
                quantity_returned_to_supplier
            ),
            quantity_pending_supplier_return=pending_supplier,
            lifecycle_status=status,
        )

    @staticmethod
    def _resolve_lifecycle_status(
        quantity_purchased: int,
        quantity_outbound: int,
        quantity_returned_by_customer: int,
        quantity_returned_to_supplier: int,
    ) -> str:
        if quantity_returned_to_supplier >= quantity_purchased:
            return "COMPLETED"

        if quantity_returned_to_supplier > 0:
            return "PARTIALLY_RETURNED_TO_SUPPLIER"

        if quantity_returned_by_customer >= quantity_outbound > 0:
            return "AVAILABLE_FOR_SUPPLIER_RETURN"

        if quantity_returned_by_customer > 0:
            return "PARTIALLY_RETURNED_BY_CUSTOMER"

        if quantity_outbound > 0:
            return "PENDING_CUSTOMER_RETURN"

        return "AVAILABLE_FOR_OUTBOUND"
