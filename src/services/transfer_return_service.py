from src.models.transfer_return import TransferReturn
from src.models.transfer_return_item import (
    TransferReturnItem,
)
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.repositories.transfer_return_item_repository import (
    TransferReturnItemRepository,
)
from src.repositories.transfer_return_repository import (
    TransferReturnRepository,
)


class TransferReturnService:
    """
    Regras de negócio das remessas de cascos
    devolvidas às filiais de origem.
    """

    ALLOWED_STATUSES = {
        "ACTIVE",
        "CANCELLED",
    }

    def __init__(
        self,
        transfer_return_repository: (
            TransferReturnRepository
        ),
        transfer_return_item_repository: (
            TransferReturnItemRepository
        ),
        transfer_repository: TransferRepository,
        transfer_item_repository: (
            TransferItemRepository
        ),
        outbound_transfer_allocation_repository: (
            OutboundTransferAllocationRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
    ) -> None:
        self.transfer_return_repository = (
            transfer_return_repository
        )

        self.transfer_return_item_repository = (
            transfer_return_item_repository
        )

        self.transfer_repository = (
            transfer_repository
        )

        self.transfer_item_repository = (
            transfer_item_repository
        )

        self.outbound_transfer_allocation_repository = (
            outbound_transfer_allocation_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

    def create_transfer_return(
        self,
        transfer_id: int,
        dispatch_invoice_number: str,
        issue_date: str,
        created_by: int,
        dispatch_invoice_series: str | None = None,
        status: str = "ACTIVE",
        notes: str | None = None,
    ) -> TransferReturn:
        """
        Registra uma nova remessa de cascos
        para a filial que originou a transferência.
        """

        self._validate_positive_id(
            transfer_id,
            (
                "O identificador da transferência "
                "deve ser maior que zero."
            ),
        )

        self._validate_positive_id(
            created_by,
            (
                "O identificador do usuário deve ser "
                "maior que zero."
            ),
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
                "Uma devolução à filial não pode ser "
                "criada já cancelada."
            )

        transfer = self.transfer_repository.get_by_id(
            transfer_id
        )

        if transfer is None:
            raise ValueError(
                "Transferência não encontrada."
            )

        if transfer.status != "ACTIVE":
            raise ValueError(
                "Não é possível registrar devolução "
                "para uma transferência que não está "
                "ativa."
            )

        existing_transfer_return = (
            self.transfer_return_repository
            .get_by_dispatch_invoice_number(
                normalized_invoice_number
            )
        )

        if existing_transfer_return is not None:
            raise ValueError(
                "Já existe uma devolução à filial "
                "cadastrada com esse número de Nota "
                "Fiscal de Simples Remessa."
            )

        transfer_return = TransferReturn(
            transfer_id=transfer_id,
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

        return self.transfer_return_repository.add(
            transfer_return
        )

    def add_item(
        self,
        transfer_return_id: int,
        transfer_item_id: int,
        quantity: int,
    ) -> TransferReturnItem:
        """
        Adiciona à remessa uma quantidade de cascos
        pertencente a um item de transferência.
        """

        self._validate_positive_id(
            transfer_return_id,
            (
                "O identificador da devolução à filial "
                "deve ser maior que zero."
            ),
        )

        self._validate_positive_id(
            transfer_item_id,
            (
                "O identificador do item de "
                "transferência deve ser maior que zero."
            ),
        )

        if quantity <= 0:
            raise ValueError(
                "A quantidade devolvida deve ser "
                "maior que zero."
            )

        transfer_return = (
            self.get_transfer_return(
                transfer_return_id
            )
        )

        if transfer_return.status != "ACTIVE":
            raise ValueError(
                "Não é possível adicionar itens a uma "
                "devolução à filial que não está ativa."
            )

        transfer_item = (
            self.transfer_item_repository.get_by_id(
                transfer_item_id
            )
        )

        if transfer_item is None:
            raise ValueError(
                "Item de transferência não encontrado."
            )

        if (
            transfer_item.transfer_id
            != transfer_return.transfer_id
        ):
            raise ValueError(
                "O item informado não pertence à "
                "transferência vinculada à devolução."
            )

        existing_item = (
            self.transfer_return_item_repository
            .get_by_transfer_return_and_transfer_item(
                transfer_return_id=(
                    transfer_return_id
                ),
                transfer_item_id=transfer_item_id,
            )
        )

        if existing_item is not None:
            raise ValueError(
                "Este item de transferência já foi "
                "adicionado à devolução."
            )

        available_quantity = (
            self.get_available_quantity(
                transfer_item_id
            )
        )

        if available_quantity <= 0:
            raise ValueError(
                "Não existe quantidade disponível para "
                "devolução à filial neste item de "
                "transferência."
            )

        if quantity > available_quantity:
            raise ValueError(
                "A quantidade devolvida é maior que a "
                "quantidade disponível para devolução "
                "à filial. Quantidade máxima permitida: "
                f"{available_quantity}."
            )

        transfer_return_item = TransferReturnItem(
            transfer_return_id=transfer_return_id,
            transfer_item_id=transfer_item_id,
            quantity=quantity,
        )

        return (
            self.transfer_return_item_repository.add(
                transfer_return_item
            )
        )

    def get_available_quantity(
        self,
        transfer_item_id: int,
    ) -> int:
        """
        Retorna quantos cascos pertencentes ao item
        já foram devolvidos pelos clientes e ainda
        não foram enviados à filial de origem.
        """

        self._validate_positive_id(
            transfer_item_id,
            (
                "O identificador do item de "
                "transferência deve ser maior que zero."
            ),
        )

        transfer_item = (
            self.transfer_item_repository.get_by_id(
                transfer_item_id
            )
        )

        if transfer_item is None:
            raise ValueError(
                "Item de transferência não encontrado."
            )

        customer_returned_quantity = (
            self._get_customer_returned_quantity(
                transfer_item_id
            )
        )

        already_returned_to_branch = (
            self.transfer_return_item_repository
            .get_returned_quantity_by_transfer_item(
                transfer_item_id
            )
        )

        available_quantity = (
            customer_returned_quantity
            - already_returned_to_branch
        )

        return max(
            available_quantity,
            0,
        )

    def get_transfer_return(
        self,
        transfer_return_id: int,
    ) -> TransferReturn:
        """
        Retorna uma devolução à filial
        pelo seu identificador.
        """

        self._validate_positive_id(
            transfer_return_id,
            (
                "O identificador da devolução à filial "
                "deve ser maior que zero."
            ),
        )

        transfer_return = (
            self.transfer_return_repository.get_by_id(
                transfer_return_id
            )
        )

        if transfer_return is None:
            raise ValueError(
                "Devolução à filial não encontrada."
            )

        return transfer_return

    def cancel_transfer_return(
        self,
        transfer_return_id: int,
    ) -> TransferReturn:
        """
        Cancela uma devolução à filial
        preservando seus itens e histórico.
        """

        transfer_return = self.get_transfer_return(
            transfer_return_id
        )

        if transfer_return.status == "CANCELLED":
            raise ValueError(
                "A devolução à filial já está "
                "cancelada."
            )

        transfer_return.status = "CANCELLED"

        return self.transfer_return_repository.save(
            transfer_return
        )

    def list_transfer_returns(
        self,
    ) -> list[TransferReturn]:
        """
        Lista todas as devoluções às filiais.
        """

        return (
            self.transfer_return_repository.list_all()
        )

    def list_by_transfer(
        self,
        transfer_id: int,
    ) -> list[TransferReturn]:
        """
        Lista as devoluções vinculadas
        a uma transferência de entrada.
        """

        self._validate_positive_id(
            transfer_id,
            (
                "O identificador da transferência "
                "deve ser maior que zero."
            ),
        )

        transfer = self.transfer_repository.get_by_id(
            transfer_id
        )

        if transfer is None:
            raise ValueError(
                "Transferência não encontrada."
            )

        return (
            self.transfer_return_repository
            .list_by_transfer(
                transfer_id
            )
        )

    def list_items(
        self,
        transfer_return_id: int,
    ) -> list[TransferReturnItem]:
        """
        Lista os itens de uma devolução à filial.
        """

        self.get_transfer_return(
            transfer_return_id
        )

        return (
            self.transfer_return_item_repository
            .list_by_transfer_return(
                transfer_return_id
            )
        )

    def _get_customer_returned_quantity(
        self,
        transfer_item_id: int,
    ) -> int:
        """
        Calcula quantos cascos devolvidos pelos clientes
        pertencem a um TransferItem específico.

        Uma saída pode consumir mais de um TransferItem.
        As devoluções dos clientes são distribuídas na
        mesma ordem das alocações criadas na saída.
        """

        target_allocations = (
            self.outbound_transfer_allocation_repository
            .list_by_transfer_item(
                transfer_item_id
            )
        )

        outbound_item_ids = {
            allocation.outbound_item_id
            for allocation in target_allocations
        }

        total_returned_for_transfer_item = 0

        for outbound_item_id in outbound_item_ids:
            transfer_allocations = (
                self.outbound_transfer_allocation_repository
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

            for transfer_allocation in (
                transfer_allocations
            ):
                if remaining_returned_quantity <= 0:
                    break

                returned_for_allocation = min(
                    remaining_returned_quantity,
                    (
                        transfer_allocation
                        .quantity_allocated
                    ),
                )

                if (
                    transfer_allocation.transfer_item_id
                    == transfer_item_id
                ):
                    total_returned_for_transfer_item += (
                        returned_for_allocation
                    )

                remaining_returned_quantity -= (
                    returned_for_allocation
                )

        return total_returned_for_transfer_item

    def _normalize_status(
        self,
        status: str,
    ) -> str:
        normalized_status = (
            self._normalize_required_text(
                status,
                (
                    "O status da devolução à filial "
                    "é obrigatório."
                ),
            )
            .upper()
        )

        if (
            normalized_status
            not in self.ALLOWED_STATUSES
        ):
            raise ValueError(
                "O status da devolução à filial deve "
                "ser ACTIVE ou CANCELLED."
            )

        return normalized_status

    @staticmethod
    def _validate_positive_id(
        value: int,
        error_message: str,
    ) -> None:
        if value <= 0:
            raise ValueError(
                error_message
            )

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