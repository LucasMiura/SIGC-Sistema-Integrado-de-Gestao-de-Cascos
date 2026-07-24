from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import PurchaseRepository
from src.repositories.supplier_repository import SupplierRepository


class PurchaseService:
    """Regras de negócio relacionadas a compras."""

    def __init__(
        self,
        purchase_repository: PurchaseRepository,
        purchase_item_repository: PurchaseItemRepository,
        supplier_repository: SupplierRepository,
        part_repository: PartRepository,
    ):
        self.purchase_repository = purchase_repository
        self.purchase_item_repository = purchase_item_repository
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
        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        purchase = Purchase(
            supplier_id=supplier_id,
            invoice_number=invoice_number,
            invoice_series=invoice_series,
            issue_date=issue_date,
            created_by=created_by,
            status=status,
            notes=notes,
        )

        return self.purchase_repository.add(purchase)

    def add_item(
        self,
        purchase_id: int,
        part_id: int,
        quantity_purchased: int,
    ) -> PurchaseItem:
        purchase = self.purchase_repository.get_by_id(
            purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra não encontrada."
            )

        part = self.part_repository.get_by_id(part_id)

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if quantity_purchased <= 0:
            raise ValueError(
                "A quantidade comprada deve ser maior que zero."
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
        purchase = self.purchase_repository.get_by_id(
            purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra não encontrada."
            )

        return purchase

    def list_purchases(self) -> list[Purchase]:
        return self.purchase_repository.list_all()

    def list_purchase_items(
        self,
        purchase_id: int,
    ) -> list[PurchaseItem]:
        purchase = self.purchase_repository.get_by_id(
            purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra não encontrada."
            )

        return self.purchase_item_repository.list_by_purchase(
            purchase_id
        )