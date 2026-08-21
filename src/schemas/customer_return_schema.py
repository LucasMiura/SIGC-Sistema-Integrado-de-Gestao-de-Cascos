from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from src.dtos.customer_return import (
    CustomerReturnOriginDTO,
    CustomerReturnOriginItemDTO,
)

class CustomerReturnType(StrEnum):
    WORK_ORDER = "WORK_ORDER"
    SALE = "SALE"


class CustomerReturnStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class CustomerReturnOriginItemResponse(
    BaseModel
):
    model_config = ConfigDict(
        frozen=True
    )

    part_id: int
    part_code: str
    part_name: str

    outbound_quantity: int
    returned_quantity: int
    pending_quantity: int

    @classmethod
    def from_dto(
        cls,
        dto:
            CustomerReturnOriginItemDTO,
    ) -> (
        "CustomerReturnOriginItemResponse"
    ):
        return cls(
            part_id=dto.part_id,
            part_code=dto.part_code,
            part_name=dto.part_name,
            outbound_quantity=(
                dto.outbound_quantity
            ),
            returned_quantity=(
                dto.returned_quantity
            ),
            pending_quantity=(
                dto.pending_quantity
            ),
        )


class CustomerReturnOriginResponse(
    BaseModel
):
    model_config = ConfigDict(
        frozen=True
    )

    outbound_id: int

    return_type: CustomerReturnType
    reference_number: str
    customer_name: str

    items: list[
        CustomerReturnOriginItemResponse
    ]

    total_outbound_quantity: int
    total_returned_quantity: int
    total_pending_quantity: int

    @classmethod
    def from_dto(
        cls,
        dto:
            CustomerReturnOriginDTO,
    ) -> (
        "CustomerReturnOriginResponse"
    ):
        return cls(
            outbound_id=(
                dto.outbound_id
            ),
            return_type=(
                dto.return_type
            ),
            reference_number=(
                dto.reference_number
            ),
            customer_name=(
                dto.customer_name
            ),
            items=[
                CustomerReturnOriginItemResponse
                .from_dto(item)
                for item in dto.items
            ],
            total_outbound_quantity=(
                dto
                .total_outbound_quantity
            ),
            total_returned_quantity=(
                dto
                .total_returned_quantity
            ),
            total_pending_quantity=(
                dto
                .total_pending_quantity
            ),
        )

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

class CustomerReturnCancelRequest(BaseModel):
    """
    Dados obrigatórios para cancelar
    uma devolução do cliente.
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