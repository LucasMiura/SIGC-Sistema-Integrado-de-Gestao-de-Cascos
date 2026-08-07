from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class OutboundStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class OutboundCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    destination_type: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Tipo de destino da saída",
        examples=[
            "WORK_ORDER",
            "SALE",
        ],
    )

    work_order_number: str | None = Field(
        default=None,
        max_length=100,
        description="Número da Ordem de Serviço",
        examples=[
            "OS-12345",
        ],
    )

    sales_invoice_number: str | None = Field(
        default=None,
        max_length=100,
        description="Número da Nota Fiscal de venda",
        examples=[
            "NFV-12345",
        ],
    )


    status: OutboundStatus = Field(
        default=OutboundStatus.ACTIVE,
        description="Status inicial da saída",
    )


class OutboundUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    destination_type: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Novo tipo de destino da saída",
        examples=[
            "WORK_ORDER",
            "SALE",
        ],
    )

    work_order_number: str | None = Field(
        default=None,
        max_length=100,
        description="Novo número da Ordem de Serviço",
        examples=[
            "OS-67890",
        ],
    )

    sales_invoice_number: str | None = Field(
        default=None,
        max_length=100,
        description="Novo número da Nota Fiscal de venda",
        examples=[
            "NFV-67890",
        ],
    )

    status: OutboundStatus | None = Field(
        default=None,
        description="Novo status da saída",
    )


class OutboundItemCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    part_id: int = Field(
        ...,
        gt=0,
        description="Identificador da peça",
        examples=[
            1,
        ],
    )

    quantity: int = Field(
        ...,
        gt=0,
        description="Quantidade retirada",
        examples=[
            5,
        ],
    )


class OutboundResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    destination_type: str
    work_order_number: str | None
    sales_invoice_number: str | None
    created_by: int
    created_at: str
    updated_at: str
    status: OutboundStatus


class OutboundItemResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    outbound_id: int
    part_id: int
    quantity: int
    created_at: str