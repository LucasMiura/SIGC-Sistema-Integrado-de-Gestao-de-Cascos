from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class CustomerReturnType(StrEnum):
    WORK_ORDER = "WORK_ORDER"
    SALE = "SALE"


class CustomerReturnStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class CustomerReturnCreateRequest(BaseModel):
    """Dados necessários para registrar uma devolução."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    return_type: CustomerReturnType = Field(
        ...,
        description="Tipo da referência original da devolução",
        examples=[
            CustomerReturnType.WORK_ORDER,
            CustomerReturnType.SALE,
        ],
    )

    reference_number: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description=(
            "Número da Ordem de Serviço ou da Nota Fiscal "
            "de venda relacionada à devolução"
        ),
        examples=[
            "OS-12345",
            "NFV-12345",
        ],
    )

    customer_name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome do cliente responsável pela devolução",
        examples=[
            "Transportadora Exemplo Ltda.",
        ],
    )


    status: CustomerReturnStatus = Field(
        default=CustomerReturnStatus.ACTIVE,
        description="Status inicial da devolução",
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description="Observações complementares da devolução",
        examples=[
            "Peça devolvida após avaliação do cliente.",
        ],
    )


class CustomerReturnItemCreateRequest(BaseModel):
    """Dados necessários para adicionar uma peça à devolução."""

    model_config = ConfigDict(
        extra="forbid",
    )

    part_id: int = Field(
        ...,
        gt=0,
        description="Identificador da peça devolvida",
        examples=[
            1,
        ],
    )

    quantity: int = Field(
        ...,
        gt=0,
        description="Quantidade devolvida pelo cliente",
        examples=[
            1,
        ],
    )


class CustomerReturnResponse(BaseModel):
    """Representação de uma devolução de cliente."""

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    return_type: CustomerReturnType
    reference_number: str
    customer_name: str
    created_by: int
    created_at: str
    updated_at: str
    status: CustomerReturnStatus
    notes: str | None


class CustomerReturnItemResponse(BaseModel):
    """Representação de um item de devolução."""

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    customer_return_id: int
    part_id: int
    quantity: int
    created_at: str