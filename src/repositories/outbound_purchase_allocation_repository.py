from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)


class OutboundPurchaseAllocationRepository:
    """Responsável pela persistência das alocações de saída."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        allocation_id: int,
    ) -> OutboundPurchaseAllocation | None:
        statement = select(
            OutboundPurchaseAllocation
        ).where(
            OutboundPurchaseAllocation.id == allocation_id
        )
        return self.session.scalar(statement)

    def list_by_outbound_item(
        self,
        outbound_item_id: int,
    ) -> list[OutboundPurchaseAllocation]:
        statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.outbound_item_id
                == outbound_item_id
            )
            .order_by(OutboundPurchaseAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def list_by_purchase_item(
        self,
        purchase_item_id: int,
    ) -> list[OutboundPurchaseAllocation]:
        statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.purchase_item_id
                == purchase_item_id
            )
            .order_by(OutboundPurchaseAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        allocation: OutboundPurchaseAllocation,
    ) -> OutboundPurchaseAllocation:
        self.session.add(allocation)
        self.session.flush()
        return allocation