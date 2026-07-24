from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class OutboundItem(Base):
    __tablename__ = "outbound_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    outbound_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("outbounds.id"),
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

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )