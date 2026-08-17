from unittest.mock import Mock

from src.database.connection import (
    enable_sqlite_foreign_keys,
    engine,
)


def test_should_enable_sqlite_foreign_keys() -> None:
    connection = Mock()

    cursor = Mock()

    connection.cursor.return_value = (
        cursor
    )

    enable_sqlite_foreign_keys(
        connection,
        Mock(),
    )

    cursor.execute.assert_called_once_with(
        "PRAGMA foreign_keys = ON"
    )

    cursor.close.assert_called_once_with()


def test_application_engine_should_have_foreign_keys_enabled() -> None:
    if engine.dialect.name != "sqlite":
        return

    with engine.connect() as connection:
        result = (
            connection
            .exec_driver_sql(
                "PRAGMA foreign_keys"
            )
            .scalar_one()
        )

    assert result == 1