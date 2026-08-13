from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class SupplierReturnStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class SupplierReturnCreateRequest(BaseModel):
    """
    Dados necessários para registrar uma remessa
    de cascos ao fornecedor.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador do fornecedor responsável "
            "pela remessa"
        ),
        examples=[
            1,
        ],
    )

    dispatch_invoice_number: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description=(
            "Número da Nota Fiscal de Simples Remessa"
        ),
        examples=[
            "NF-REMESSA-12345",
        ],
    )

    dispatch_invoice_series: str | None = Field(
        default=None,
        max_length=50,
        description=(
            "Série da Nota Fiscal de Simples Remessa"
        ),
        examples=[
            "1",
        ],
    )

    issue_date: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description=(
            "Data de emissão da Nota Fiscal de "
            "Simples Remessa"
        ),
        examples=[
            "2026-08-05",
        ],
    )

    status: SupplierReturnStatus = Field(
        default=SupplierReturnStatus.ACTIVE,
        description="Status inicial da remessa",
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description=(
            "Observações complementares da remessa"
        ),
        examples=[
            (
                "Remessa parcial de cascos vinculada "
                "à Nota Fiscal de compra."
            ),
        ],
    )

class SupplierReturnCancelRequest(BaseModel):
    """
    Dados obrigatórios para cancelar
    uma remessa ao fornecedor.
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


class SupplierReturnItemCreateRequest(BaseModel):
    """
    Dados necessários para adicionar um item
    à remessa ao fornecedor.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    purchase_item_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador do item da compra de origem"
        ),
        examples=[
            1,
        ],
    )

    quantity: int = Field(
        ...,
        gt=0,
        description=(
            "Quantidade de cascos enviada ao fornecedor"
        ),
        examples=[
            4,
        ],
    )


class SupplierReturnResponse(BaseModel):
    """
    Representação de uma remessa de cascos
    ao fornecedor.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    supplier_id: int
    dispatch_invoice_number: str
    dispatch_invoice_series: str | None
    issue_date: str
    created_by: int
    created_at: str
    updated_at: str
    status: SupplierReturnStatus
    notes: str | None


class SupplierReturnItemResponse(BaseModel):
    """
    Representação de um item pertencente
    à remessa ao fornecedor.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    supplier_return_id: int
    purchase_item_id: int
    quantity: int
    created_at: str


class SupplierReturnAvailableQuantityResponse(
    BaseModel
):
    """
    Quantidade de cascos disponível para nova
    remessa em um item de compra.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    purchase_item_id: int
    available_quantity: int