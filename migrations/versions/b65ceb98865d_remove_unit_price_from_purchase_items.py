"""remove unit price from purchase items

Revision ID: b65ceb98865d
Revises: 5920bd9270a0
Create Date: 2026-07-24 17:00:31.730691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b65ceb98865d'
down_revision: Union[str, Sequence[str], None] = '5920bd9270a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Remove o campo de preço dos itens de compra."""
    with op.batch_alter_table(
        "purchase_items"
    ) as batch_op:
        batch_op.drop_column("unit_price")


def downgrade() -> None:
    """Restaura o campo de preço dos itens de compra."""
    with op.batch_alter_table(
        "purchase_items"
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "unit_price",
                sa.Numeric(
                    precision=12,
                    scale=2,
                ),
                nullable=False,
            )
        )