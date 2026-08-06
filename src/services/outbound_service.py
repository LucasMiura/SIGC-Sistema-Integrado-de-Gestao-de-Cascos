from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.outbound_transfer_allocation import (
    OutboundTransferAllocation,
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
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)


class OutboundService:
    """Regras de negócio relacionadas às saídas de estoque."""

    ALLOWED_STATUSES = {
        "ACTIVE",
        "CANCELLED",
    }

    def __init__(
        self,
        outbound_repository: OutboundRepository,
        outbound_item_repository: OutboundItemRepository,
        outbound_purchase_allocation_repository: (
            OutboundPurchaseAllocationRepository
        ),
        outbound_transfer_allocation_repository: (
            OutboundTransferAllocationRepository
        ),
        purchase_item_repository: PurchaseItemRepository,
        transfer_item_repository: TransferItemRepository,
        part_repository: PartRepository,
    ) -> None:
        self.outbound_repository = outbound_repository

        self.outbound_item_repository = (
            outbound_item_repository
        )

        self.outbound_purchase_allocation_repository = (
            outbound_purchase_allocation_repository
        )

        self.outbound_transfer_allocation_repository = (
            outbound_transfer_allocation_repository
        )

        self.purchase_item_repository = (
            purchase_item_repository
        )

        self.transfer_item_repository = (
            transfer_item_repository
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
        normalized_destination_type = (
            self._normalize_required_text(
                destination_type,
                "O tipo de destino é obrigatório.",
            )
        )

        normalized_work_order_number = (
            self._normalize_optional_text(
                work_order_number
            )
        )

        normalized_sales_invoice_number = (
            self._normalize_optional_text(
                sales_invoice_number
            )
        )

        normalized_status = self._normalize_status(
            status
        )

        if created_by <= 0:
            raise ValueError(
                "O identificador do usuário deve ser "
                "maior que zero."
            )

        self._validate_reference_numbers(
            work_order_number=(
                normalized_work_order_number
            ),
            sales_invoice_number=(
                normalized_sales_invoice_number
            ),
        )

        if normalized_status == "CANCELLED":
            raise ValueError(
                "Uma saída não pode ser criada "
                "já cancelada."
            )

        self._ensure_work_order_is_unique(
            work_order_number=(
                normalized_work_order_number
            ),
        )

        self._ensure_sales_invoice_is_unique(
            sales_invoice_number=(
                normalized_sales_invoice_number
            ),
        )

        outbound = Outbound(
            destination_type=(
                normalized_destination_type
            ),
            work_order_number=(
                normalized_work_order_number
            ),
            sales_invoice_number=(
                normalized_sales_invoice_number
            ),
            created_by=created_by,
            status=normalized_status,
        )

        return self.outbound_repository.add(
            outbound
        )

    def add_item(
        self,
        outbound_id: int,
        part_id: int,
        quantity: int,
    ) -> OutboundItem:
        if outbound_id <= 0:
            raise ValueError(
                "O identificador da saída deve ser "
                "maior que zero."
            )

        if part_id <= 0:
            raise ValueError(
                "O identificador da peça deve ser "
                "maior que zero."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade da saída deve ser "
                "maior que zero."
            )

        outbound = self.outbound_repository.get_by_id(
            outbound_id
        )

        if outbound is None:
            raise ValueError(
                "Saída não encontrada."
            )

        if outbound.status == "CANCELLED":
            raise ValueError(
                "Não é possível adicionar itens a uma "
                "saída cancelada."
            )

        part = self.part_repository.get_by_id(
            part_id
        )

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if not part.is_active:
            raise ValueError(
                "Não é possível realizar a saída "
                "de uma peça inativa."
            )

        existing_outbound_items = (
            self.outbound_item_repository
            .list_by_outbound(
                outbound_id
            )
        )

        if any(
            outbound_item.part_id == part_id
            for outbound_item in existing_outbound_items
        ):
            raise ValueError(
                "Esta peça já foi adicionada à saída."
            )

        available_transfer_items = (
            self.transfer_item_repository
            .list_available_by_part(
                part_id
            )
        )

        available_purchase_items = (
            self.purchase_item_repository
            .list_available_by_part(
                part_id
            )
        )

        total_transfer_available = sum(
            transfer_item.quantity_available
            for transfer_item in available_transfer_items
        )

        total_purchase_available = sum(
            purchase_item.quantity_available
            for purchase_item in available_purchase_items
        )

        total_available = (
            total_transfer_available
            + total_purchase_available
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

        # Transferências possuem prioridade porque têm
        # prazo específico para devolução à filial de origem.
        for transfer_item in available_transfer_items:
            if remaining_quantity <= 0:
                break

            if transfer_item.quantity_available <= 0:
                continue

            quantity_to_allocate = min(
                transfer_item.quantity_available,
                remaining_quantity,
            )

            transfer_item.quantity_available -= (
                quantity_to_allocate
            )

            self.transfer_item_repository.save(
                transfer_item
            )

            transfer_allocation = (
                OutboundTransferAllocation(
                    outbound_item_id=outbound_item.id,
                    transfer_item_id=transfer_item.id,
                    quantity_allocated=(
                        quantity_to_allocate
                    ),
                )
            )

            self.outbound_transfer_allocation_repository.add(
                transfer_allocation
            )

            remaining_quantity -= quantity_to_allocate

        # Somente o saldo não atendido pelas transferências
        # segue para o FIFO das compras.
        for purchase_item in available_purchase_items:
            if remaining_quantity <= 0:
                break

            if purchase_item.quantity_available <= 0:
                continue

            quantity_to_allocate = min(
                purchase_item.quantity_available,
                remaining_quantity,
            )

            purchase_item.quantity_available -= (
                quantity_to_allocate
            )

            self.purchase_item_repository.save(
                purchase_item
            )

            purchase_allocation = (
                OutboundPurchaseAllocation(
                    outbound_item_id=outbound_item.id,
                    purchase_item_id=purchase_item.id,
                    quantity_allocated=(
                        quantity_to_allocate
                    ),
                )
            )

            self.outbound_purchase_allocation_repository.add(
                purchase_allocation
            )

            remaining_quantity -= quantity_to_allocate

        if remaining_quantity > 0:
            raise ValueError(
                "Não foi possível alocar toda a quantidade "
                "solicitada para a saída."
            )

        return outbound_item

    def get_outbound(
        self,
        outbound_id: int,
    ) -> Outbound:
        if outbound_id <= 0:
            raise ValueError(
                "O identificador da saída deve ser "
                "maior que zero."
            )

        outbound = self.outbound_repository.get_by_id(
            outbound_id
        )

        if outbound is None:
            raise ValueError(
                "Saída não encontrada."
            )

        return outbound

    def list_outbounds(
        self,
        status: str | None = None,
        destination_type: str | None = None,
    ) -> list[Outbound]:
        if (
            status is not None
            and destination_type is not None
        ):
            raise ValueError(
                "Informe apenas um filtro por vez."
            )

        if status is not None:
            normalized_status = self._normalize_status(
                status
            )

            return (
                self.outbound_repository.list_by_status(
                    normalized_status
                )
            )

        if destination_type is not None:
            normalized_destination_type = (
                self._normalize_required_text(
                    destination_type,
                    (
                        "O tipo de destino é "
                        "obrigatório."
                    ),
                )
            )

            return (
                self.outbound_repository
                .list_by_destination_type(
                    normalized_destination_type
                )
            )

        return self.outbound_repository.list_all()

    def list_outbounds_by_status(
        self,
        status: str,
    ) -> list[Outbound]:
        normalized_status = self._normalize_status(
            status
        )

        return self.outbound_repository.list_by_status(
            normalized_status
        )

    def list_outbounds_by_destination_type(
        self,
        destination_type: str,
    ) -> list[Outbound]:
        normalized_destination_type = (
            self._normalize_required_text(
                destination_type,
                "O tipo de destino é obrigatório.",
            )
        )

        return (
            self.outbound_repository
            .list_by_destination_type(
                normalized_destination_type
            )
        )

    def list_outbound_items(
        self,
        outbound_id: int,
    ) -> list[OutboundItem]:
        self.get_outbound(
            outbound_id
        )

        return (
            self.outbound_item_repository
            .list_by_outbound(
                outbound_id
            )
        )

    def update_outbound(
        self,
        outbound_id: int,
        destination_type: str | None = None,
        work_order_number: str | None = None,
        sales_invoice_number: str | None = None,
        status: str | None = None,
    ) -> Outbound:
        outbound = self.get_outbound(
            outbound_id
        )

        if outbound.status == "CANCELLED":
            raise ValueError(
                "Não é possível alterar uma saída "
                "cancelada."
            )

        if destination_type is not None:
            outbound.destination_type = (
                self._normalize_required_text(
                    destination_type,
                    (
                        "O tipo de destino é "
                        "obrigatório."
                    ),
                )
            )

        if work_order_number is not None:
            normalized_work_order_number = (
                self._normalize_optional_text(
                    work_order_number
                )
            )

            self._ensure_work_order_is_unique(
                work_order_number=(
                    normalized_work_order_number
                ),
                ignored_outbound_id=outbound_id,
            )

            outbound.work_order_number = (
                normalized_work_order_number
            )

        if sales_invoice_number is not None:
            normalized_sales_invoice_number = (
                self._normalize_optional_text(
                    sales_invoice_number
                )
            )

            self._ensure_sales_invoice_is_unique(
                sales_invoice_number=(
                    normalized_sales_invoice_number
                ),
                ignored_outbound_id=outbound_id,
            )

            outbound.sales_invoice_number = (
                normalized_sales_invoice_number
            )

        if status is not None:
            normalized_status = self._normalize_status(
                status
            )

            if normalized_status == "CANCELLED":
                raise ValueError(
                    "Utilize a operação específica "
                    "para cancelar a saída."
                )

            outbound.status = normalized_status

        self._validate_reference_numbers(
            work_order_number=(
                outbound.work_order_number
            ),
            sales_invoice_number=(
                outbound.sales_invoice_number
            ),
        )

        return self.outbound_repository.save(
            outbound
        )

    def cancel_outbound(
        self,
        outbound_id: int,
    ) -> Outbound:
        outbound = self.get_outbound(
            outbound_id
        )

        if outbound.status == "CANCELLED":
            raise ValueError(
                "A saída já está cancelada."
            )

        outbound_items = (
            self.outbound_item_repository
            .list_by_outbound(
                outbound_id
            )
        )

        for outbound_item in outbound_items:
            allocations = (
                self
                .outbound_purchase_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            for allocation in allocations:
                purchase_item = (
                    self.purchase_item_repository
                    .get_by_id(
                        allocation.purchase_item_id
                    )
                )

                if purchase_item is None:
                    raise ValueError(
                        "Item de compra relacionado "
                        "à saída não encontrado."
                    )

                purchase_item.quantity_available += (
                    allocation.quantity_allocated
                )

        outbound.status = "CANCELLED"

        return self.outbound_repository.save(
            outbound
        )

    def _ensure_work_order_is_unique(
        self,
        work_order_number: str | None,
        ignored_outbound_id: int | None = None,
    ) -> None:
        if work_order_number is None:
            return

        existing_outbound = (
            self.outbound_repository
            .get_by_work_order_number(
                work_order_number
            )
        )

        if (
            existing_outbound is not None
            and existing_outbound.id
            != ignored_outbound_id
        ):
            raise ValueError(
                "Já existe uma saída com esta "
                "ordem de serviço."
            )

    def _ensure_sales_invoice_is_unique(
        self,
        sales_invoice_number: str | None,
        ignored_outbound_id: int | None = None,
    ) -> None:
        if sales_invoice_number is None:
            return

        existing_outbound = (
            self.outbound_repository
            .get_by_sales_invoice_number(
                sales_invoice_number
            )
        )

        if (
            existing_outbound is not None
            and existing_outbound.id
            != ignored_outbound_id
        ):
            raise ValueError(
                "Já existe uma saída com esta "
                "nota fiscal de venda."
            )

    @staticmethod
    def _validate_reference_numbers(
        work_order_number: str | None,
        sales_invoice_number: str | None,
    ) -> None:
        if (
            work_order_number is None
            and sales_invoice_number is None
        ):
            raise ValueError(
                "A saída deve possuir uma ordem de serviço "
                "ou uma nota fiscal de venda."
            )

    @classmethod
    def _normalize_status(
        cls,
        status: str,
    ) -> str:
        normalized_status = (
            cls._normalize_required_text(
                status,
                "O status da saída é obrigatório.",
            )
            .upper()
        )

        if (
            normalized_status
            not in cls.ALLOWED_STATUSES
        ):
            raise ValueError(
                "Status de saída inválido."
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

        if not normalized_value:
            return None

        return normalized_value