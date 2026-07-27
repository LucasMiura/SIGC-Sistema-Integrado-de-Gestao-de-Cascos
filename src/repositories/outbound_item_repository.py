from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound_item import OutboundItem


class OutboundItemRepository:
    """Responsável pela persistência dos itens de saída."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        outbound_item_id: int,
    ) -> OutboundItem | None:
        statement = select(
            OutboundItem
        ).where(
            OutboundItem.id == outbound_item_id
        )

        return self.session.scalar(
            statement
        )

    def list_by_outbound(
        self,
        outbound_id: int,
    ) -> list[OutboundItem]:
        statement = (
            select(OutboundItem)
            .where(
                OutboundItem.outbound_id
                == outbound_id
            )
            .order_by(
                OutboundItem.id
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
    ) -> list[OutboundItem]:
        statement = (
            select(OutboundItem)
            .where(
                OutboundItem.part_id
                == part_id
            )
            .order_by(
                OutboundItem.created_at,
                OutboundItem.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        outbound_item: OutboundItem,
    ) -> OutboundItem:
        self.session.add(
            outbound_item
        )

        self.session.flush()

        return outbound_item