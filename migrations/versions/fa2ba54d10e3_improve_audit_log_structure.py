"""improve audit log structure

Revision ID: fa2ba54d10e3
Revises: 75c9aad59603
Create Date: 2026-08-10 14:15:06.996405

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fa2ba54d10e3"
down_revision: Union[
    str,
    Sequence[str],
    None,
] = "75c9aad59603"

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
    Adiciona a descrição da operação
    e vincula o usuário da auditoria
    à tabela de usuários.
    """

    with op.batch_alter_table(
        "audit_logs"
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "description",
                sa.Text(),
                nullable=True,
            )
        )

        batch_op.create_foreign_key(
            "fk_audit_logs_user_id_users",
            "users",
            ["user_id"],
            ["id"],
        )


def downgrade() -> None:
    """
    Remove a chave estrangeira e
    o campo de descrição da auditoria.
    """

    with op.batch_alter_table(
        "audit_logs"
    ) as batch_op:
        batch_op.drop_constraint(
            "fk_audit_logs_user_id_users",
            type_="foreignkey",
        )

        batch_op.drop_column(
            "description"
        )