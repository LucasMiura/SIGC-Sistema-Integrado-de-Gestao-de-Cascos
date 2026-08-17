from collections.abc import Sequence
from datetime import datetime

import sqlalchemy as sa
from alembic import op


revision: str = "c1d2e3f4a5b6"

down_revision: (
    str
    | Sequence[str]
    | None
) = "fa2ba54d10e3"

branch_labels: (
    str
    | Sequence[str]
    | None
) = None

depends_on: (
    str
    | Sequence[str]
    | None
) = None


DEFAULT_ROLES = (
    (
        "Administrador Master",
        (
            "Perfil responsável pela "
            "administração geral do SIGC."
        ),
    ),
    (
        "Comprador",
        (
            "Perfil responsável por compras, "
            "fornecedores e devoluções."
        ),
    ),
    (
        "Vendedor",
        (
            "Perfil responsável por saídas "
            "e devoluções de clientes."
        ),
    ),
)


def validate_existing_roles() -> None:
    """
    Impede alteração estrutural caso existam
    perfis inválidos ou duplicados.
    """

    connection = op.get_bind()

    invalid_count = connection.execute(
        sa.text(
            """
            SELECT COUNT(*)
            FROM roles
            WHERE name IS NULL
               OR TRIM(name) = ''
            """
        )
    ).scalar_one()

    if invalid_count > 0:
        raise RuntimeError(
            "Existem perfis sem nome válido. "
            "Corrija os registros antes "
            "de executar a migration."
        )

    duplicate = connection.execute(
        sa.text(
            """
            SELECT name
            FROM roles
            GROUP BY name
            HAVING COUNT(*) > 1
            LIMIT 1
            """
        )
    ).scalar_one_or_none()

    if duplicate is not None:
        raise RuntimeError(
            "Existem perfis duplicados. "
            "Corrija os registros antes "
            "de executar a migration."
        )


def seed_default_roles() -> None:
    """
    Garante a existência dos três perfis
    iniciais do SIGC.
    """

    connection = op.get_bind()

    created_at = (
        datetime.now()
        .isoformat(
            timespec="microseconds"
        )
    )

    for (
        name,
        description,
    ) in DEFAULT_ROLES:
        connection.execute(
            sa.text(
                """
                INSERT INTO roles (
                    name,
                    description,
                    created_at
                )
                SELECT
                    :name,
                    :description,
                    :created_at
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM roles
                    WHERE name = :name
                )
                """
            ),
            {
                "name": name,
                "description": description,
                "created_at": created_at,
            },
        )


def upgrade() -> None:
    """
    Fortalece o cadastro de perfis e
    garante os perfis iniciais.
    """

    validate_existing_roles()

    seed_default_roles()

    with op.batch_alter_table(
        "roles",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "name",
            existing_type=sa.String(
                length=100
            ),
            nullable=False,
        )

        batch_op.create_unique_constraint(
            "uq_roles_name",
            [
                "name",
            ],
        )


def downgrade() -> None:
    """
    Remove as restrições estruturais.

    Os perfis não são apagados para evitar
    perda de referências históricas.
    """

    with op.batch_alter_table(
        "roles",
        schema=None,
    ) as batch_op:
        batch_op.drop_constraint(
            "uq_roles_name",
            type_="unique",
        )

        batch_op.alter_column(
            "name",
            existing_type=sa.String(
                length=100
            ),
            nullable=True,
        )