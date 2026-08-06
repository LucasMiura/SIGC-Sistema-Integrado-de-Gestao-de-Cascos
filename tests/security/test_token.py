import os
from datetime import (
    datetime,
    timedelta,
    timezone,
)

import jwt
import pytest

from src.security.token import (
    ALGORITHM,
    DEFAULT_ACCESS_TOKEN_MINUTES,
    ExpiredTokenError,
    InvalidAccessTokenError,
    create_access_token,
    decode_access_token,
)

@pytest.fixture(autouse=True)
def configure_environment(monkeypatch):
    monkeypatch.setenv(
        "SIGC_JWT_SECRET_KEY",
        "sigc-chave-local-desenvolvimento-2026-segura",
    )

    monkeypatch.setenv(
        "SIGC_ACCESS_TOKEN_MINUTES",
        str(DEFAULT_ACCESS_TOKEN_MINUTES),
    )

def test_should_create_access_token():
    token = create_access_token(
        user_id=15,
        role_id=3,
    )

    assert isinstance(
        token,
        str,
    )

    assert len(token) > 30

def test_should_decode_access_token():
    token = create_access_token(
        user_id=20,
        role_id=5,
    )

    payload = decode_access_token(
        token,
    )

    assert payload["user_id"] == 20
    assert payload["role_id"] == 5
    assert payload["type"] == "access"

def test_should_generate_required_claims():
    token = create_access_token(
        1,
        2,
    )

    payload = jwt.decode(
        token,
        os.environ["SIGC_JWT_SECRET_KEY"],
        algorithms=[
            ALGORITHM,
        ],
    )

    assert "sub" in payload
    assert "role_id" in payload
    assert "iat" in payload
    assert "exp" in payload
    assert "type" in payload

def test_should_reject_invalid_signature():
    token = create_access_token(
        1,
        1,
    )

    invalid = token[:-2] + "AA"

    with pytest.raises(
        InvalidAccessTokenError,
    ):
        decode_access_token(
            invalid,
        )

def test_should_reject_expired_token():
    payload = {
        "sub": "1",
        "role_id": 1,
        "type": "access",
        "iat": datetime.now(
            timezone.utc,
        ) - timedelta(hours=2),
        "exp": datetime.now(
            timezone.utc,
        ) - timedelta(hours=1),
    }

    token = jwt.encode(
        payload,
        os.environ["SIGC_JWT_SECRET_KEY"],
        algorithm=ALGORITHM,
    )

    with pytest.raises(
        ExpiredTokenError,
    ):
        decode_access_token(
            token,
        )

def test_should_reject_refresh_token():
    payload = {
        "sub": "1",
        "role_id": 1,
        "type": "refresh",
        "iat": datetime.now(
            timezone.utc,
        ),
        "exp": datetime.now(
            timezone.utc,
        )
        + timedelta(minutes=10),
    }

    token = jwt.encode(
        payload,
        os.environ["SIGC_JWT_SECRET_KEY"],
        algorithm=ALGORITHM,
    )

    with pytest.raises(
        InvalidAccessTokenError,
    ):
        decode_access_token(
            token,
        )

@pytest.mark.parametrize(
    "user_id",
    [
        0,
        -1,
    ],
)
def test_should_not_create_invalid_user_id(
    user_id,
):
    with pytest.raises(
        ValueError,
    ):
        create_access_token(
            user_id,
            1,
        )

@pytest.mark.parametrize(
    "role_id",
    [
        0,
        -5,
    ],
)
def test_should_not_create_invalid_role_id(
    role_id,
):
    with pytest.raises(
        ValueError,
    ):
        create_access_token(
            1,
            role_id,
        )

def test_should_fail_without_secret_key(
    monkeypatch,
):
    monkeypatch.delenv(
        "SIGC_JWT_SECRET_KEY",
    )

    with pytest.raises(
        RuntimeError,
    ):
        create_access_token(
            1,
            1,
        )

def test_should_fail_when_secret_is_too_short(
    monkeypatch,
):
    monkeypatch.setenv(
        "SIGC_JWT_SECRET_KEY",
        "123",
    )

    with pytest.raises(
        RuntimeError,
    ):
        create_access_token(
            1,
            1,
        )

@pytest.mark.parametrize(
    "value",
    [
        "0",
        "-10",
        "abc",
    ],
)
def test_should_fail_when_expiration_is_invalid(
    monkeypatch,
    value,
):
    monkeypatch.setenv(
        "SIGC_ACCESS_TOKEN_MINUTES",
        value,
    )

    with pytest.raises(
        RuntimeError,
    ):
        create_access_token(
            1,
            1,
        )

