from typing import Final

from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)


FIELD_NOT_PROVIDED: Final = object()


class PurchaseService:
    """
    Regras de negócio relacionadas às compras.
    """

    ALLOWED_STATUSES: Final[set[str]] = {
        "PENDING",
        "RECEIVED",
        "CANCELLED",
    }

    def __init__(
        self,
        purchase_repository: PurchaseRepository,
        purchase_item_repository: PurchaseItemRepository,
        supplier_repository: SupplierRepository,
        part_repository: PartRepository,
    ) -> None:
        self.purchase_repository = purchase_repository
        self.purchase_item_repository = (
            purchase_item_repository
        )
        self.supplier_repository = supplier_repository
        self.part_repository = part_repository

    def create_purchase(
        self,
        supplier_id: int,
        invoice_number: str,
        invoice_series: str | None,
        issue_date: str,
        created_by: int,
        status: str,
        notes: str | None = None,
    ) -> Purchase:
        """
        Cria uma nova compra.
        """

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

        normalized_invoice_number = (
            self._normalize_required_text(
                invoice_number,
                "O número da nota fiscal é obrigatório.",
            )
        )

        normalized_invoice_series = (
            self._normalize_optional_text(
                invoice_series
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

        normalized_notes = self._normalize_optional_text(
            notes
        )

        existing_purchase = (
            self.purchase_repository.get_by_invoice(
                supplier_id=supplier_id,
                invoice_number=normalized_invoice_number,
                invoice_series=normalized_invoice_series,
            )
        )

        if existing_purchase is not None:
            raise ValueError(
                "Já existe uma compra com esta nota fiscal, "
                "série e fornecedor."
            )

        purchase = Purchase(
            supplier_id=supplier_id,
            invoice_number=normalized_invoice_number,
            invoice_series=normalized_invoice_series,
            issue_date=normalized_issue_date,
            created_by=created_by,
            status=normalized_status,
            notes=normalized_notes,
        )

        return self.purchase_repository.add(
            purchase
        )

    def add_item(
        self,
        purchase_id: int,
        part_id: int,
        quantity_purchased: int,
    ) -> PurchaseItem:
        """
        Adiciona um item a uma compra.
        """

        purchase = self.get_purchase(
            purchase_id
        )

        if purchase.status == "CANCELLED":
            raise ValueError(
                "Não é possível adicionar itens "
                "a uma compra cancelada."
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

        if part.supplier_id != purchase.supplier_id:
            raise ValueError(
                "A peça informada não pertence "
                "ao fornecedor da compra."
            )

        if quantity_purchased <= 0:
            raise ValueError(
                "A quantidade comprada deve ser "
                "maior que zero."
            )

        purchase_items = (
            self.purchase_item_repository.list_by_purchase(
                purchase_id
            )
        )

        item_already_exists = any(
            item.part_id == part_id
            for item in purchase_items
        )

        if item_already_exists:
            raise ValueError(
                "Esta peça já foi adicionada à compra."
            )

        purchase_item = PurchaseItem(
            purchase_id=purchase_id,
            part_id=part_id,
            quantity_purchased=quantity_purchased,
            quantity_available=quantity_purchased,
        )

        return self.purchase_item_repository.add(
            purchase_item
        )

    def get_purchase(
        self,
        purchase_id: int,
    ) -> Purchase:
        """
        Retorna uma compra obrigatoriamente existente.
        """

        purchase = self.purchase_repository.get_by_id(
            purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra não encontrada."
            )

        return purchase

    def list_purchases(
        self,
    ) -> list[Purchase]:
        """
        Lista todas as compras.
        """

        return self.purchase_repository.list_all()

    def list_purchases_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Purchase]:
        """
        Lista as compras de determinado fornecedor.
        """

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        return self.purchase_repository.list_by_supplier(
            supplier_id
        )

    def list_purchase_items(
        self,
        purchase_id: int,
    ) -> list[PurchaseItem]:
        """
        Lista os itens de uma compra.
        """

        self.get_purchase(
            purchase_id
        )

        return (
            self.purchase_item_repository.list_by_purchase(
                purchase_id
            )
        )

    def update_purchase(
        self,
        purchase_id: int,
        *,
        supplier_id: int | object = FIELD_NOT_PROVIDED,
        invoice_number: str | object = FIELD_NOT_PROVIDED,
        invoice_series: (
            str | None | object
        ) = FIELD_NOT_PROVIDED,
        issue_date: str | object = FIELD_NOT_PROVIDED,
        status: str | object = FIELD_NOT_PROVIDED,
        notes: (
            str | None | object
        ) = FIELD_NOT_PROVIDED,
    ) -> Purchase:
        """
        Atualiza parcialmente uma compra.
        """

        purchase = self.get_purchase(
            purchase_id
        )

        if purchase.status == "CANCELLED":
            raise ValueError(
                "Uma compra cancelada não pode ser alterada."
            )

        new_supplier_id = purchase.supplier_id
        new_invoice_number = purchase.invoice_number
        new_invoice_series = purchase.invoice_series

        if supplier_id is not FIELD_NOT_PROVIDED:
            if not isinstance(supplier_id, int):
                raise ValueError(
                    "Fornecedor inválido."
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

            purchase_items = (
                self.purchase_item_repository.list_by_purchase(
                    purchase_id
                )
            )

            incompatible_item = any(
                self._part_belongs_to_another_supplier(
                    item.part_id,
                    supplier_id,
                )
                for item in purchase_items
            )

            if incompatible_item:
                raise ValueError(
                    "Não é possível alterar o fornecedor "
                    "porque existem peças incompatíveis "
                    "na compra."
                )

            new_supplier_id = supplier_id

        if invoice_number is not FIELD_NOT_PROVIDED:
            if not isinstance(invoice_number, str):
                raise ValueError(
                    "Número da nota fiscal inválido."
                )

            new_invoice_number = (
                self._normalize_required_text(
                    invoice_number,
                    "O número da nota fiscal é obrigatório.",
                )
            )

        if invoice_series is not FIELD_NOT_PROVIDED:
            if (
                invoice_series is not None
                and not isinstance(invoice_series, str)
            ):
                raise ValueError(
                    "Série da nota fiscal inválida."
                )

            new_invoice_series = (
                self._normalize_optional_text(
                    invoice_series
                )
            )

        invoice_data_changed = any(
            (
                new_supplier_id != purchase.supplier_id,
                new_invoice_number
                != purchase.invoice_number,
                new_invoice_series
                != purchase.invoice_series,
            )
        )

        if invoice_data_changed:
            existing_purchase = (
                self.purchase_repository.get_by_invoice(
                    supplier_id=new_supplier_id,
                    invoice_number=new_invoice_number,
                    invoice_series=new_invoice_series,
                )
            )

            if (
                existing_purchase is not None
                and existing_purchase.id != purchase.id
            ):
                raise ValueError(
                    "Já existe uma compra com esta nota "
                    "fiscal, série e fornecedor."
                )

        purchase.supplier_id = new_supplier_id
        purchase.invoice_number = new_invoice_number
        purchase.invoice_series = new_invoice_series

        if issue_date is not FIELD_NOT_PROVIDED:
            if not isinstance(issue_date, str):
                raise ValueError(
                    "Data de emissão inválida."
                )

            purchase.issue_date = (
                self._normalize_required_text(
                    issue_date,
                    "A data de emissão é obrigatória.",
                )
            )

        if status is not FIELD_NOT_PROVIDED:
            if not isinstance(status, str):
                raise ValueError(
                    "Status da compra inválido."
                )

            normalized_status = self._normalize_status(
                status
            )

            if normalized_status == "CANCELLED":
                raise ValueError(
                    "Utilize a operação específica "
                    "para cancelar a compra."
                )

            purchase.status = normalized_status

        if notes is not FIELD_NOT_PROVIDED:
            if (
                notes is not None
                and not isinstance(notes, str)
            ):
                raise ValueError(
                    "Observações inválidas."
                )

            purchase.notes = self._normalize_optional_text(
                notes
            )

        return self.purchase_repository.save(
            purchase
        )

    def cancel_purchase(
        self,
        purchase_id: int,
    ) -> Purchase:
        """
        Cancela uma compra sem apagar seu histórico.
        """

        purchase = self.get_purchase(
            purchase_id
        )

        if purchase.status == "CANCELLED":
            raise ValueError(
                "A compra já está cancelada."
            )

        purchase_items = (
            self.purchase_item_repository.list_by_purchase(
                purchase_id
            )
        )

        has_movement = any(
            item.quantity_available
            != item.quantity_purchased
            for item in purchase_items
        )

        if has_movement:
            raise ValueError(
                "Não é possível cancelar uma compra "
                "que já possui movimentações."
            )

        purchase.status = "CANCELLED"

        return self.purchase_repository.save(
            purchase
        )

    def _part_belongs_to_another_supplier(
        self,
        part_id: int,
        supplier_id: int,
    ) -> bool:
        """
        Verifica a compatibilidade entre peça e fornecedor.
        """

        part = self.part_repository.get_by_id(
            part_id
        )

        return (
            part is None
            or part.supplier_id != supplier_id
        )

    @classmethod
    def _normalize_status(
        cls,
        value: str,
    ) -> str:
        """
        Normaliza e valida o status da compra.
        """

        normalized_value = (
            cls._normalize_required_text(
                value,
                "O status da compra é obrigatório.",
            ).upper()
        )

        if normalized_value not in cls.ALLOWED_STATUSES:
            allowed_values = ", ".join(
                sorted(cls.ALLOWED_STATUSES)
            )

            raise ValueError(
                "Status da compra inválido. "
                f"Valores permitidos: {allowed_values}."
            )

        return normalized_value

    @staticmethod
    def _normalize_required_text(
        value: str,
        empty_message: str,
    ) -> str:
        """
        Normaliza um texto obrigatório.
        """

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                empty_message
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """
        Normaliza um texto opcional.
        """

        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None