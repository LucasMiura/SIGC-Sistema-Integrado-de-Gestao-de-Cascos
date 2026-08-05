from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)


class TransferService:
    """
    Regras de negócio relacionadas às transferências
    recebidas de outras filiais.
    """

    ALLOWED_STATUSES = {
        "ACTIVE",
        "CANCELLED",
    }

    def __init__(
        self,
        transfer_repository: TransferRepository,
        transfer_item_repository: (
            TransferItemRepository
        ),
        part_repository: PartRepository,
    ) -> None:
        self.transfer_repository = (
            transfer_repository
        )

        self.transfer_item_repository = (
            transfer_item_repository
        )

        self.part_repository = (
            part_repository
        )

    def create_transfer(
        self,
        origin_branch_id: int,
        destination_branch_id: int,
        invoice_number: str,
        issue_date: str,
        created_by: int,
        status: str = "ACTIVE",
    ) -> Transfer:
        """
        Registra uma transferência recebida
        de outra filial.
        """

        self._validate_positive_id(
            origin_branch_id,
            (
                "O identificador da filial de origem "
                "deve ser maior que zero."
            ),
        )

        self._validate_positive_id(
            destination_branch_id,
            (
                "O identificador da filial de destino "
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

        if origin_branch_id == destination_branch_id:
            raise ValueError(
                "A filial de origem deve ser diferente "
                "da filial de destino."
            )

        normalized_invoice_number = (
            self._normalize_required_text(
                invoice_number,
                (
                    "O número da Nota Fiscal de "
                    "transferência é obrigatório."
                ),
            )
        )

        normalized_issue_date = (
            self._normalize_required_text(
                issue_date,
                "A data de emissão é obrigatória.",
            )
        )

        normalized_status = self._normalize_status(
            status
        )

        if normalized_status == "CANCELLED":
            raise ValueError(
                "Uma transferência não pode ser criada "
                "já cancelada."
            )

        existing_transfer = (
            self.transfer_repository
            .get_by_invoice_number(
                normalized_invoice_number
            )
        )

        if existing_transfer is not None:
            raise ValueError(
                "Já existe uma transferência cadastrada "
                "com esse número de Nota Fiscal."
            )

        transfer = Transfer(
            origin_branch_id=origin_branch_id,
            destination_branch_id=(
                destination_branch_id
            ),
            invoice_number=(
                normalized_invoice_number
            ),
            issue_date=normalized_issue_date,
            status=normalized_status,
            created_by=created_by,
        )

        return self.transfer_repository.add(
            transfer
        )

    def add_item(
        self,
        transfer_id: int,
        part_id: int,
        quantity: int,
        return_deadline_days: int,
    ) -> TransferItem:
        """
        Adiciona uma peça recebida à transferência.

        A quantidade recebida é registrada também
        como quantidade inicialmente disponível.
        """

        self._validate_positive_id(
            transfer_id,
            (
                "O identificador da transferência "
                "deve ser maior que zero."
            ),
        )

        self._validate_positive_id(
            part_id,
            (
                "O identificador da peça deve ser "
                "maior que zero."
            ),
        )

        if quantity <= 0:
            raise ValueError(
                "A quantidade recebida deve ser "
                "maior que zero."
            )

        if return_deadline_days <= 0:
            raise ValueError(
                "O prazo de devolução deve ser "
                "maior que zero."
            )

        transfer = self.get_transfer(
            transfer_id
        )

        if transfer.status != "ACTIVE":
            raise ValueError(
                "Não é possível adicionar itens a uma "
                "transferência que não está ativa."
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
                "A peça informada está inativa."
            )

        existing_item = (
            self.transfer_item_repository
            .get_by_transfer_and_part(
                transfer_id=transfer_id,
                part_id=part_id,
            )
        )

        if existing_item is not None:
            raise ValueError(
                "Esta peça já foi adicionada "
                "à transferência."
            )

        transfer_item = TransferItem(
            transfer_id=transfer_id,
            part_id=part_id,
            quantity=quantity,
            quantity_available=quantity,
            return_deadline_days=(
                return_deadline_days
            ),
        )

        return self.transfer_item_repository.add(
            transfer_item
        )

    def get_transfer(
        self,
        transfer_id: int,
    ) -> Transfer:
        """
        Retorna uma transferência pelo identificador.
        """

        self._validate_positive_id(
            transfer_id,
            (
                "O identificador da transferência "
                "deve ser maior que zero."
            ),
        )

        transfer = (
            self.transfer_repository.get_by_id(
                transfer_id
            )
        )

        if transfer is None:
            raise ValueError(
                "Transferência não encontrada."
            )

        return transfer

    def list_transfers(
        self,
    ) -> list[Transfer]:
        """
        Lista todas as transferências cadastradas.
        """

        return self.transfer_repository.list_all()

    def list_items(
        self,
        transfer_id: int,
    ) -> list[TransferItem]:
        """
        Lista os itens de uma transferência.
        """

        self.get_transfer(
            transfer_id
        )

        return (
            self.transfer_item_repository
            .list_by_transfer(
                transfer_id
            )
        )

    def get_transfer_item(
        self,
        transfer_item_id: int,
    ) -> TransferItem:
        """
        Retorna um item de transferência
        pelo identificador.
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

        return transfer_item

    def get_available_quantity(
        self,
        transfer_item_id: int,
    ) -> int:
        """
        Retorna a quantidade ainda disponível
        para novas saídas.
        """

        transfer_item = self.get_transfer_item(
            transfer_item_id
        )

        return max(
            transfer_item.quantity_available,
            0,
        )

    def reduce_available_quantity(
        self,
        transfer_item_id: int,
        quantity: int,
    ) -> TransferItem:
        """
        Reduz o saldo disponível de uma origem
        de transferência.

        Este método será utilizado posteriormente
        pela integração com o módulo de saídas.
        """

        if quantity <= 0:
            raise ValueError(
                "A quantidade a movimentar deve ser "
                "maior que zero."
            )

        transfer_item = self.get_transfer_item(
            transfer_item_id
        )

        if quantity > transfer_item.quantity_available:
            raise ValueError(
                "A quantidade informada é superior "
                "ao saldo disponível do item de "
                "transferência."
            )

        transfer_item.quantity_available -= quantity

        return self.transfer_item_repository.save(
            transfer_item
        )

    def restore_available_quantity(
        self,
        transfer_item_id: int,
        quantity: int,
    ) -> TransferItem:
        """
        Restaura saldo disponível quando uma
        movimentação for revertida.
        """

        if quantity <= 0:
            raise ValueError(
                "A quantidade a restaurar deve ser "
                "maior que zero."
            )

        transfer_item = self.get_transfer_item(
            transfer_item_id
        )

        restored_quantity = (
            transfer_item.quantity_available
            + quantity
        )

        if restored_quantity > transfer_item.quantity:
            raise ValueError(
                "A quantidade restaurada não pode "
                "ultrapassar a quantidade originalmente "
                "recebida."
            )

        transfer_item.quantity_available = (
            restored_quantity
        )

        return self.transfer_item_repository.save(
            transfer_item
        )

    def cancel_transfer(
        self,
        transfer_id: int,
    ) -> Transfer:
        """
        Cancela uma transferência que ainda não teve
        nenhuma quantidade movimentada.
        """

        transfer = self.get_transfer(
            transfer_id
        )

        if transfer.status == "CANCELLED":
            raise ValueError(
                "A transferência já está cancelada."
            )

        transfer_items = (
            self.transfer_item_repository
            .list_by_transfer(
                transfer_id
            )
        )

        has_movements = any(
            (
                transfer_item.quantity_available
                != transfer_item.quantity
            )
            for transfer_item in transfer_items
        )

        if has_movements:
            raise ValueError(
                "Não é possível cancelar uma "
                "transferência que possui movimentações."
            )

        transfer.status = "CANCELLED"

        return self.transfer_repository.save(
            transfer
        )

    def _normalize_status(
        self,
        status: str,
    ) -> str:
        normalized_status = (
            self._normalize_required_text(
                status,
                (
                    "O status da transferência "
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
                "O status da transferência deve ser "
                "ACTIVE ou CANCELLED."
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