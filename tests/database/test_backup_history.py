from datetime import datetime
import json
from pathlib import Path

import pytest

from src.database.backup_history import (
    register_backup_history,
)


def test_should_register_backup_history(
    tmp_path: Path,
) -> None:
    history_path = (
        tmp_path
        / "backup_history.jsonl"
    )

    register_backup_history(
        history_path=history_path,
        operation="backup",
        status="success",
        details={
            "backup_file": "sigc.db",
        },
        timestamp=datetime(
            2026,
            8,
            14,
            16,
            0,
            0,
        ),
    )

    content = (
        history_path
        .read_text(
            encoding="utf-8"
        )
        .splitlines()
    )

    assert len(content) == 1

    record = json.loads(
        content[0]
    )

    assert record == {
        "timestamp": (
            "2026-08-14T16:00:00"
        ),
        "operation": "BACKUP",
        "status": "SUCCESS",
        "details": {
            "backup_file": "sigc.db",
        },
    }


def test_should_append_history_without_overwriting(
    tmp_path: Path,
) -> None:
    history_path = (
        tmp_path
        / "backup_history.jsonl"
    )

    register_backup_history(
        history_path=history_path,
        operation="BACKUP",
        status="SUCCESS",
    )

    register_backup_history(
        history_path=history_path,
        operation="RESTORE",
        status="FAILED",
    )

    lines = (
        history_path
        .read_text(
            encoding="utf-8"
        )
        .splitlines()
    )

    assert len(lines) == 2

    first = json.loads(
        lines[0]
    )

    second = json.loads(
        lines[1]
    )

    assert (
        first["operation"]
        == "BACKUP"
    )

    assert (
        second["operation"]
        == "RESTORE"
    )

    assert (
        second["status"]
        == "FAILED"
    )


@pytest.mark.parametrize(
    (
        "operation",
        "status",
        "expected_message",
    ),
    [
        (
            "   ",
            "SUCCESS",
            (
                "A operação do histórico "
                "é obrigatória."
            ),
        ),
        (
            "BACKUP",
            "   ",
            (
                "O status do histórico "
                "é obrigatório."
            ),
        ),
    ],
)
def test_should_reject_invalid_history_fields(
    tmp_path: Path,
    operation: str,
    status: str,
    expected_message: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        register_backup_history(
            history_path=(
                tmp_path
                / "history.jsonl"
            ),
            operation=operation,
            status=status,
        )