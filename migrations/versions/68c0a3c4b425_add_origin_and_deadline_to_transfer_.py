"""add stock and deadline to transfer items

Revision ID: 68c0a3c4b425
Revises: c27a0a62fa9e
Create Date: 2026-08-05 09:35:36.108333

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68c0a3c4b425"
down_revision: Union[str, Sequence[str], None] = (
    "c27a0a62fa9e"
)
branch_labels: Union[
    str,
    Sequence[str],
    None,
] = None
depends_on: Union[
    str,
    Sequence[str],
    None,
] = None


def upgrade() -> None:
    """
    Adiciona saldo disponível e prazo específico
    aos itens recebidos por transferência.
    """

    with op.batch_alter_table(
        "transfer_items",
        schema=None,
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "quantity_available",
                sa.Integer(),
                nullable=False,
            )
        )

        batch_op.add_column(
            sa.Column(
                "return_deadline_days",
                sa.Integer(),
                nullable=False,
            )
        )


def downgrade() -> None:
    """
    Remove saldo disponível e prazo específico
    dos itens de transferência.
    """

    with op.batch_alter_table(
        "transfer_items",
        schema=None,
    ) as batch_op:
        batch_op.drop_column(
            "return_deadline_days"
        )

        batch_op.drop_column(
            "quantity_available"
        )