from datetime import datetime


def now_iso() -> str:
    """Retorna a data e hora atual no formato ISO 8601."""
    return datetime.now().isoformat()