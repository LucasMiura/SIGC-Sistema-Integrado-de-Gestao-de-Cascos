from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class RoleCreateRequest(BaseModel):
    """
    Dados necessários para cadastrar
    um perfil de acesso.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Nome do perfil de acesso",
        examples=[
            "Administrador Master",
            "Comprador",
            "Vendedor",
        ],
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
        description=(
            "Descrição das responsabilidades "
            "do perfil"
        ),
        examples=[
            (
                "Perfil responsável pelas operações "
                "administrativas do SIGC."
            ),
        ],
    )


class RoleResponse(BaseModel):
    """
    Representação pública de um perfil.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    name: str
    description: str | None
    created_at: str