from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    purchase_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("purchases.id"),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity_purchased: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    quantity_available: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )