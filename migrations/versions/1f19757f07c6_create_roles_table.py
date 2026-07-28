"""create roles table

Revision ID: 1f19757f07c6
Revises:
Create Date: 2026-07-24 10:09:54.706300
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op


revision: str = "1f19757f07c6"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Cria a tabela de perfis de acesso."""

    op.create_table(
        "roles",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=True,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.String(length=30),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Remove a tabela de perfis de acesso."""

    op.drop_table("roles")