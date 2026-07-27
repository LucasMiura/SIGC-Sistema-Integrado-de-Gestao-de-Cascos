"""create supplier return tables

Revision ID: 6905c4ac94c4
Revises: 3e391eb4855b
Create Date: 2026-07-27 14:41:05.347807

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6905c4ac94c4"
down_revision: Union[str, Sequence[str], None] = "3e391eb4855b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Cria as tabelas de remessas de cascos aos fornecedores."""

    op.create_table(
        "supplier_returns",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "supplier_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "dispatch_invoice_number",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "dispatch_invoice_series",
            sa.String(length=50),
            nullable=True,
        ),
        sa.Column(
            "issue_date",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "notes",
            sa.String(length=1000),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_id"],
            ["suppliers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "supplier_return_items",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "supplier_return_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "purchase_item_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "quantity",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.String(length=30),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["purchase_item_id"],
            ["purchase_items.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_return_id"],
            ["supplier_returns.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Remove as tabelas de remessas aos fornecedores."""

    op.drop_table("supplier_return_items")
    op.drop_table("supplier_returns")