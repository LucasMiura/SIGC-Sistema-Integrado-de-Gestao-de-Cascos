import os
from urllib.parse import urlparse


def get_cors_origins() -> list[str]:
    """
    Retorna as origens permitidas para CORS.

    A variável SIGC_CORS_ORIGINS aceita
    múltiplas origens separadas por vírgula.

    Quando não configurada, nenhuma origem
    externa é permitida.
    """

    raw_value = os.getenv(
        "SIGC_CORS_ORIGINS",
        "",
    ).strip()

    if not raw_value:
        return []

    origins: list[str] = []

    for raw_origin in raw_value.split(","):
        origin = (
            raw_origin
            .strip()
            .rstrip("/")
        )

        if not origin:
            continue

        if origin == "*":
            raise RuntimeError(
                "SIGC_CORS_ORIGINS não deve "
                "utilizar '*' como origem."
            )

        parsed = urlparse(
            origin
        )

        if (
            parsed.scheme
            not in {
                "http",
                "https",
            }
            or not parsed.netloc
        ):
            raise RuntimeError(
                "SIGC_CORS_ORIGINS contém "
                "uma origem inválida."
            )

        if origin not in origins:
            origins.append(
                origin
            )

    return origins