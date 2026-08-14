import json
from datetime import datetime
from pathlib import Path
from typing import Any


def register_backup_history(
    *,
    history_path: Path,
    operation: str,
    status: str,
    details: dict[str, Any] | None = None,
    timestamp: datetime | None = None,
) -> None:
    """
    Acrescenta um evento ao histórico
    administrativo de backup/restauração.

    O arquivo utiliza JSON Lines para que
    cada operação permaneça independente.
    """

    normalized_operation = (
        operation.strip().upper()
    )

    if not normalized_operation:
        raise ValueError(
            "A operação do histórico "
            "é obrigatória."
        )

    normalized_status = (
        status.strip().upper()
    )

    if not normalized_status:
        raise ValueError(
            "O status do histórico "
            "é obrigatório."
        )

    effective_timestamp = (
        timestamp
        or datetime.now()
    )

    target_path = Path(
        history_path
    ).resolve()

    target_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    record = {
        "timestamp": (
            effective_timestamp.isoformat()
        ),
        "operation": (
            normalized_operation
        ),
        "status": (
            normalized_status
        ),
        "details": details or {},
    }

    with target_path.open(
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            json.dumps(
                record,
                ensure_ascii=False,
                sort_keys=True,
            )
        )

        file.write("\n")