from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class OutboundTransferAllocation(Base):
    """
    Registra a quantidade de um item de saída
    consumida de um item recebido por transferência.
    """

    __tablename__ = (
        "outbound_transfer_allocations"
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    outbound_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("outbound_items.id"),
        nullable=False,
    )

    transfer_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transfer_items.id"),
        nullable=False,
    )

    quantity_allocated: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )