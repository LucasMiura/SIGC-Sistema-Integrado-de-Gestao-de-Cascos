from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)


class OutboundService:
    """Regras de negócio relacionadas a saídas."""

    def __init__(
        self,
        outbound_repository: OutboundRepository,
        outbound_item_repository: OutboundItemRepository,
        outbound_purchase_allocation_repository: (
            OutboundPurchaseAllocationRepository
        ),
        purchase_item_repository: PurchaseItemRepository,
        part_repository: PartRepository,
    ):
        self.outbound_repository = outbound_repository
        self.outbound_item_repository = (
            outbound_item_repository
        )
        self.outbound_purchase_allocation_repository = (
            outbound_purchase_allocation_repository
        )
        self.purchase_item_repository = (
            purchase_item_repository
        )
        self.part_repository = part_repository

    def create_outbound(
        self,
        destination_type: str,
        created_by: int,
        work_order_number: str | None = None,
        sales_invoice_number: str | None = None,
        status: str = "ACTIVE",
    ) -> Outbound:
        if not destination_type.strip():
            raise ValueError(
                "O tipo de destino é obrigatório."
            )

        if work_order_number is None and (
            sales_invoice_number is None
        ):
            raise ValueError(
                "A saída deve possuir uma ordem de serviço "
                "ou uma nota fiscal de venda."
            )

        outbound = Outbound(
            destination_type=destination_type.strip(),
            work_order_number=work_order_number,
            sales_invoice_number=sales_invoice_number,
            created_by=created_by,
            status=status,
        )

        return self.outbound_repository.add(outbound)

    def add_item(
        self,
        outbound_id: int,
        part_id: int,
        quantity: int,
    ) -> OutboundItem:
        outbound = self.outbound_repository.get_by_id(
            outbound_id
        )

        if outbound is None:
            raise ValueError(
                "Saída não encontrada."
            )

        part = self.part_repository.get_by_id(part_id)

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade da saída deve ser maior que zero."
            )

        available_purchase_items = (
            self.purchase_item_repository.list_available_by_part(
                part_id
            )
        )

        total_available = sum(
            item.quantity_available
            for item in available_purchase_items
        )

        if total_available < quantity:
            raise ValueError(
                "Quantidade disponível insuficiente "
                "para a saída."
            )

        outbound_item = OutboundItem(
            outbound_id=outbound_id,
            part_id=part_id,
            quantity=quantity,
        )

        outbound_item = (
            self.outbound_item_repository.add(
                outbound_item
            )
        )

        remaining_quantity = quantity

        for purchase_item in available_purchase_items:
            if remaining_quantity <= 0:
                break

            quantity_to_allocate = min(
                purchase_item.quantity_available,
                remaining_quantity,
            )

            purchase_item.quantity_available -= (
                quantity_to_allocate
            )

            allocation = OutboundPurchaseAllocation(
                outbound_item_id=outbound_item.id,
                purchase_item_id=purchase_item.id,
                quantity_allocated=quantity_to_allocate,
            )

            self.outbound_purchase_allocation_repository.add(
                allocation
            )

            remaining_quantity -= quantity_to_allocate

        return outbound_item

    def get_outbound(
        self,
        outbound_id: int,
    ) -> Outbound:
        outbound = self.outbound_repository.get_by_id(
            outbound_id
        )

        if outbound is None:
            raise ValueError(
                "Saída não encontrada."
            )

        return outbound

    def list_outbounds(self) -> list[Outbound]:
        return self.outbound_repository.list_all()

    def list_outbound_items(
        self,
        outbound_id: int,
    ) -> list[OutboundItem]:
        outbound = self.outbound_repository.get_by_id(
            outbound_id
        )

        if outbound is None:
            raise ValueError(
                "Saída não encontrada."
            )

        return self.outbound_item_repository.list_by_outbound(
            outbound_id
        )