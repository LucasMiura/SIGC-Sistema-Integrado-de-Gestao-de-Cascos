from __future__ import annotations

import argparse
from pathlib import Path
import sys

from src.database.backup import (
    create_backup,
)
from src.database.backup_history import (
    register_backup_history,
)
from src.database.connection import (
    BASE_DIR,
    DATABASE_PATH,
)


DEFAULT_BACKUP_DIRECTORY = (
    BASE_DIR
    / "backups"
)

DEFAULT_HISTORY_PATH = (
    DEFAULT_BACKUP_DIRECTORY
    / "backup_history.jsonl"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Cria um backup consistente "
            "do banco SQLite do SIGC."
        )
    )

    parser.add_argument(
        "--destination",
        type=Path,
        default=DEFAULT_BACKUP_DIRECTORY,
        help=(
            "Diretório de destino. "
            "O padrão é ./backups."
        ),
    )

    return parser


def main() -> int:
    parser = build_parser()

    args = parser.parse_args()

    destination = (
        args.destination.resolve()
    )

    history_path = (
        destination
        / "backup_history.jsonl"
    )

    try:
        result = create_backup(
            source_path=DATABASE_PATH,
            destination_directory=(
                destination
            ),
        )

        register_backup_history(
            history_path=history_path,
            operation="BACKUP",
            status="SUCCESS",
            details={
                "source_database": (
                    DATABASE_PATH.name
                ),
                "backup_file": (
                    result.backup_path.name
                ),
                "size_bytes": (
                    result.size_bytes
                ),
                "sha256": result.sha256,
                "integrity_status": (
                    result.integrity_status
                ),
            },
        )

    except Exception as error:
        try:
            register_backup_history(
                history_path=history_path,
                operation="BACKUP",
                status="FAILED",
                details={
                    "source_database": (
                        DATABASE_PATH.name
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
            "realizar o backup.",
            file=sys.stderr,
        )

        print(
            str(error),
            file=sys.stderr,
        )

        return 1

    print(
        "Backup concluído com sucesso."
    )

    print(
        f"Banco de origem: "
        f"{DATABASE_PATH}"
    )

    print(
        f"Arquivo gerado: "
        f"{result.backup_path}"
    )

    print(
        f"Tamanho: "
        f"{result.size_bytes} bytes"
    )

    print(
        f"SHA-256: "
        f"{result.sha256}"
    )

    print(
        f"Integridade: "
        f"{result.integrity_status}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )