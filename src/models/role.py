from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )