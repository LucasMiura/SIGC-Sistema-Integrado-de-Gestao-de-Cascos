from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class OutboundPurchaseAllocation(Base):
    __tablename__ = "outbound_purchase_allocations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    outbound_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("outbound_items.id"),
        nullable=False,
    )

    purchase_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("purchase_items.id"),
        nullable=False,
    )

    quantity_allocated: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )