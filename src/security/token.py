import os
from datetime import (
    datetime,
    timedelta,
    timezone,
)
from typing import Any

import jwt
from jwt import (
    ExpiredSignatureError,
    InvalidTokenError,
)


ALGORITHM = "HS256"
TOKEN_TYPE = "access"
DEFAULT_ACCESS_TOKEN_MINUTES = 30
MINIMUM_SECRET_LENGTH = 32


class TokenError(ValueError):
    """
    Erro relacionado à criação ou validação
    de tokens de autenticação.
    """


class ExpiredTokenError(TokenError):
    """
    Indica que o token informado expirou.
    """


class InvalidAccessTokenError(TokenError):
    """
    Indica que o token é inválido ou incompatível.
    """


def create_access_token(
    user_id: int,
    role_id: int,
) -> str:
    """
    Cria um token de acesso JWT para um usuário.
    """

    if user_id <= 0:
        raise ValueError(
            (
                "O identificador do usuário deve ser "
                "maior que zero."
            )
        )

    if role_id <= 0:
        raise ValueError(
            (
                "O identificador do perfil deve ser "
                "maior que zero."
            )
        )

    secret_key = _get_secret_key()
    expiration_minutes = (
        _get_access_token_expiration_minutes()
    )

    issued_at = datetime.now(
        timezone.utc
    )

    expires_at = issued_at + timedelta(
        minutes=expiration_minutes
    )

    payload = {
        "sub": str(user_id),
        "role_id": role_id,
        "type": TOKEN_TYPE,
        "iat": issued_at,
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        secret_key,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> dict[str, Any]:
    """
    Valida um token de acesso e retorna
    seus dados internos.
    """

    normalized_token = token.strip()

    if not normalized_token:
        raise InvalidAccessTokenError(
            "Token de acesso inválido."
        )

    try:
        payload = jwt.decode(
            normalized_token,
            _get_secret_key(),
            algorithms=[
                ALGORITHM,
            ],
            options={
                "require": [
                    "sub",
                    "role_id",
                    "type",
                    "iat",
                    "exp",
                ],
            },
        )

    except ExpiredSignatureError as error:
        raise ExpiredTokenError(
            "Token de acesso expirado."
        ) from error

    except InvalidTokenError as error:
        raise InvalidAccessTokenError(
            "Token de acesso inválido."
        ) from error

    if payload.get("type") != TOKEN_TYPE:
        raise InvalidAccessTokenError(
            "Token de acesso inválido."
        )

    user_id = _parse_positive_integer_claim(
        payload.get("sub"),
    )

    role_id = _parse_positive_integer_claim(
        payload.get("role_id"),
    )

    payload["user_id"] = user_id
    payload["role_id"] = role_id

    return payload


def _get_secret_key() -> str:
    """
    Obtém a chave secreta pelas variáveis
    de ambiente.
    """

    secret_key = os.getenv(
        "SIGC_JWT_SECRET_KEY",
        "",
    ).strip()

    if not secret_key:
        raise RuntimeError(
            (
                "A variável SIGC_JWT_SECRET_KEY "
                "não foi configurada."
            )
        )

    if len(secret_key) < MINIMUM_SECRET_LENGTH:
        raise RuntimeError(
            (
                "A variável SIGC_JWT_SECRET_KEY deve "
                "possuir pelo menos 32 caracteres."
            )
        )

    return secret_key


def _get_access_token_expiration_minutes() -> int:
    """
    Obtém o período de validade do token.
    """

    raw_value = os.getenv(
        "SIGC_ACCESS_TOKEN_MINUTES",
        str(DEFAULT_ACCESS_TOKEN_MINUTES),
    ).strip()

    try:
        expiration_minutes = int(
            raw_value
        )

    except ValueError as error:
        raise RuntimeError(
            (
                "A variável "
                "SIGC_ACCESS_TOKEN_MINUTES deve "
                "possuir um número inteiro."
            )
        ) from error

    if expiration_minutes <= 0:
        raise RuntimeError(
            (
                "A variável "
                "SIGC_ACCESS_TOKEN_MINUTES deve "
                "ser maior que zero."
            )
        )

    return expiration_minutes


def _parse_positive_integer_claim(
    value: object,
) -> int:
    """
    Converte e valida um identificador
    armazenado no token.
    """

    try:
        parsed_value = int(
            value
        )

    except (
        TypeError,
        ValueError,
    ) as error:
        raise InvalidAccessTokenError(
            "Token de acesso inválido."
        ) from error

    if parsed_value <= 0:
        raise InvalidAccessTokenError(
            "Token de acesso inválido."
        )

    return parsed_value