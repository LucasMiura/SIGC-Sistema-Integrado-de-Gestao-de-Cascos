from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class UserCreateRequest(BaseModel):
    """
    Dados necessários para cadastrar
    um novo usuário.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    full_name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome completo do usuário",
        examples=[
            "Lucas do Nascimento Miura",
        ],
    )

    username: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nome utilizado para acesso",
        examples=[
            "lucas.miura",
        ],
    )

    email: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="E-mail do usuário",
        examples=[
            "lucas@example.com",
        ],
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=200,
        description=(
            "Senha inicial do usuário, com no "
            "mínimo oito caracteres"
        ),
        examples=[
            "SenhaSegura123",
        ],
    )

    role_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador do perfil de acesso"
        ),
        examples=[
            1,
        ],
    )


class UserUpdateRequest(BaseModel):
    """
    Campos cadastrais que podem ser alterados
    por um administrador autorizado.

    A senha não é alterada por este schema.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    full_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Novo nome completo",
    )

    username: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Novo username",
    )

    email: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
        description="Novo e-mail",
    )

    role_id: int | None = Field(
        default=None,
        gt=0,
        description="Novo perfil de acesso",
    )

class UserDeactivateRequest(BaseModel):
    """
    Dados obrigatórios para desativar
    um usuário.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    justification: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description=(
            "Justificativa obrigatória "
            "para a desativação"
        ),
    )


class UserResetPasswordRequest(BaseModel):
    """
    Redefinição administrativa da senha.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    new_password: str = Field(
        ...,
        min_length=8,
        max_length=200,
        description="Nova senha do usuário",
        examples=[
            "NovaSenhaSegura123",
        ],
    )


class UserChangePasswordRequest(BaseModel):
    """
    Alteração da própria senha mediante
    confirmação da senha atual.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    current_password: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Senha atual do usuário",
    )

    new_password: str = Field(
        ...,
        min_length=8,
        max_length=200,
        description="Nova senha desejada",
    )


class UserResponse(BaseModel):
    """
    Representação segura de um usuário.

    O hash da senha nunca é retornado.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    full_name: str
    username: str
    email: str
    role_id: int
    is_active: int
    last_login_at: str | None
    created_at: str
    updated_at: str