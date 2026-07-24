from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.purchase_item import PurchaseItem


class PurchaseItemRepository:
    """Responsável pela persistência dos itens de compra."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        purchase_item_id: int,
    ) -> PurchaseItem | None:
        statement = select(PurchaseItem).where(
            PurchaseItem.id == purchase_item_id
        )
        return self.session.scalar(statement)

    def list_by_purchase(
        self,
        purchase_id: int,
    ) -> list[PurchaseItem]:
        statement = (
            select(PurchaseItem)
            .where(PurchaseItem.purchase_id == purchase_id)
            .order_by(PurchaseItem.id)
        )
        return list(self.session.scalars(statement).all())

    def list_available_by_part(
        self,
        part_id: int,
    ) -> list[PurchaseItem]:
        statement = (
            select(PurchaseItem)
            .where(
                PurchaseItem.part_id == part_id,
                PurchaseItem.quantity_available > 0,
            )
            .order_by(
                PurchaseItem.created_at,
                PurchaseItem.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        purchase_item: PurchaseItem,
    ) -> PurchaseItem:
        self.session.add(purchase_item)
        self.session.flush()
        return purchase_item