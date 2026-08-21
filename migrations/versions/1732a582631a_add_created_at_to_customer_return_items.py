"""add created at to customer return items

Revision ID: 1732a582631a
Revises: b595fd844049
Create Date: 2026-08-21 17:12:14.604112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1732a582631a'
down_revision: Union[str, Sequence[str], None] = 'b595fd844049'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Adiciona a data de criação aos
    itens de devolução de clientes.
    """

    with op.batch_alter_table(
        "customer_return_items",
        schema=None,
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "created_at",
                sa.String(length=30),
                nullable=True,
            )
        )

    op.execute(
        """
        UPDATE customer_return_items
        SET created_at = strftime(
            '%Y-%m-%dT%H:%M:%f',
            'now'
        )
        WHERE created_at IS NULL
        """
    )

    with op.batch_alter_table(
        "customer_return_items",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "created_at",
            existing_type=sa.String(
                length=30
            ),
            nullable=False,
        )


def downgrade() -> None:
    """
    Remove a data de criação dos
    itens de devolução de clientes.
    """

    with op.batch_alter_table(
        "customer_return_items",
        schema=None,
    ) as batch_op:
        batch_op.drop_column(
            "created_at"
        )