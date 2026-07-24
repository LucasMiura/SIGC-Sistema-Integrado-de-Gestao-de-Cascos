from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class CustomerReturn(Base):
    __tablename__ = "customer_returns"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    return_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    reference_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    customer_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    created_by: Mapped[int] = mapped_column(
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

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )