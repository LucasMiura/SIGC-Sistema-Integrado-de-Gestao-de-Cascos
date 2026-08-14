from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class PartCreateRequest(BaseModel):
    """Dados necessários para cadastrar uma peça."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int = Field(
        ...,
        gt=0,
        description="Identificador do fornecedor da peça",
    )

    part_code: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Código original da peça",
        examples=["07C911023H"],
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome da peça",
        examples=["Motor de partida"],
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
        description="Descrição complementar da peça",
    )

    return_deadline_days: int = Field(
        ...,
        gt=0,
        le=3650,
        description=(
            "Prazo padrão, em dias, para devolução "
            "do casco"
        ),
        examples=[90],
    )


class PartUpdateRequest(BaseModel):
    """Campos permitidos na atualização de uma peça."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int | None = Field(
        default=None,
        gt=0,
        description="Identificador do fornecedor da peça",
    )

    part_code: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Código original da peça",
    )

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Nome da peça",
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
        description="Descrição complementar da peça",
    )

    return_deadline_days: int | None = Field(
        default=None,
        gt=0,
        le=3650,
        description=(
            "Prazo padrão, em dias, para devolução "
            "do casco"
        ),
    )

class PartDeactivateRequest(BaseModel):
    """
    Dados obrigatórios para desativar
    uma peça.
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


class PartResponse(BaseModel):
    """Representação pública de uma peça."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    supplier_id: int
    part_code: str
    name: str
    description: str | None
    return_deadline_days: int
    is_active: bool
    created_at: str
    updated_at: str