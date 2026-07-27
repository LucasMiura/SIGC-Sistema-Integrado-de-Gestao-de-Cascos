from src.models.supplier_return import SupplierReturn
from src.models.supplier_return_item import SupplierReturnItem
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)


class SupplierReturnService:
    """Regras de negócio das remessas de cascos aos fornecedores."""

    def __init__(
        self,
        supplier_return_repository: SupplierReturnRepository,
        supplier_return_item_repository: (
            SupplierReturnItemRepository
        ),
        supplier_repository: SupplierRepository,
        purchase_repository: PurchaseRepository,
        purchase_item_repository: PurchaseItemRepository,
        outbound_purchase_allocation_repository: (
            OutboundPurchaseAllocationRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
    ):
        self.supplier_return_repository = (
            supplier_return_repository
        )

        self.supplier_return_item_repository = (
            supplier_return_item_repository
        )

        self.supplier_repository = supplier_repository
        self.purchase_repository = purchase_repository

        self.purchase_item_repository = (
            purchase_item_repository
        )

        self.outbound_purchase_allocation_repository = (
            outbound_purchase_allocation_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

    def create_supplier_return(
        self,
        supplier_id: int,
        dispatch_invoice_number: str,
        dispatch_invoice_series: str | None,
        issue_date: str,
        created_by: int,
        status: str = "ACTIVE",
        notes: str | None = None,
    ) -> SupplierReturn:
        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        normalized_invoice_number = (
            dispatch_invoice_number.strip()
        )

        if not normalized_invoice_number:
            raise ValueError(
                "O número da Nota Fiscal de Simples "
                "Remessa é obrigatório."
            )

        if not issue_date.strip():
            raise ValueError(
                "A data da remessa é obrigatória."
            )

        existing_supplier_return = (
            self.supplier_return_repository
            .get_by_dispatch_invoice_number(
                normalized_invoice_number
            )
        )

        if existing_supplier_return is not None:
            raise ValueError(
                "Já existe uma remessa cadastrada com "
                "este número de Nota Fiscal."
            )

        normalized_series = None

        if dispatch_invoice_series is not None:
            normalized_series = (
                dispatch_invoice_series.strip() or None
            )

        supplier_return = SupplierReturn(
            supplier_id=supplier_id,
            dispatch_invoice_number=(
                normalized_invoice_number
            ),
            dispatch_invoice_series=normalized_series,
            issue_date=issue_date.strip(),
            created_by=created_by,
            status=status.strip() or "ACTIVE",
            notes=notes,
        )

        return self.supplier_return_repository.add(
            supplier_return
        )

    def add_item(
        self,
        supplier_return_id: int,
        purchase_item_id: int,
        quantity: int,
    ) -> SupplierReturnItem:
        supplier_return = (
            self.supplier_return_repository.get_by_id(
                supplier_return_id
            )
        )

        if supplier_return is None:
            raise ValueError(
                "Remessa ao fornecedor não encontrada."
            )

        purchase_item = (
            self.purchase_item_repository.get_by_id(
                purchase_item_id
            )
        )

        if purchase_item is None:
            raise ValueError(
                "Item de compra não encontrado."
            )

        purchase = self.purchase_repository.get_by_id(
            purchase_item.purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra de origem não encontrada."
            )

        if purchase.supplier_id != supplier_return.supplier_id:
            raise ValueError(
                "O item de compra não pertence ao fornecedor "
                "da remessa."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade remetida deve ser maior que zero."
            )

        self._validate_same_purchase(
            supplier_return_id=supplier_return_id,
            purchase_id=purchase.id,
        )

        available_quantity = (
            self.get_available_quantity(
                purchase_item_id
            )
        )

        if quantity > available_quantity:
            raise ValueError(
                "A quantidade remetida é maior que a "
                "quantidade disponível para remessa. "
                f"Quantidade máxima permitida: "
                f"{available_quantity}."
            )

        supplier_return_item = SupplierReturnItem(
            supplier_return_id=supplier_return_id,
            purchase_item_id=purchase_item_id,
            quantity=quantity,
        )

        return self.supplier_return_item_repository.add(
            supplier_return_item
        )

    def get_available_quantity(
        self,
        purchase_item_id: int,
    ) -> int:
        purchase_item = (
            self.purchase_item_repository.get_by_id(
                purchase_item_id
            )
        )

        if purchase_item is None:
            raise ValueError(
                "Item de compra não encontrado."
            )

        received_quantity = (
            self._get_customer_returned_quantity(
                purchase_item_id
            )
        )

        already_dispatched_quantity = (
            self.supplier_return_item_repository
            .get_returned_quantity_by_purchase_item(
                purchase_item_id
            )
        )

        available_quantity = (
            received_quantity
            - already_dispatched_quantity
        )

        return max(available_quantity, 0)

    def get_supplier_return(
        self,
        supplier_return_id: int,
    ) -> SupplierReturn:
        supplier_return = (
            self.supplier_return_repository.get_by_id(
                supplier_return_id
            )
        )

        if supplier_return is None:
            raise ValueError(
                "Remessa ao fornecedor não encontrada."
            )

        return supplier_return

    def list_supplier_returns(
        self,
    ) -> list[SupplierReturn]:
        return self.supplier_return_repository.list_all()

    def list_items(
        self,
        supplier_return_id: int,
    ) -> list[SupplierReturnItem]:
        self.get_supplier_return(
            supplier_return_id
        )

        return (
            self.supplier_return_item_repository
            .list_by_supplier_return(
                supplier_return_id
            )
        )

    def _get_customer_returned_quantity(
        self,
        purchase_item_id: int,
    ) -> int:
        """
        Calcula quantos cascos já retornaram dos clientes
        para uma origem específica de compra.

        A devolução do cliente está ligada ao OutboundItem.
        Portanto, a quantidade devolvida é redistribuída
        sobre as origens FIFO daquele OutboundItem.
        """

        target_allocations = (
            self.outbound_purchase_allocation_repository
            .list_by_purchase_item(
                purchase_item_id
            )
        )

        total_returned_for_purchase_item = 0

        for target_allocation in target_allocations:
            outbound_item_id = (
                target_allocation.outbound_item_id
            )

            outbound_allocations = (
                self.outbound_purchase_allocation_repository
                .list_by_outbound_item(
                    outbound_item_id
                )
            )

            customer_return_allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item_id
                )
            )

            remaining_returned_quantity = sum(
                allocation.quantity_allocated
                for allocation
                in customer_return_allocations
            )

            for outbound_allocation in outbound_allocations:
                if remaining_returned_quantity <= 0:
                    break

                quantity_returned_for_allocation = min(
                    remaining_returned_quantity,
                    outbound_allocation.quantity_allocated,
                )

                if (
                    outbound_allocation.id
                    == target_allocation.id
                ):
                    total_returned_for_purchase_item += (
                        quantity_returned_for_allocation
                    )

                remaining_returned_quantity -= (
                    quantity_returned_for_allocation
                )

        return total_returned_for_purchase_item

    def _validate_same_purchase(
        self,
        supplier_return_id: int,
        purchase_id: int,
    ) -> None:
        existing_items = (
            self.supplier_return_item_repository
            .list_by_supplier_return(
                supplier_return_id
            )
        )

        for existing_item in existing_items:
            existing_purchase_item = (
                self.purchase_item_repository.get_by_id(
                    existing_item.purchase_item_id
                )
            )

            if existing_purchase_item is None:
                raise ValueError(
                    "Um item existente da remessa possui "
                    "origem de compra inválida."
                )

            if existing_purchase_item.purchase_id != purchase_id:
                raise ValueError(
                    "Todos os itens de uma remessa devem "
                    "pertencer à mesma Nota Fiscal de compra."
                )