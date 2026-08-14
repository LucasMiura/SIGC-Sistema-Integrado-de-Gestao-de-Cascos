from __future__ import annotations

import argparse
from pathlib import Path
import sqlite3
import sys

from src.api.dependencies.authorization import (
    ROLE_ADMIN,
)
from src.database.backup import (
    calculate_sha256,
    restore_backup,
    validate_sqlite_database,
)
from src.database.backup_history import (
    register_backup_history,
)
from src.database.connection import (
    BASE_DIR,
    DATABASE_PATH,
    SessionLocal,
)
from src.repositories.audit_log_repository import (
    AuditLogRepository,
)
from src.services.audit_service import (
    AuditService,
)


DEFAULT_BACKUP_DIRECTORY = (
    BASE_DIR
    / "backups"
)

DEFAULT_SAFETY_DIRECTORY = (
    DEFAULT_BACKUP_DIRECTORY
    / "pre_restore"
)

DEFAULT_HISTORY_PATH = (
    DEFAULT_BACKUP_DIRECTORY
    / "backup_history.jsonl"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Restaura de forma controlada "
            "um backup SQLite do SIGC."
        )
    )

    parser.add_argument(
        "backup_path",
        type=Path,
        help=(
            "Arquivo .db que será restaurado."
        ),
    )

    parser.add_argument(
        "--user-id",
        type=int,
        required=True,
        help=(
            "ID do Administrador Master "
            "responsável pela restauração."
        ),
    )

    parser.add_argument(
        "--justification",
        type=str,
        required=True,
        help=(
            "Justificativa administrativa "
            "da restauração."
        ),
    )

    parser.add_argument(
        "--yes",
        action="store_true",
        help=(
            "Confirma a restauração sem "
            "solicitar confirmação interativa."
        ),
    )

    return parser


def validate_restore_actor(
    *,
    backup_path: Path,
    user_id: int,
) -> None:
    """
    Confirma que o usuário responsável
    existe e é Administrador Master
    dentro do backup a ser restaurado.
    """

    if user_id <= 0:
        raise ValueError(
            "O identificador do usuário "
            "deve ser maior que zero."
        )

    database_path = (
        backup_path.resolve()
    )

    database_uri = (
        database_path.as_uri()
        + "?mode=ro"
    )

    connection: (
        sqlite3.Connection | None
    ) = None

    try:
        connection = sqlite3.connect(
            database_uri,
            uri=True,
        )

        row = connection.execute(
            """
            SELECT
                users.id,
                roles.name,
                users.is_active
            FROM users
            INNER JOIN roles
                ON roles.id = users.role_id
            WHERE users.id = ?
            """,
            (
                user_id,
            ),
        ).fetchone()

    except sqlite3.Error as error:
        raise ValueError(
            "Não foi possível validar "
            "o usuário responsável dentro "
            "do backup."
        ) from error

    finally:
        if connection is not None:
            connection.close()

    if row is None:
        raise ValueError(
            "O usuário responsável não existe "
            "no backup informado."
        )

    _actor_id, role_name, is_active = row

    if role_name != ROLE_ADMIN:
        raise ValueError(
            "A restauração deve ser realizada "
            "por um Administrador Master."
        )

    if int(is_active) != 1:
        raise ValueError(
            "O Administrador Master informado "
            "está inativo no backup."
        )


def register_restore_audit(
    *,
    user_id: int,
    backup_path: Path,
    safety_backup_path: Path | None,
    justification: str,
) -> None:
    """
    Registra a restauração dentro do
    banco que acabou de ser restaurado.
    """

    session = SessionLocal()

    try:
        repository = AuditLogRepository(
            session
        )

        service = AuditService(
            repository
        )

        old_values = None

        if safety_backup_path is not None:
            old_values = {
                "safety_backup_file": (
                    safety_backup_path.name
                ),
            }

        service.register(
            user_id=user_id,
            action="RESTORE",
            module="DATABASE",
            entity_type="Database",
            entity_id=1,
            description=(
                "Banco de dados restaurado "
                "a partir de backup."
            ),
            old_values=old_values,
            new_values={
                "backup_file": (
                    backup_path.name
                ),
                "backup_sha256": (
                    calculate_sha256(
                        backup_path
                    )
                ),
                "integrity_status": "OK",
            },
            justification=justification,
        )

        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


def confirm_restore() -> bool:
    """
    Exige confirmação textual para reduzir
    o risco de restauração acidental.
    """

    print()
    print(
        "ATENÇÃO: a restauração substituirá "
        "o conteúdo atual do banco."
    )

    print(
        "A aplicação SIGC deve estar parada "
        "antes desta operação."
    )

    print()

    confirmation = input(
        "Digite RESTAURAR para confirmar: "
    )

    return (
        confirmation.strip().upper()
        == "RESTAURAR"
    )


def main() -> int:
    parser = build_parser()

    args = parser.parse_args()

    backup_path = (
        args.backup_path.resolve()
    )

    justification = (
        args.justification.strip()
    )

    history_path = (
        DEFAULT_HISTORY_PATH
    )

    if not justification:
        print(
            "ERRO: a justificativa "
            "é obrigatória.",
            file=sys.stderr,
        )

        return 1

    try:
        validate_sqlite_database(
            backup_path
        )

        validate_restore_actor(
            backup_path=backup_path,
            user_id=args.user_id,
        )

        if (
            not args.yes
            and not confirm_restore()
        ):
            print(
                "Restauração cancelada "
                "pelo operador."
            )

            register_backup_history(
                history_path=history_path,
                operation="RESTORE",
                status="CANCELLED",
                details={
                    "backup_file": (
                        backup_path.name
                    ),
                    "user_id": (
                        args.user_id
                    ),
                },
            )

            return 0

        result = restore_backup(
            backup_path=backup_path,
            target_path=DATABASE_PATH,
            safety_backup_directory=(
                DEFAULT_SAFETY_DIRECTORY
            ),
        )

        safety_backup_path = None

        if result.safety_backup is not None:
            safety_backup_path = (
                result
                .safety_backup
                .backup_path
            )

        register_restore_audit(
            user_id=args.user_id,
            backup_path=backup_path,
            safety_backup_path=(
                safety_backup_path
            ),
            justification=justification,
        )

        register_backup_history(
            history_path=history_path,
            operation="RESTORE",
            status="SUCCESS",
            details={
                "backup_file": (
                    backup_path.name
                ),
                "target_database": (
                    DATABASE_PATH.name
                ),
                "user_id": (
                    args.user_id
                ),
                "safety_backup_file": (
                    (
                        safety_backup_path.name
                    )
                    if safety_backup_path
                    is not None
                    else None
                ),
                "integrity_status": (
                    result.integrity_status
                ),
            },
        )

    except Exception as error:
        try:
            register_backup_history(
                history_path=history_path,
                operation="RESTORE",
                status="FAILED",
                details={
                    "backup_file": (
                        backup_path.name
                    ),
                    "target_database": (
                        DATABASE_PATH.name
                    ),
                    "user_id": (
                        args.user_id
                    ),
                    "error_type": (
                        type(error).__name__
                    ),
                    "error": str(error),
                },
            )

        except Exception:
            pass

        print(
            "ERRO: não foi possível "
            "concluir a restauração.",
            file=sys.stderr,
        )

        print(
            str(error),
            file=sys.stderr,
        )

        return 1

    print()
    print(
        "Restauração concluída com sucesso."
    )

    print(
        f"Backup utilizado: "
        f"{result.restored_from}"
    )

    print(
        f"Banco restaurado: "
        f"{result.target_path}"
    )

    if result.safety_backup is not None:
        print(
            "Backup preventivo: "
            f"{result.safety_backup.backup_path}"
        )

    print(
        f"Integridade: "
        f"{result.integrity_status}"
    )

    print(
        "Evento registrado na auditoria."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )