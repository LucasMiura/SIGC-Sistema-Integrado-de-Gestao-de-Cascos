from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class TransferReturn(Base):
    """
    Representa uma remessa de cascos devolvida
    à filial que forneceu as peças.
    """

    __tablename__ = "transfer_returns"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    transfer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transfers.id"),
        nullable=False,
    )

    dispatch_invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    dispatch_invoice_series: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    issue_date: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )