from pydantic import BaseModel, ConfigDict, Field


class SupplierCreateRequest(BaseModel):
    """Dados necessários para cadastrar um fornecedor."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome ou razão social do fornecedor",
        examples=["Distribuidora de Peças Registro Ltda."],
    )

    document: str | None = Field(
        default=None,
        max_length=50,
        description="CPF, CNPJ ou outro documento do fornecedor",
        examples=["12.345.678/0001-90"],
    )

    address: str | None = Field(
        default=None,
        description="Endereço completo do fornecedor",
        examples=[
            "Rua Exemplo, 100 - Centro - Registro/SP"
        ],
    )

    notes: str | None = Field(
        default=None,
        description="Observações sobre o fornecedor",
        examples=[
            "Fornecedor especializado em peças com casco."
        ],
    )


class SupplierUpdateRequest(BaseModel):
    """Dados que podem ser alterados em um fornecedor."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Novo nome ou razão social",
    )

    document: str | None = Field(
        default=None,
        max_length=50,
        description="Novo documento do fornecedor",
    )

    address: str | None = Field(
        default=None,
        description="Novo endereço do fornecedor",
    )

    notes: str | None = Field(
        default=None,
        description="Novas observações sobre o fornecedor",
    )

class SupplierDeactivateRequest(BaseModel):
    """
    Dados obrigatórios para desativar
    um fornecedor.
    """

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
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

class SupplierResponse(BaseModel):
    """Representa um fornecedor retornado pela API."""

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int

    name: str
    document: str | None
    address: str | None
    notes: str | None

    is_active: bool

    created_at: str
    updated_at: str