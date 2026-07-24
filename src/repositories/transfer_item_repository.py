from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.transfer_item import TransferItem


class TransferItemRepository:
    """Responsável pela persistência dos itens de transferência."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        transfer_item_id: int,
    ) -> TransferItem | None:
        statement = select(TransferItem).where(
            TransferItem.id == transfer_item_id
        )
        return self.session.scalar(statement)

    def list_by_transfer(
        self,
        transfer_id: int,
    ) -> list[TransferItem]:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.transfer_id == transfer_id
            )
            .order_by(TransferItem.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        item: TransferItem,
    ) -> TransferItem:
        self.session.add(item)
        self.session.flush()
        return item