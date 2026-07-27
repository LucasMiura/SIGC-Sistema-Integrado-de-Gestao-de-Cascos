"""fix roles created_at nullable

Revision ID: 3e391eb4855b
Revises: b65ceb98865d
Create Date: 2026-07-27 14:26:17.809017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e391eb4855b'
down_revision: Union[str, Sequence[str], None] = 'b65ceb98865d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        UPDATE roles
        SET created_at = strftime(
            '%Y-%m-%dT%H:%M:%f',
            'now'
        )
        WHERE created_at IS NULL
        """
    )

    with op.batch_alter_table(
        "roles",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "created_at",
            existing_type=sa.String(length=30),
            nullable=False,
        )


def downgrade() -> None:
    with op.batch_alter_table(
        "roles",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "created_at",
            existing_type=sa.String(length=30),
            nullable=True,
        )
    # ### end Alembic commands ###
