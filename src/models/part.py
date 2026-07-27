from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Part(Base):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
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