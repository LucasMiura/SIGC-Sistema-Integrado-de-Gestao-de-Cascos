import os
from collections.abc import Generator
from pathlib import Path
from typing import Any

from sqlalchemy import (
    create_engine,
    event,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Session,
    sessionmaker,
)


BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE_DIR = BASE_DIR / "data"
DATABASE_DIR.mkdir(
    exist_ok=True
)

DEFAULT_DATABASE_PATH = (
    DATABASE_DIR
    / "sigc_dev.db"
)

DEFAULT_DATABASE_URL = (
    f"sqlite:///{DEFAULT_DATABASE_PATH}"
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    DEFAULT_DATABASE_URL,
)


def build_connect_args(
    database_url: str,
) -> dict[str, Any]:
    """
    Retorna argumentos específicos para
    a tecnologia de banco utilizada.
    """

    if database_url.startswith(
        "sqlite:"
    ):
        return {
            "check_same_thread": False,
        }

    return {}


engine = create_engine(
    DATABASE_URL,
    connect_args=build_connect_args(
        DATABASE_URL
    ),
)


def enable_sqlite_foreign_keys(
    dbapi_connection: Any,
    _connection_record: Any,
) -> None:
    """
    Ativa a validação de chaves estrangeiras
    em cada nova conexão SQLite.
    """

    cursor = (
        dbapi_connection.cursor()
    )

    try:
        cursor.execute(
            "PRAGMA foreign_keys = ON"
        )

    finally:
        cursor.close()


if engine.dialect.name == "sqlite":
    event.listen(
        engine,
        "connect",
        enable_sqlite_foreign_keys,
    )


if (
    engine.dialect.name == "sqlite"
    and engine.url.database
):
    DATABASE_PATH = Path(
        engine.url.database
    ).resolve()

else:
    DATABASE_PATH = (
        DEFAULT_DATABASE_PATH
    )


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


def get_session() -> Generator[
    Session,
    None,
    None,
]:
    """
    Fornece uma sessão do banco para cada
    requisição da API.

    A sessão é sempre fechada ao final da
    requisição, mesmo quando ocorre algum erro.
    """

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()