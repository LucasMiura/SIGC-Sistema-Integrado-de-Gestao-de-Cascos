from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound_transfer_allocation import (
    OutboundTransferAllocation,
)


class OutboundTransferAllocationRepository:
    """
    Responsável pela persistência das alocações
    de saídas originadas de transferências.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        allocation_id: int,
    ) -> OutboundTransferAllocation | None:
        statement = (
            select(
                OutboundTransferAllocation
            )
            .where(
                OutboundTransferAllocation.id
                == allocation_id
            )
        )

        return self.session.scalar(
            statement
        )

    def list_by_outbound_item(
        self,
        outbound_item_id: int,
    ) -> list[OutboundTransferAllocation]:
        statement = (
            select(
                OutboundTransferAllocation
            )
            .where(
                OutboundTransferAllocation
                .outbound_item_id
                == outbound_item_id
            )
            .order_by(
                OutboundTransferAllocation.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_transfer_item(
        self,
        transfer_item_id: int,
    ) -> list[OutboundTransferAllocation]:
        statement = (
            select(
                OutboundTransferAllocation
            )
            .where(
                OutboundTransferAllocation
                .transfer_item_id
                == transfer_item_id
            )
            .order_by(
                OutboundTransferAllocation.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        allocation: OutboundTransferAllocation,
    ) -> OutboundTransferAllocation:
        self.session.add(
            allocation
        )

        self.session.flush()

        return allocation