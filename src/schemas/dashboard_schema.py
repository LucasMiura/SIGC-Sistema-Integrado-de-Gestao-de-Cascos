from pydantic import (
    BaseModel,
    ConfigDict,
)

from src.dtos.dashboard import (
    DashboardSummaryDTO,
)


class DashboardDeadlineIndicatorsResponse(
    BaseModel
):
    """
    Indicadores de quantidade por
    classificação de prazo.
    """

    model_config = ConfigDict(
        frozen=True
    )

    normal_quantity: int
    attention_quantity: int
    urgent_quantity: int
    overdue_quantity: int


class DashboardCustomerReturnIndicatorsResponse(
    BaseModel
):
    """
    Indicadores consolidados das
    devoluções realizadas pelos clientes.
    """

    model_config = ConfigDict(
        frozen=True
    )

    outbound_quantity: int
    returned_quantity: int
    pending_quantity: int

    pending_origin_count: int
    partial_origin_count: int
    completed_origin_count: int


class DashboardSupplierReturnIndicatorsResponse(
    BaseModel
):
    """
    Indicadores das remessas de cascos
    realizadas aos fornecedores.
    """

    model_config = ConfigDict(
        frozen=True
    )

    available_quantity: int
    returned_quantity: int
    pending_quantity: int


class DashboardTransferReturnIndicatorsResponse(
    BaseModel
):
    """
    Indicadores das devoluções de cascos
    às filiais de origem.
    """

    model_config = ConfigDict(
        frozen=True
    )

    available_quantity: int
    returned_quantity: int
    pending_quantity: int


class DashboardSummaryResponse(
    BaseModel
):
    """
    Resposta do dashboard geral do SIGC.
    """

    model_config = ConfigDict(
        frozen=True
    )

    total_origin_count: int
    total_available_quantity: int

    deadline: (
        DashboardDeadlineIndicatorsResponse
    )

    customer_returns: (
        DashboardCustomerReturnIndicatorsResponse
    )

    supplier_returns: (
        DashboardSupplierReturnIndicatorsResponse
    )

    transfer_returns: (
        DashboardTransferReturnIndicatorsResponse
    )

    @classmethod
    def from_dto(
        cls,
        dto: DashboardSummaryDTO,
    ) -> "DashboardSummaryResponse":
        """
        Converte o DTO consolidado em
        resposta pública da API.
        """

        return cls(
            total_origin_count=(
                dto.total_origin_count
            ),
            total_available_quantity=(
                dto.total_available_quantity
            ),
            deadline=(
                DashboardDeadlineIndicatorsResponse(
                    normal_quantity=(
                        dto.deadline
                        .normal_quantity
                    ),
                    attention_quantity=(
                        dto.deadline
                        .attention_quantity
                    ),
                    urgent_quantity=(
                        dto.deadline
                        .urgent_quantity
                    ),
                    overdue_quantity=(
                        dto.deadline
                        .overdue_quantity
                    ),
                )
            ),
            customer_returns=(
                DashboardCustomerReturnIndicatorsResponse(
                    outbound_quantity=(
                        dto.customer_returns
                        .outbound_quantity
                    ),
                    returned_quantity=(
                        dto.customer_returns
                        .returned_quantity
                    ),
                    pending_quantity=(
                        dto.customer_returns
                        .pending_quantity
                    ),
                    pending_origin_count=(
                        dto.customer_returns
                        .pending_origin_count
                    ),
                    partial_origin_count=(
                        dto.customer_returns
                        .partial_origin_count
                    ),
                    completed_origin_count=(
                        dto.customer_returns
                        .completed_origin_count
                    ),
                )
            ),
            supplier_returns=(
                DashboardSupplierReturnIndicatorsResponse(
                    available_quantity=(
                        dto.supplier_returns
                        .available_quantity
                    ),
                    returned_quantity=(
                        dto.supplier_returns
                        .returned_quantity
                    ),
                    pending_quantity=(
                        dto.supplier_returns
                        .pending_quantity
                    ),
                )
            ),
            transfer_returns=(
                DashboardTransferReturnIndicatorsResponse(
                    available_quantity=(
                        dto.transfer_returns
                        .available_quantity
                    ),
                    returned_quantity=(
                        dto.transfer_returns
                        .returned_quantity
                    ),
                    pending_quantity=(
                        dto.transfer_returns
                        .pending_quantity
                    ),
                )
            ),
        )