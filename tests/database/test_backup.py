from datetime import datetime
from pathlib import Path
import sqlite3

import pytest

from src.database.backup import (
    calculate_sha256,
    create_backup,
    restore_backup,
    validate_sqlite_database,
)


def create_test_database(
    database_path: Path,
    *,
    value: str = "original",
) -> None:
    """
    Cria um SQLite mínimo para os testes.
    """

    connection = sqlite3.connect(
        database_path
    )

    try:
        connection.execute(
            """
            CREATE TABLE test_data (
                id INTEGER PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
        )

        connection.execute(
            """
            INSERT INTO test_data (
                value
            )
            VALUES (?)
            """,
            (
                value,
            ),
        )

        connection.commit()

    finally:
        connection.close()


def read_test_value(
    database_path: Path,
) -> str:
    connection = sqlite3.connect(
        database_path
    )

    try:
        row = connection.execute(
            """
            SELECT value
            FROM test_data
            WHERE id = 1
            """
        ).fetchone()

        assert row is not None

        return str(
            row[0]
        )

    finally:
        connection.close()


def test_should_validate_valid_sqlite_database(
    tmp_path: Path,
) -> None:
    database_path = (
        tmp_path
        / "database.db"
    )

    create_test_database(
        database_path
    )

    validate_sqlite_database(
        database_path
    )


def test_should_reject_missing_database(
    tmp_path: Path,
) -> None:
    database_path = (
        tmp_path
        / "missing.db"
    )

    with pytest.raises(
        ValueError,
        match=(
            "O banco de dados informado "
            "não foi encontrado."
        ),
    ):
        validate_sqlite_database(
            database_path
        )


def test_should_reject_invalid_sqlite_database(
    tmp_path: Path,
) -> None:
    database_path = (
        tmp_path
        / "invalid.db"
    )

    database_path.write_text(
        "arquivo que não é sqlite",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não foi possível validar "
            "a integridade do banco de dados."
        ),
    ):
        validate_sqlite_database(
            database_path
        )


def test_should_create_valid_backup(
    tmp_path: Path,
) -> None:
    database_directory = (
        tmp_path
        / "database"
    )

    backup_directory = (
        tmp_path
        / "backups"
    )

    database_directory.mkdir()

    database_path = (
        database_directory
        / "sigc_dev.db"
    )

    create_test_database(
        database_path,
        value="dado preservado",
    )

    timestamp = datetime(
        2026,
        8,
        14,
        15,
        30,
        45,
    )

    result = create_backup(
        source_path=database_path,
        destination_directory=(
            backup_directory
        ),
        timestamp=timestamp,
    )

    assert result.backup_path == (
        backup_directory
        / (
            "sigc_dev_"
            "2026-08-14_153045.db"
        )
    )

    assert result.backup_path.exists()

    assert (
        read_test_value(
            result.backup_path
        )
        == "dado preservado"
    )

    assert result.integrity_status == "OK"

    assert result.size_bytes > 0

    assert len(
        result.sha256
    ) == 64

    assert result.sha256 == (
        calculate_sha256(
            result.backup_path
        )
    )


def test_should_reject_backup_in_database_directory(
    tmp_path: Path,
) -> None:
    database_path = (
        tmp_path
        / "sigc_dev.db"
    )

    create_test_database(
        database_path
    )

    with pytest.raises(
        ValueError,
        match=(
            "O diretório de backup deve ser "
            "diferente do diretório do banco "
            "principal."
        ),
    ):
        create_backup(
            source_path=database_path,
            destination_directory=tmp_path,
        )


def test_should_not_overwrite_existing_backup(
    tmp_path: Path,
) -> None:
    database_directory = (
        tmp_path
        / "database"
    )

    backup_directory = (
        tmp_path
        / "backups"
    )

    database_directory.mkdir()

    database_path = (
        database_directory
        / "sigc_dev.db"
    )

    create_test_database(
        database_path
    )

    timestamp = datetime(
        2026,
        8,
        14,
        16,
        0,
        0,
    )

    create_backup(
        source_path=database_path,
        destination_directory=(
            backup_directory
        ),
        timestamp=timestamp,
    )

    with pytest.raises(
        FileExistsError,
        match=(
            "Já existe um backup com "
            "a mesma identificação."
        ),
    ):
        create_backup(
            source_path=database_path,
            destination_directory=(
                backup_directory
            ),
            timestamp=timestamp,
        )


def test_should_restore_backup_and_preserve_current_database(
    tmp_path: Path,
) -> None:
    database_directory = (
        tmp_path
        / "database"
    )

    backup_directory = (
        tmp_path
        / "backups"
    )

    safety_directory = (
        tmp_path
        / "safety"
    )

    database_directory.mkdir()

    database_path = (
        database_directory
        / "sigc_dev.db"
    )

    create_test_database(
        database_path,
        value="versao original",
    )

    source_backup_result = create_backup(
        source_path=database_path,
        destination_directory=(
            backup_directory
        ),
        timestamp=datetime(
            2026,
            8,
            14,
            10,
            0,
            0,
        ),
    )

    connection = sqlite3.connect(
        database_path
    )

    try:
        connection.execute(
            """
            UPDATE test_data
            SET value = ?
            WHERE id = 1
            """,
            (
                "versao atual",
            ),
        )

        connection.commit()

    finally:
        connection.close()

    assert (
        read_test_value(
            database_path
        )
        == "versao atual"
    )

    result = restore_backup(
        backup_path=(
            source_backup_result
            .backup_path
        ),
        target_path=database_path,
        safety_backup_directory=(
            safety_directory
        ),
        timestamp=datetime(
            2026,
            8,
            14,
            17,
            0,
            0,
        ),
    )

    assert (
        read_test_value(
            database_path
        )
        == "versao original"
    )

    assert result.integrity_status == "OK"

    assert result.safety_backup is not None

    assert (
        result.safety_backup
        .backup_path
        .exists()
    )

    assert (
        read_test_value(
            result.safety_backup
            .backup_path
        )
        == "versao atual"
    )


def test_should_restore_when_target_does_not_exist(
    tmp_path: Path,
) -> None:
    source_directory = (
        tmp_path
        / "source"
    )

    target_directory = (
        tmp_path
        / "target"
    )

    safety_directory = (
        tmp_path
        / "safety"
    )

    source_directory.mkdir()

    source_database = (
        source_directory
        / "backup.db"
    )

    target_database = (
        target_directory
        / "sigc_dev.db"
    )

    create_test_database(
        source_database,
        value="restaurado",
    )

    result = restore_backup(
        backup_path=source_database,
        target_path=target_database,
        safety_backup_directory=(
            safety_directory
        ),
    )

    assert target_database.exists()

    assert (
        read_test_value(
            target_database
        )
        == "restaurado"
    )

    assert result.safety_backup is None


def test_should_reject_restore_from_invalid_backup(
    tmp_path: Path,
) -> None:
    backup_path = (
        tmp_path
        / "invalid.db"
    )

    target_path = (
        tmp_path
        / "target"
        / "sigc.db"
    )

    backup_path.write_text(
        "conteudo invalido",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError
    ):
        restore_backup(
            backup_path=backup_path,
            target_path=target_path,
            safety_backup_directory=(
                tmp_path
                / "safety"
            ),
        )

    assert not target_path.exists()


def test_should_reject_restoring_database_over_itself(
    tmp_path: Path,
) -> None:
    database_path = (
        tmp_path
        / "database.db"
    )

    create_test_database(
        database_path
    )

    with pytest.raises(
        ValueError,
        match=(
            "O arquivo de backup e o banco "
            "de destino não podem ser "
            "o mesmo arquivo."
        ),
    ):
        restore_backup(
            backup_path=database_path,
            target_path=database_path,
            safety_backup_directory=(
                tmp_path
                / "safety"
            ),
        )