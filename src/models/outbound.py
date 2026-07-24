from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class Outbound(Base):
    __tablename__ = "outbounds"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    destination_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    work_order_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    sales_invoice_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )