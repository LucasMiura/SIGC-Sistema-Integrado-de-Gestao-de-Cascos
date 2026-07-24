from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    document: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
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
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )