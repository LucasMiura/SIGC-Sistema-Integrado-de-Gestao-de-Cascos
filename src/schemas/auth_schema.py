from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from src.schemas.user_schema import (
    UserResponse,
)


class LoginRequest(BaseModel):
    """
    Credenciais utilizadas no login.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    login: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description=(
            "Username ou e-mail do usuário"
        ),
        examples=[
            "lucas.miura",
            "lucas@example.com",
        ],
    )

    password: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Senha do usuário",
        examples=[
            "SenhaSegura123",
        ],
    )


class AuthenticatedSessionResponse(BaseModel):
    """
    Representa a sessão autenticada atual.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    user: UserResponse
    role_name: str


class LoginResponse(
    AuthenticatedSessionResponse
):
    """
    Resposta retornada após autenticação.
    """

    access_token: str
    token_type: str