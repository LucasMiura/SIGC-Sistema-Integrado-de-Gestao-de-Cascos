from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class CustomerReturnAllocation(Base):
    __tablename__ = "customer_return_allocations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    customer_return_item_id: Mapped[int] = mapped_column(
        ForeignKey("customer_return_items.id"),
        nullable=False,
    )

    outbound_item_id: Mapped[int] = mapped_column(
        ForeignKey("outbound_items.id"),
        nullable=False,
    )

    quantity_allocated: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )