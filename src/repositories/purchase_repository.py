from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.purchase import Purchase


class PurchaseRepository:
    """Responsável pela persistência de compras."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, purchase_id: int) -> Purchase | None:
        statement = select(Purchase).where(
            Purchase.id == purchase_id
        )
        return self.session.scalar(statement)

    def list_all(self) -> list[Purchase]:
        statement = select(Purchase).order_by(
            Purchase.issue_date,
            Purchase.id,
        )
        return list(self.session.scalars(statement).all())

    def add(self, purchase: Purchase) -> Purchase:
        self.session.add(purchase)
        self.session.flush()
        return purchase