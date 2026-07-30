from src.models.customer_return import CustomerReturn
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import CustomerReturnItem
from src.models.outbound import Outbound
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
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository


class CustomerReturnService:
    """Regras de negócio relacionadas a devoluções de clientes."""

    ALLOWED_RETURN_TYPES = {
        "WORK_ORDER",
        "SALE",
    }

    ALLOWED_STATUSES = {
        "ACTIVE",
        "CANCELLED",
    }

    def __init__(
        self,
        customer_return_repository: CustomerReturnRepository,
        customer_return_item_repository: (
            CustomerReturnItemRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
        outbound_repository: OutboundRepository,
        outbound_item_repository: OutboundItemRepository,
        part_repository: PartRepository,
    ) -> None:
        self.customer_return_repository = (
            customer_return_repository
        )

        self.customer_return_item_repository = (
            customer_return_item_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

        self.outbound_repository = outbound_repository

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
        normalized_return_type = (
            self._normalize_required_text(
                return_type,
                "O tipo de devolução é obrigatório.",
            ).upper()
        )

        normalized_reference_number = (
            self._normalize_required_text(
                reference_number,
                "O número de referência é obrigatório.",
            )
        )

        normalized_customer_name = (
            self._normalize_required_text(
                customer_name,
                "O nome do cliente é obrigatório.",
            )
        )

        normalized_status = (
            self._normalize_required_text(
                status,
                "O status da devolução é obrigatório.",
            ).upper()
        )

        normalized_notes = self._normalize_optional_text(
            notes
        )

        if (
            normalized_return_type
            not in self.ALLOWED_RETURN_TYPES
        ):
            raise ValueError(
                "O tipo de devolução deve ser "
                "WORK_ORDER ou SALE."
            )

        if normalized_status not in self.ALLOWED_STATUSES:
            raise ValueError(
                "O status da devolução deve ser "
                "ACTIVE ou CANCELLED."
            )

        self._get_original_outbound_by_reference(
            normalized_return_type,
            normalized_reference_number,
        )

        customer_return = CustomerReturn(
            return_type=normalized_return_type,
            reference_number=(
                normalized_reference_number
            ),
            customer_name=normalized_customer_name,
            created_by=created_by,
            status=normalized_status,
            notes=normalized_notes,
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

        if customer_return.status != "ACTIVE":
            raise ValueError(
                "Não é possível adicionar itens a uma "
                "devolução que não esteja ativa."
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
                "A quantidade devolvida deve ser "
                "maior que zero."
            )

        outbound = self._get_original_outbound(
            customer_return
        )

        outbound_items = (
            self.outbound_item_repository.list_by_outbound(
                outbound.id
            )
        )

        matching_outbound_items = [
            outbound_item
            for outbound_item in outbound_items
            if outbound_item.part_id == part_id
        ]

        if not matching_outbound_items:
            raise ValueError(
                "A peça não pertence à saída original "
                "informada."
            )

        total_outbound_quantity = sum(
            outbound_item.quantity
            for outbound_item in matching_outbound_items
        )

        total_already_returned = 0

        for outbound_item in matching_outbound_items:
            allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            total_already_returned += sum(
                allocation.quantity_allocated
                for allocation in allocations
            )

        available_quantity = (
            total_outbound_quantity
            - total_already_returned
        )

        if quantity > available_quantity:
            raise ValueError(
                "A quantidade devolvida é superior "
                "à quantidade pendente da saída original."
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

        for outbound_item in matching_outbound_items:
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

            remaining_quantity -= quantity_to_allocate

        if remaining_quantity > 0:
            raise ValueError(
                "Não foi possível alocar toda a quantidade "
                "devolvida à saída original."
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

    def _get_original_outbound(
        self,
        customer_return: CustomerReturn,
    ) -> Outbound:
        return self._get_original_outbound_by_reference(
            customer_return.return_type,
            customer_return.reference_number,
        )

    def _get_original_outbound_by_reference(
        self,
        return_type: str,
        reference_number: str,
    ) -> Outbound:
        normalized_return_type = return_type.strip().upper()
        normalized_reference_number = (
            reference_number.strip()
        )

        if normalized_return_type == "WORK_ORDER":
            outbound = (
                self.outbound_repository
                .get_by_work_order_number(
                    normalized_reference_number
                )
            )
        elif normalized_return_type == "SALE":
            outbound = (
                self.outbound_repository
                .get_by_sales_invoice_number(
                    normalized_reference_number
                )
            )
        else:
            raise ValueError(
                "O tipo de devolução deve ser "
                "WORK_ORDER ou SALE."
            )

        if outbound is None:
            raise ValueError(
                "Saída original não encontrada."
            )

        if outbound.destination_type != (
            normalized_return_type
        ):
            raise ValueError(
                "A referência informada não corresponde "
                "ao tipo de devolução."
            )

        if outbound.status != "ACTIVE":
            raise ValueError(
                "A saída original não está ativa."
            )

        return outbound

    @staticmethod
    def _normalize_required_text(
        value: str,
        error_message: str,
    ) -> str:
        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(error_message)

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None