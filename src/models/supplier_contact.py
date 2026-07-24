from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class SupplierContact(Base):
    __tablename__ = "supplier_contacts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    position: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    is_primary: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
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