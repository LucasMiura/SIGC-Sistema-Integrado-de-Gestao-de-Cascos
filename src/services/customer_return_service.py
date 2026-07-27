from src.models.customer_return import CustomerReturn
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import CustomerReturnItem
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.part_repository import PartRepository


class CustomerReturnService:
    """Regras de negócio relacionadas a devoluções de clientes."""

    def __init__(
        self,
        customer_return_repository: CustomerReturnRepository,
        customer_return_item_repository: (
            CustomerReturnItemRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
        outbound_item_repository: OutboundItemRepository,
        part_repository: PartRepository,
    ):
        self.customer_return_repository = (
            customer_return_repository
        )

        self.customer_return_item_repository = (
            customer_return_item_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

        self.outbound_item_repository = (
            outbound_item_repository
        )

        self.part_repository = part_repository

    def create_customer_return(
        self,
        return_type: str,
        reference_number: str,
        customer_name: str,
        created_by: int,
        status: str = "ACTIVE",
        notes: str | None = None,
    ) -> CustomerReturn:
        if not return_type.strip():
            raise ValueError(
                "O tipo de devolução é obrigatório."
            )

        if not reference_number.strip():
            raise ValueError(
                "O número de referência é obrigatório."
            )

        if not customer_name.strip():
            raise ValueError(
                "O nome do cliente é obrigatório."
            )

        customer_return = CustomerReturn(
            return_type=return_type.strip(),
            reference_number=reference_number.strip(),
            customer_name=customer_name.strip(),
            created_by=created_by,
            status=status,
            notes=notes,
        )

        return self.customer_return_repository.add(
            customer_return
        )

    def add_item(
        self,
        customer_return_id: int,
        part_id: int,
        quantity: int,
    ) -> CustomerReturnItem:
        customer_return = (
            self.customer_return_repository.get_by_id(
                customer_return_id
            )
        )

        if customer_return is None:
            raise ValueError(
                "Devolução do cliente não encontrada."
            )

        part = self.part_repository.get_by_id(
            part_id
        )

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade devolvida deve ser maior que zero."
            )

        outbound_items = (
            self.outbound_item_repository.list_by_part(
                part_id
            )
        )

        if not outbound_items:
            raise ValueError(
                "Não existem saídas registradas para esta peça."
            )

        total_outbound_quantity = sum(
            item.quantity
            for item in outbound_items
        )

        total_returned_quantity = 0

        for outbound_item in outbound_items:
            allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            total_returned_quantity += sum(
                allocation.quantity_allocated
                for allocation in allocations
            )

        available_for_return = (
            total_outbound_quantity
            - total_returned_quantity
        )

        if quantity > available_for_return:
            raise ValueError(
                "A quantidade devolvida é maior que a "
                "quantidade disponível para devolução."
            )

        customer_return_item = CustomerReturnItem(
            customer_return_id=customer_return_id,
            part_id=part_id,
            quantity=quantity,
        )

        customer_return_item = (
            self.customer_return_item_repository.add(
                customer_return_item
            )
        )

        remaining_quantity = quantity

        for outbound_item in outbound_items:
            if remaining_quantity <= 0:
                break

            allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            already_returned = sum(
                allocation.quantity_allocated
                for allocation in allocations
            )

            available_from_outbound = (
                outbound_item.quantity
                - already_returned
            )

            if available_from_outbound <= 0:
                continue

            quantity_to_allocate = min(
                available_from_outbound,
                remaining_quantity,
            )

            allocation = CustomerReturnAllocation(
                customer_return_item_id=(
                    customer_return_item.id
                ),
                outbound_item_id=outbound_item.id,
                quantity_allocated=(
                    quantity_to_allocate
                ),
            )

            self.customer_return_allocation_repository.add(
                allocation
            )

            remaining_quantity -= (
                quantity_to_allocate
            )

        if remaining_quantity > 0:
            raise ValueError(
                "Não foi possível alocar toda a quantidade "
                "devolvida às saídas existentes."
            )

        return customer_return_item

    def get_customer_return(
        self,
        customer_return_id: int,
    ) -> CustomerReturn:
        customer_return = (
            self.customer_return_repository.get_by_id(
                customer_return_id
            )
        )

        if customer_return is None:
            raise ValueError(
                "Devolução do cliente não encontrada."
            )

        return customer_return

    def list_customer_returns(
        self,
    ) -> list[CustomerReturn]:
        return self.customer_return_repository.list_all()

    def list_customer_return_items(
        self,
        customer_return_id: int,
    ) -> list[CustomerReturnItem]:
        customer_return = (
            self.customer_return_repository.get_by_id(
                customer_return_id
            )
        )

        if customer_return is None:
            raise ValueError(
                "Devolução do cliente não encontrada."
            )

        return (
            self.customer_return_item_repository
            .list_by_customer_return(
                customer_return_id
            )
        )