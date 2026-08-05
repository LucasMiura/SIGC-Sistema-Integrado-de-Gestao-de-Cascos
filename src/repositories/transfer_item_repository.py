from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.transfer_item import TransferItem


class TransferItemRepository:
    """
    Responsável pela persistência dos itens
    recebidos por transferência.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        transfer_item_id: int,
    ) -> TransferItem | None:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.id
                == transfer_item_id
            )
        )

        return self.session.scalar(
            statement
        )

    def get_by_transfer_and_part(
        self,
        transfer_id: int,
        part_id: int,
    ) -> TransferItem | None:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.transfer_id
                == transfer_id,
                TransferItem.part_id
                == part_id,
            )
        )

        return self.session.scalar(
            statement
        )

    def list_by_transfer(
        self,
        transfer_id: int,
    ) -> list[TransferItem]:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.transfer_id
                == transfer_id
            )
            .order_by(
                TransferItem.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_part(
        self,
        part_id: int,
    ) -> list[TransferItem]:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.part_id
                == part_id
            )
            .order_by(
                TransferItem.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_available_by_part(
        self,
        part_id: int,
    ) -> list[TransferItem]:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.part_id
                == part_id,
                TransferItem.quantity_available > 0,
            )
            .order_by(
                TransferItem.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        transfer_item: TransferItem,
    ) -> TransferItem:
        self.session.add(
            transfer_item
        )

        self.session.flush()

        return transfer_item

    def save(
        self,
        transfer_item: TransferItem,
    ) -> TransferItem:
        self.session.add(
            transfer_item
        )

        self.session.flush()

        return transfer_item