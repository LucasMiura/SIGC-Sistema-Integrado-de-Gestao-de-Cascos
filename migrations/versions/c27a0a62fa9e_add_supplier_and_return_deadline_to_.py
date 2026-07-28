"""add supplier and return deadline to parts

Revision ID: c27a0a62fa9e
Revises: 6905c4ac94c4
Create Date: 2026-07-28 14:43:09.408031
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op


revision: str = "c27a0a62fa9e"
down_revision: str | Sequence[str] | None = "6905c4ac94c4"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Adiciona fornecedor e prazo de devolução às peças."""

    with op.batch_alter_table(
        "parts",
        schema=None,
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "supplier_id",
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

        batch_op.create_unique_constraint(
            "uq_parts_supplier_id_part_code",
            [
                "supplier_id",
                "part_code",
            ],
        )

        batch_op.create_foreign_key(
            "fk_parts_supplier_id_suppliers",
            "suppliers",
            ["supplier_id"],
            ["id"],
        )


def downgrade() -> None:
    """Remove fornecedor e prazo de devolução das peças."""

    with op.batch_alter_table(
        "parts",
        schema=None,
    ) as batch_op:
        batch_op.drop_constraint(
            "fk_parts_supplier_id_suppliers",
            type_="foreignkey",
        )

        batch_op.drop_constraint(
            "uq_parts_supplier_id_part_code",
            type_="unique",
        )

        batch_op.drop_column(
            "return_deadline_days",
        )

        batch_op.drop_column(
            "supplier_id",
        )