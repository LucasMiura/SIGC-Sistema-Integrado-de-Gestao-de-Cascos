from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Part(Base):
    """Peça que possui obrigação de devolução de casco."""

    __tablename__ = "parts"

    __table_args__ = (
        UniqueConstraint(
            "supplier_id",
            "part_code",
            name="uq_parts_supplier_id_part_code",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False,
    )

    part_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    return_deadline_days: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_active: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
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