from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class TransferReturnItem(Base):
    """
    Representa uma quantidade de cascos devolvida
    à filial de origem.
    """

    __tablename__ = "transfer_return_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    transfer_return_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transfer_returns.id"),
        nullable=False,
    )

    transfer_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transfer_items.id"),
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