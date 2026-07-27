from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class SupplierReturnItem(Base):
    __tablename__ = "supplier_return_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_return_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("supplier_returns.id"),
        nullable=False,
    )

    purchase_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("purchase_items.id"),
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