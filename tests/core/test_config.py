import pytest

from src.core.config import (
    get_cors_origins,
)


def test_should_return_empty_cors_origins_when_not_configured(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(
        "SIGC_CORS_ORIGINS",
        raising=False,
    )

    assert get_cors_origins() == []


def test_should_parse_single_cors_origin(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(
        "SIGC_CORS_ORIGINS",
        "http://localhost:5173",
    )

    assert get_cors_origins() == [
        "http://localhost:5173",
    ]


def test_should_parse_multiple_cors_origins(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(
        "SIGC_CORS_ORIGINS",
        (
            "http://localhost:5173, "
            "http://192.168.0.100:5173"
        ),
    )

    assert get_cors_origins() == [
        "http://localhost:5173",
        "http://192.168.0.100:5173",
    ]


def test_should_remove_trailing_slash_from_cors_origin(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(
        "SIGC_CORS_ORIGINS",
        "http://localhost:5173/",
    )

    assert get_cors_origins() == [
        "http://localhost:5173",
    ]


def test_should_ignore_duplicate_cors_origins(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(
        "SIGC_CORS_ORIGINS",
        (
            "http://localhost:5173,"
            "http://localhost:5173/"
        ),
    )

    assert get_cors_origins() == [
        "http://localhost:5173",
    ]


def test_should_reject_wildcard_cors_origin(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(
        "SIGC_CORS_ORIGINS",
        "*",
    )

    with pytest.raises(
        RuntimeError,
        match=(
            "SIGC_CORS_ORIGINS não deve "
            "utilizar '\\*' como origem."
        ),
    ):
        get_cors_origins()


@pytest.mark.parametrize(
    "origin",
    [
        "localhost:5173",
        "ftp://localhost",
        "qualquer-coisa",
    ],
)
def test_should_reject_invalid_cors_origin(
    monkeypatch: pytest.MonkeyPatch,
    origin: str,
) -> None:
    monkeypatch.setenv(
        "SIGC_CORS_ORIGINS",
        origin,
    )

    with pytest.raises(
        RuntimeError,
        match=(
            "SIGC_CORS_ORIGINS contém "
            "uma origem inválida."
        ),
    ):
        get_cors_origins()