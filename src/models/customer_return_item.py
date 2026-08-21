from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.core.time import now_iso
from src.database.connection import Base


class CustomerReturnItem(Base):
    __tablename__ = "customer_return_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    customer_return_id: Mapped[int] = mapped_column(
        ForeignKey(
            "customer_returns.id"
        ),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )