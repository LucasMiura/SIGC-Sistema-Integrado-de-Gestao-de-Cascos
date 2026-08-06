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


class LoginResponse(BaseModel):
    """
    Resposta retornada após autenticação.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    access_token: str
    token_type: str
    user: UserResponse