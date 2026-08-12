from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


PurchaseStatus = Literal[
    "PENDING",
    "RECEIVED",
    "CANCELLED",
]


class PurchaseCreateRequest(BaseModel):
    """
    Dados necessários para cadastrar uma compra.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int = Field(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    )

    invoice_number: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Número da nota fiscal",
        examples=["NF-12345"],
    )

    invoice_series: str | None = Field(
        default=None,
        max_length=50,
        description="Série da nota fiscal",
        examples=["1"],
    )

    issue_date: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="Data de emissão da nota fiscal",
        examples=["2026-07-29"],
    )


    status: PurchaseStatus = Field(
        default="PENDING",
        description="Status inicial da compra",
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description="Observações complementares",
    )


class PurchaseUpdateRequest(BaseModel):
    """
    Campos permitidos na atualização de uma compra.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int | None = Field(
        default=None,
        gt=0,
        description="Novo identificador do fornecedor",
    )

    invoice_number: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Novo número da nota fiscal",
    )

    invoice_series: str | None = Field(
        default=None,
        max_length=50,
        description="Nova série da nota fiscal",
    )

    issue_date: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="Nova data de emissão",
    )

    status: PurchaseStatus | None = Field(
        default=None,
        description="Novo status da compra",
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description="Novas observações da compra",
    )


class PurchaseCancelRequest(BaseModel):
    """
    Dados obrigatórios para cancelar
    uma compra.
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
            "para o cancelamento"
        ),
    )


class PurchaseItemCreateRequest(BaseModel):
    """
    Dados para adicionar uma peça à compra.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    part_id: int = Field(
        ...,
        gt=0,
        description="Identificador da peça",
    )

    quantity_purchased: int = Field(
        ...,
        gt=0,
        description="Quantidade comprada",
        examples=[10],
    )


class PurchaseResponse(BaseModel):
    """
    Representa uma compra retornada pela API.
    """

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int
    supplier_id: int

    invoice_number: str
    invoice_series: str | None

    issue_date: str
    received_at: str | None

    notes: str | None

    created_by: int
    created_at: str
    updated_at: str

    status: str


class PurchaseItemResponse(BaseModel):
    """
    Representa um item de compra retornado pela API.
    """

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int
    purchase_id: int
    part_id: int

    quantity_purchased: int
    quantity_available: int

    created_at: str