from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class TransferReturnStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class TransferReturnCreateRequest(BaseModel):
    """
    Dados necessários para registrar uma remessa
    de cascos devolvida à filial de origem.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    transfer_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador da transferência de entrada "
            "que originou os cascos"
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
            "Número da Nota Fiscal de Simples Remessa "
            "emitida para a filial de origem"
        ),
        examples=[
            "NF-DEV-FILIAL-12345",
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
            "Data de emissão da Nota Fiscal "
            "de Simples Remessa"
        ),
        examples=[
            "2026-08-05",
        ],
    )

    status: TransferReturnStatus = Field(
        default=TransferReturnStatus.ACTIVE,
        description=(
            "Status inicial da devolução à filial"
        ),
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description=(
            "Observações complementares da devolução"
        ),
        examples=[
            (
                "Devolução parcial dos cascos "
                "recebidos por transferência."
            ),
        ],
    )


class TransferReturnItemCreateRequest(BaseModel):
    """
    Dados necessários para adicionar um item
    à devolução para a filial de origem.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    transfer_item_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador do item recebido "
            "por transferência"
        ),
        examples=[
            1,
        ],
    )

    quantity: int = Field(
        ...,
        gt=0,
        description=(
            "Quantidade de cascos devolvida "
            "à filial de origem"
        ),
        examples=[
            4,
        ],
    )


class TransferReturnResponse(BaseModel):
    """
    Representação de uma devolução de cascos
    para a filial de origem.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    transfer_id: int
    dispatch_invoice_number: str
    dispatch_invoice_series: str | None
    issue_date: str
    created_by: int
    created_at: str
    updated_at: str
    status: TransferReturnStatus
    notes: str | None


class TransferReturnItemResponse(BaseModel):
    """
    Representação de um item pertencente
    à devolução para a filial.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    transfer_return_id: int
    transfer_item_id: int
    quantity: int
    created_at: str


class TransferReturnAvailableQuantityResponse(
    BaseModel
):
    """
    Quantidade de cascos ainda disponível
    para devolução à filial de origem.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    transfer_item_id: int
    available_quantity: int