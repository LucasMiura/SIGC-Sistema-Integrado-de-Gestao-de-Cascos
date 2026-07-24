from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class TransferItem(Base):
    __tablename__ = "transfer_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    transfer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transfers.id"),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )