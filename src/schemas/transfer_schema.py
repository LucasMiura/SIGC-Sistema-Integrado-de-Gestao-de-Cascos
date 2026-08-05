from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class TransferStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class TransferCreateRequest(BaseModel):
    """
    Dados necessários para registrar
    uma transferência entre filiais.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    origin_branch_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador da filial que forneceu "
            "as peças"
        ),
        examples=[
            2,
        ],
    )

    destination_branch_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador da filial que recebeu "
            "as peças"
        ),
        examples=[
            1,
        ],
    )

    invoice_number: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description=(
            "Número da Nota Fiscal de transferência"
        ),
        examples=[
            "NF-TRANSFER-12345",
        ],
    )

    issue_date: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description=(
            "Data de emissão da Nota Fiscal "
            "de transferência"
        ),
        examples=[
            "2026-08-05",
        ],
    )

    created_by: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador do usuário responsável "
            "pelo lançamento"
        ),
        examples=[
            1,
        ],
    )

    status: TransferStatus = Field(
        default=TransferStatus.ACTIVE,
        description="Status inicial da transferência",
    )


class TransferItemCreateRequest(BaseModel):
    """
    Dados necessários para adicionar uma peça
    recebida por transferência.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    part_id: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador da peça recebida"
        ),
        examples=[
            1,
        ],
    )

    quantity: int = Field(
        ...,
        gt=0,
        description=(
            "Quantidade recebida da filial de origem"
        ),
        examples=[
            10,
        ],
    )

    return_deadline_days: int = Field(
        ...,
        gt=0,
        description=(
            "Prazo específico, em dias, para devolver "
            "os cascos à filial de origem"
        ),
        examples=[
            45,
        ],
    )


class TransferResponse(BaseModel):
    """
    Representação de uma transferência
    entre filiais.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    origin_branch_id: int
    destination_branch_id: int
    invoice_number: str
    issue_date: str
    status: TransferStatus
    created_by: int


class TransferItemResponse(BaseModel):
    """
    Representação de uma peça recebida
    por transferência.
    """

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    transfer_id: int
    part_id: int
    quantity: int
    quantity_available: int
    return_deadline_days: int


class TransferAvailableQuantityResponse(
    BaseModel
):
    """
    Quantidade ainda disponível em uma origem
    recebida por transferência.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    transfer_item_id: int
    available_quantity: int