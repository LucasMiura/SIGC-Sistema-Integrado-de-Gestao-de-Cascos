from dataclasses import dataclass
from datetime import datetime
from hashlib import sha256
from pathlib import Path
import sqlite3


@dataclass(
    frozen=True,
    slots=True,
)
class BackupResult:
    """
    Resultado de uma operação de backup
    realizada com sucesso.
    """

    backup_path: Path
    created_at: str
    size_bytes: int
    sha256: str
    integrity_status: str


@dataclass(
    frozen=True,
    slots=True,
)
class RestoreResult:
    """
    Resultado de uma restauração realizada
    com sucesso.
    """

    restored_from: Path
    target_path: Path
    safety_backup: BackupResult | None
    restored_at: str
    integrity_status: str


def validate_sqlite_database(
    database_path: Path,
) -> None:
    """
    Valida a integridade de um banco SQLite.

    Levanta ValueError quando o arquivo não
    existe, não é um arquivo ou falha no
    PRAGMA integrity_check.
    """

    normalized_path = Path(
        database_path
    ).resolve()

    if not normalized_path.exists():
        raise ValueError(
            "O banco de dados informado "
            "não foi encontrado."
        )

    if not normalized_path.is_file():
        raise ValueError(
            "O caminho informado não "
            "corresponde a um arquivo."
        )

    connection: sqlite3.Connection | None = None

    try:
        database_uri = (
            normalized_path
            .as_uri()
            + "?mode=ro"
        )

        connection = sqlite3.connect(
            database_uri,
            uri=True,
        )

        result = connection.execute(
            "PRAGMA integrity_check"
        ).fetchone()

    except sqlite3.Error as error:
        raise ValueError(
            "Não foi possível validar "
            "a integridade do banco de dados."
        ) from error

    finally:
        if connection is not None:
            connection.close()

    if (
        result is None
        or str(result[0]).lower() != "ok"
    ):
        raise ValueError(
            "O banco de dados falhou "
            "na verificação de integridade."
        )


def calculate_sha256(
    file_path: Path,
) -> str:
    """
    Calcula SHA-256 do arquivo para permitir
    verificação adicional de identificação
    e integridade do backup.
    """

    digest = sha256()

    with Path(
        file_path
    ).open("rb") as file:
        for chunk in iter(
            lambda: file.read(
                1024 * 1024
            ),
            b"",
        ):
            digest.update(
                chunk
            )

    return digest.hexdigest()


def create_backup(
    *,
    source_path: Path,
    destination_directory: Path,
    timestamp: datetime | None = None,
    filename_prefix: str | None = None,
) -> BackupResult:
    """
    Cria uma cópia consistente do SQLite
    utilizando a API nativa de backup.

    O backup é validado após sua criação.
    """

    source = Path(
        source_path
    ).resolve()

    destination = Path(
        destination_directory
    ).resolve()

    validate_sqlite_database(
        source
    )

    if (
        destination
        == source.parent
    ):
        raise ValueError(
            "O diretório de backup deve ser "
            "diferente do diretório do banco "
            "principal."
        )

    destination.mkdir(
        parents=True,
        exist_ok=True,
    )

    effective_timestamp = (
        timestamp
        or datetime.now()
    )

    timestamp_text = (
        effective_timestamp.strftime(
            "%Y-%m-%d_%H%M%S"
        )
    )

    normalized_prefix = (
        filename_prefix.strip()
        if filename_prefix
        else source.stem
    )

    if not normalized_prefix:
        normalized_prefix = "sigc"

    backup_path = (
        destination
        / (
            f"{normalized_prefix}_"
            f"{timestamp_text}.db"
        )
    )

    if backup_path.exists():
        raise FileExistsError(
            "Já existe um backup com "
            "a mesma identificação."
        )

    source_connection: (
        sqlite3.Connection | None
    ) = None

    destination_connection: (
        sqlite3.Connection | None
    ) = None

    try:
        source_connection = (
            sqlite3.connect(
                source
            )
        )

        destination_connection = (
            sqlite3.connect(
                backup_path
            )
        )

        source_connection.backup(
            destination_connection
        )

        destination_connection.commit()

    except sqlite3.Error as error:
        if backup_path.exists():
            backup_path.unlink(
                missing_ok=True
            )

        raise RuntimeError(
            "Não foi possível criar "
            "o backup do banco de dados."
        ) from error

    finally:
        if (
            destination_connection
            is not None
        ):
            destination_connection.close()

        if source_connection is not None:
            source_connection.close()

    try:
        validate_sqlite_database(
            backup_path
        )

    except ValueError:
        backup_path.unlink(
            missing_ok=True
        )

        raise

    return BackupResult(
        backup_path=backup_path,
        created_at=(
            effective_timestamp.isoformat()
        ),
        size_bytes=(
            backup_path.stat().st_size
        ),
        sha256=calculate_sha256(
            backup_path
        ),
        integrity_status="OK",
    )


def restore_backup(
    *,
    backup_path: Path,
    target_path: Path,
    safety_backup_directory: Path,
    timestamp: datetime | None = None,
) -> RestoreResult:
    """
    Restaura um banco SQLite válido.

    Quando o banco de destino existe,
    cria antes um backup preventivo
    do estado atual.
    """

    source_backup = Path(
        backup_path
    ).resolve()

    target = Path(
        target_path
    ).resolve()

    safety_directory = Path(
        safety_backup_directory
    ).resolve()

    validate_sqlite_database(
        source_backup
    )

    if source_backup == target:
        raise ValueError(
            "O arquivo de backup e o banco "
            "de destino não podem ser "
            "o mesmo arquivo."
        )

    effective_timestamp = (
        timestamp
        or datetime.now()
    )

    safety_backup: BackupResult | None = (
        None
    )

    if target.exists():
        safety_backup = create_backup(
            source_path=target,
            destination_directory=(
                safety_directory
            ),
            timestamp=effective_timestamp,
            filename_prefix=(
                f"{target.stem}_"
                "pre_restore"
            ),
        )

    target.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    source_connection: (
        sqlite3.Connection | None
    ) = None

    target_connection: (
        sqlite3.Connection | None
    ) = None

    try:
        source_connection = (
            sqlite3.connect(
                source_backup
            )
        )

        target_connection = (
            sqlite3.connect(
                target
            )
        )

        source_connection.backup(
            target_connection
        )

        target_connection.commit()

    except sqlite3.Error as error:
        raise RuntimeError(
            "Não foi possível restaurar "
            "o backup do banco de dados."
        ) from error

    finally:
        if target_connection is not None:
            target_connection.close()

        if source_connection is not None:
            source_connection.close()

    validate_sqlite_database(
        target
    )

    return RestoreResult(
        restored_from=source_backup,
        target_path=target,
        safety_backup=safety_backup,
        restored_at=(
            effective_timestamp.isoformat()
        ),
        integrity_status="OK",
    )