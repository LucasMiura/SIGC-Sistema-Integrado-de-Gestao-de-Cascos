"""add customer name to outbounds

Revision ID: b595fd844049
Revises: c1d2e3f4a5b6
Create Date: 2026-08-21 09:04:59.479323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b595fd844049'
down_revision: Union[str, Sequence[str], None] = 'c1d2e3f4a5b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Adiciona a identificação simplificada
    do cliente às saídas.
    """

    with op.batch_alter_table(
        "outbounds",
        schema=None,
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "customer_name",
                sa.String(length=200),
                nullable=True,
            )
        )

    op.execute(
        """
        UPDATE outbounds
        SET customer_name = 'Não informado'
        WHERE customer_name IS NULL
           OR TRIM(customer_name) = ''
        """
    )

    with op.batch_alter_table(
        "outbounds",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "customer_name",
            existing_type=sa.String(
                length=200
            ),
            nullable=False,
        )


def upgrade() -> None:
    """
    Adiciona a identificação simplificada
    do cliente às saídas.
    """

    with op.batch_alter_table(
        "outbounds",
        schema=None,
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "customer_name",
                sa.String(length=200),
                nullable=True,
            )
        )

    op.execute(
        """
        UPDATE outbounds
        SET customer_name = 'Não informado'
        WHERE customer_name IS NULL
           OR TRIM(customer_name) = ''
        """
    )

    with op.batch_alter_table(
        "outbounds",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "customer_name",
            existing_type=sa.String(
                length=200
            ),
            nullable=False,
        )


def downgrade() -> None:
    """
    Remove a identificação simplificada
    do cliente das saídas.
    """

    with op.batch_alter_table(
        "outbounds",
        schema=None,
    ) as batch_op:
        batch_op.drop_column(
            "customer_name"
        )