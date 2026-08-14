from pydantic import BaseModel, ConfigDict, Field


class SupplierContactCreateRequest(BaseModel):
    """Dados necessários para cadastrar um contato."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome do contato",
        examples=["João Silva"],
    )

    email: str | None = Field(
        default=None,
        min_length=3,
        max_length=255,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        description="Endereço de e-mail do contato",
        examples=["joao.silva@fornecedor.com.br"],
    )

    phone: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Telefone do contato",
        examples=["(11) 99999-1111"],
    )

    position: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Cargo ou área do contato",
        examples=["Garantia"],
    )

    is_primary: bool = Field(
        default=False,
        description=(
            "Indica se este é o contato principal "
            "do fornecedor"
        ),
    )


class SupplierContactUpdateRequest(BaseModel):
    """Dados que podem ser alterados em um contato."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Novo nome do contato",
    )

    email: str | None = Field(
        default=None,
        min_length=3,
        max_length=255,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        description="Novo endereço de e-mail",
    )

    phone: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Novo telefone",
    )

    position: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Novo cargo ou área",
    )

    is_primary: bool | None = Field(
        default=None,
        description=(
            "Indica se o contato deve ser considerado "
            "principal"
        ),
    )

class SupplierContactDeactivateRequest(BaseModel):
    """
    Dados obrigatórios para desativar
    um contato de fornecedor.
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


class SupplierContactResponse(BaseModel):
    """Representa um contato retornado pela API."""

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int
    supplier_id: int

    name: str
    email: str | None
    phone: str | None
    position: str | None

    is_primary: bool
    is_active: bool

    created_at: str