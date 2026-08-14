from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class DashboardDeadlineIndicatorsDTO:
    """
    Quantidades pendentes classificadas
    pelo prazo de devolução.
    """

    normal_quantity: int
    attention_quantity: int
    urgent_quantity: int
    overdue_quantity: int


@dataclass(
    frozen=True,
    slots=True,
)
class DashboardCustomerReturnIndicatorsDTO:
    """
    Indicadores consolidados das devoluções
    realizadas pelos clientes.
    """

    outbound_quantity: int
    returned_quantity: int
    pending_quantity: int

    pending_origin_count: int
    partial_origin_count: int
    completed_origin_count: int


@dataclass(
    frozen=True,
    slots=True,
)
class DashboardSupplierReturnIndicatorsDTO:
    """
    Indicadores das devoluções de cascos
    aos fornecedores.
    """

    available_quantity: int
    returned_quantity: int
    pending_quantity: int


@dataclass(
    frozen=True,
    slots=True,
)
class DashboardTransferReturnIndicatorsDTO:
    """
    Indicadores das devoluções de cascos
    às filiais de origem.
    """

    available_quantity: int
    returned_quantity: int
    pending_quantity: int


@dataclass(
    frozen=True,
    slots=True,
)
class DashboardSummaryDTO:
    """
    Visão consolidada utilizada pelo
    dashboard geral do SIGC.
    """

    total_origin_count: int
    total_available_quantity: int

    deadline: DashboardDeadlineIndicatorsDTO

    customer_returns: (
        DashboardCustomerReturnIndicatorsDTO
    )

    supplier_returns: (
        DashboardSupplierReturnIndicatorsDTO
    )

    transfer_returns: (
        DashboardTransferReturnIndicatorsDTO
    )