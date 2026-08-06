from src.models.supplier_return import SupplierReturn
from src.models.supplier_return_item import (
    SupplierReturnItem,
)
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
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)


class SupplierReturnService:
    """
    Regras de negócio relacionadas às remessas
    de cascos aos fornecedores.
    """

    ALLOWED_STATUSES = {
        "ACTIVE",
        "CANCELLED",
    }

    def __init__(
        self,
        supplier_return_repository: (
            SupplierReturnRepository
        ),
        supplier_return_item_repository: (
            SupplierReturnItemRepository
        ),
        supplier_repository: SupplierRepository,
        purchase_repository: PurchaseRepository,
        purchase_item_repository: (
            PurchaseItemRepository
        ),
        outbound_purchase_allocation_repository: (
            OutboundPurchaseAllocationRepository
        ),
        outbound_transfer_allocation_repository: (
            OutboundTransferAllocationRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
    ) -> None:
        self.supplier_return_repository = (
            supplier_return_repository
        )

        self.supplier_return_item_repository = (
            supplier_return_item_repository
        )

        self.supplier_repository = (
            supplier_repository
        )

        self.purchase_repository = (
            purchase_repository
        )

        self.purchase_item_repository = (
            purchase_item_repository
        )

        self.outbound_purchase_allocation_repository = (
            outbound_purchase_allocation_repository
        )

        self.outbound_transfer_allocation_repository = (
            outbound_transfer_allocation_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

    def create_supplier_return(
        self,
        supplier_id: int,
        dispatch_invoice_number: str,
        issue_date: str,
        created_by: int,
        dispatch_invoice_series: str | None = None,
        status: str = "ACTIVE",
        notes: str | None = None,
    ) -> SupplierReturn:
        if supplier_id <= 0:
            raise ValueError(
                "O identificador do fornecedor deve ser "
                "maior que zero."
            )

        if created_by <= 0:
            raise ValueError(
                "O identificador do usuário deve ser "
                "maior que zero."
            )

        normalized_invoice_number = (
            self._normalize_required_text(
                dispatch_invoice_number,
                (
                    "O número da Nota Fiscal de Simples "
                    "Remessa é obrigatório."
                ),
            )
        )

        normalized_issue_date = (
            self._normalize_required_text(
                issue_date,
                "A data de emissão é obrigatória.",
            )
        )

        normalized_series = (
            self._normalize_optional_text(
                dispatch_invoice_series
            )
        )

        normalized_status = (
            self._normalize_status(
                status
            )
        )

        normalized_notes = (
            self._normalize_optional_text(
                notes
            )
        )

        if normalized_status == "CANCELLED":
            raise ValueError(
                "Uma remessa ao fornecedor não pode ser "
                "criada já cancelada."
            )

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        if not supplier.is_active:
            raise ValueError(
                "O fornecedor informado está inativo."
            )

        existing_supplier_return = (
            self.supplier_return_repository
            .get_by_dispatch_invoice_number(
                normalized_invoice_number
            )
        )

        if existing_supplier_return is not None:
            raise ValueError(
                "Já existe uma remessa cadastrada com esse "
                "número de Nota Fiscal de Simples Remessa."
            )

        supplier_return = SupplierReturn(
            supplier_id=supplier_id,
            dispatch_invoice_number=(
                normalized_invoice_number
            ),
            dispatch_invoice_series=(
                normalized_series
            ),
            issue_date=normalized_issue_date,
            created_by=created_by,
            status=normalized_status,
            notes=normalized_notes,
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
        if supplier_return_id <= 0:
            raise ValueError(
                "O identificador da remessa deve ser "
                "maior que zero."
            )

        if purchase_item_id <= 0:
            raise ValueError(
                "O identificador do item de compra deve ser "
                "maior que zero."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade remetida deve ser "
                "maior que zero."
            )

        supplier_return = (
            self.get_supplier_return(
                supplier_return_id
            )
        )

        if supplier_return.status != "ACTIVE":
            raise ValueError(
                "Não é possível adicionar itens a uma "
                "remessa que não está ativa."
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

        if (
            purchase.supplier_id
            != supplier_return.supplier_id
        ):
            raise ValueError(
                "O item de compra não pertence ao "
                "fornecedor da remessa."
            )

        existing_item = (
            self.supplier_return_item_repository
            .get_by_supplier_return_and_purchase_item(
                supplier_return_id=supplier_return_id,
                purchase_item_id=purchase_item_id,
            )
        )

        if existing_item is not None:
            raise ValueError(
                "Este item de compra já foi adicionado "
                "à remessa."
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

        if available_quantity <= 0:
            raise ValueError(
                "Não existe quantidade disponível para "
                "remessa neste item de compra."
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

        return (
            self.supplier_return_item_repository.add(
                supplier_return_item
            )
        )

    def get_available_quantity(
        self,
        purchase_item_id: int,
    ) -> int:
        if purchase_item_id <= 0:
            raise ValueError(
                "O identificador do item de compra deve ser "
                "maior que zero."
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

        customer_returned_quantity = (
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
            customer_returned_quantity
            - already_dispatched_quantity
        )

        return max(
            available_quantity,
            0,
        )

    def get_supplier_return(
        self,
        supplier_return_id: int,
    ) -> SupplierReturn:
        if supplier_return_id <= 0:
            raise ValueError(
                "O identificador da remessa deve ser "
                "maior que zero."
            )

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
        return (
            self.supplier_return_repository.list_all()
        )

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
        Calcula quantos cascos devolvidos pelos clientes
        pertencem a um item específico de compra.

        A saída consome primeiro itens de transferência
        e somente depois itens de compra. A atribuição
        das devoluções respeita exatamente essa mesma
        ordem de origem.
        """

        target_purchase_allocations = (
            self.outbound_purchase_allocation_repository
            .list_by_purchase_item(
                purchase_item_id
            )
        )

        outbound_item_ids = {
            allocation.outbound_item_id
            for allocation
            in target_purchase_allocations
        }

        total_returned_for_purchase_item = 0

        for outbound_item_id in outbound_item_ids:
            transfer_allocations = (
                self.outbound_transfer_allocation_repository
                .list_by_outbound_item(
                    outbound_item_id
                )
            )

            purchase_allocations = (
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

            # A saída consumiu transferências primeiro.
            # Logo, as primeiras unidades devolvidas também
            # pertencem às origens de transferência.
            for transfer_allocation in transfer_allocations:
                if remaining_returned_quantity <= 0:
                    break

                returned_for_transfer = min(
                    remaining_returned_quantity,
                    transfer_allocation.quantity_allocated,
                )

                remaining_returned_quantity -= (
                    returned_for_transfer
                )

            # Apenas o saldo da devolução que ultrapassou
            # as transferências pode pertencer às compras.
            for purchase_allocation in purchase_allocations:
                if remaining_returned_quantity <= 0:
                    break

                returned_for_purchase = min(
                    remaining_returned_quantity,
                    purchase_allocation.quantity_allocated,
                )

                if (
                    purchase_allocation.purchase_item_id
                    == purchase_item_id
                ):
                    total_returned_for_purchase_item += (
                        returned_for_purchase
                    )

                remaining_returned_quantity -= (
                    returned_for_purchase
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
                    "Um item já cadastrado na remessa não "
                    "possui uma origem de compra válida."
                )

            if (
                existing_purchase_item.purchase_id
                != purchase_id
            ):
                raise ValueError(
                    "Todos os itens da remessa devem "
                    "pertencer à mesma Nota Fiscal "
                    "de compra."
                )

    def _normalize_status(
        self,
        status: str,
    ) -> str:
        normalized_status = (
            self._normalize_required_text(
                status,
                "O status da remessa é obrigatório.",
            )
            .upper()
        )

        if (
            normalized_status
            not in self.ALLOWED_STATUSES
        ):
            raise ValueError(
                "O status da remessa deve ser "
                "ACTIVE ou CANCELLED."
            )

        return normalized_status

    @staticmethod
    def _normalize_required_text(
        value: str,
        error_message: str,
    ) -> str:
        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                error_message
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None