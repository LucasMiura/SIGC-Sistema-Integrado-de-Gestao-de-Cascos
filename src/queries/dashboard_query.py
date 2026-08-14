from collections import defaultdict
from datetime import (
    date,
    datetime,
    timedelta,
)

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.dtos.dashboard import (
    DashboardCustomerReturnIndicatorsDTO,
    DashboardDeadlineIndicatorsDTO,
    DashboardSummaryDTO,
    DashboardSupplierReturnIndicatorsDTO,
    DashboardTransferReturnIndicatorsDTO,
)
from src.models.customer_return import (
    CustomerReturn,
)
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import (
    CustomerReturnItem,
)
from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.outbound_transfer_allocation import (
    OutboundTransferAllocation,
)
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.models.supplier import Supplier
from src.models.supplier_return import (
    SupplierReturn,
)
from src.models.supplier_return_item import (
    SupplierReturnItem,
)
from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem
from src.models.transfer_return import (
    TransferReturn,
)
from src.models.transfer_return_item import (
    TransferReturnItem,
)


class DashboardQuery:
    """
    Monta os indicadores consolidados
    utilizados pelo dashboard do SIGC.

    Esta camada é somente leitura.
    """

    ORIGIN_PURCHASE = "PURCHASE"
    ORIGIN_TRANSFER = "TRANSFER"

    DEADLINE_NORMAL = "NORMAL"
    DEADLINE_ATTENTION = "ATTENTION"
    DEADLINE_URGENT = "URGENT"
    DEADLINE_OVERDUE = "OVERDUE"

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_summary(
        self,
        *,
        supplier_id: int | None = None,
        part_id: int | None = None,
        origin_type: str | None = None,
        deadline_status: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> DashboardSummaryDTO:
        """
        Retorna os indicadores gerais
        considerando os filtros informados.
        """

        purchase_rows = []

        if origin_type in (
            None,
            self.ORIGIN_PURCHASE,
        ):
            purchase_rows = (
                self._get_purchase_rows(
                    supplier_id=supplier_id,
                    part_id=part_id,
                    date_from=date_from,
                    date_to=date_to,
                )
            )

        transfer_rows = []

        if origin_type in (
            None,
            self.ORIGIN_TRANSFER,
        ):
            transfer_rows = (
                self._get_transfer_rows(
                    supplier_id=supplier_id,
                    part_id=part_id,
                    date_from=date_from,
                    date_to=date_to,
                )
            )

        purchase_item_ids = [
            purchase_item.id
            for (
                purchase_item,
                _purchase,
                _part,
                _supplier,
            )
            in purchase_rows
        ]

        transfer_item_ids = [
            transfer_item.id
            for (
                transfer_item,
                _transfer,
                _part,
            )
            in transfer_rows
        ]

        (
            outbound_by_purchase,
            outbound_by_transfer,
            returned_by_purchase,
            returned_by_transfer,
        ) = self._get_outbound_and_customer_return_quantities(
            purchase_item_ids=purchase_item_ids,
            transfer_item_ids=transfer_item_ids,
        )

        returned_to_supplier = (
            self._get_supplier_return_quantities(
                purchase_item_ids
            )
        )

        returned_to_origin_branch = (
            self._get_transfer_return_quantities(
                transfer_item_ids
            )
        )

        deadline_quantities = {
            self.DEADLINE_NORMAL: 0,
            self.DEADLINE_ATTENTION: 0,
            self.DEADLINE_URGENT: 0,
            self.DEADLINE_OVERDUE: 0,
        }

        total_origin_count = 0
        total_available_quantity = 0

        total_outbound_quantity = 0
        total_customer_returned = 0
        total_customer_pending = 0

        customer_pending_origin_count = 0
        customer_partial_origin_count = 0
        customer_completed_origin_count = 0

        supplier_available_quantity = 0
        supplier_returned_quantity = 0
        supplier_pending_quantity = 0

        transfer_available_quantity = 0
        transfer_returned_quantity = 0
        transfer_pending_quantity = 0

        today = date.today()

        for (
            purchase_item,
            purchase,
            part,
            _supplier,
        ) in purchase_rows:
            outbound_quantity = (
                outbound_by_purchase.get(
                    purchase_item.id,
                    0,
                )
            )

            customer_returned_quantity = (
                returned_by_purchase.get(
                    purchase_item.id,
                    0,
                )
            )

            supplier_returned = (
                returned_to_supplier.get(
                    purchase_item.id,
                    0,
                )
            )

            pending_customer = max(
                outbound_quantity
                - customer_returned_quantity,
                0,
            )

            available_supplier_return = max(
                customer_returned_quantity
                - supplier_returned,
                0,
            )

            pending_supplier_return = max(
                purchase_item.quantity_purchased
                - supplier_returned,
                0,
            )

            deadline_date = (
                self._parse_date(
                    purchase.issue_date
                )
                + timedelta(
                    days=(
                        part.return_deadline_days
                    )
                )
            )

            resolved_deadline_status = (
                self._resolve_deadline_status(
                    deadline_date=deadline_date,
                    today=today,
                )
            )

            if (
                deadline_status is not None
                and resolved_deadline_status
                != deadline_status
            ):
                continue

            total_origin_count += 1

            total_available_quantity += (
                purchase_item.quantity_available
            )

            total_outbound_quantity += (
                outbound_quantity
            )

            total_customer_returned += (
                customer_returned_quantity
            )

            total_customer_pending += (
                pending_customer
            )


            if outbound_quantity > 0:
                if (
                    customer_returned_quantity
                    <= 0
                ):
                    customer_pending_origin_count += 1

                elif (
                    customer_returned_quantity
                    < outbound_quantity
                ):
                    customer_partial_origin_count += 1

                else:
                    customer_completed_origin_count += 1

            supplier_available_quantity += (
                available_supplier_return
            )

            supplier_returned_quantity += (
                supplier_returned
            )

            supplier_pending_quantity += (
                pending_supplier_return
            )

            if pending_supplier_return > 0:
                deadline_quantities[
                    resolved_deadline_status
                ] += pending_supplier_return

        for (
            transfer_item,
            transfer,
            part,
        ) in transfer_rows:
            outbound_quantity = (
                outbound_by_transfer.get(
                    transfer_item.id,
                    0,
                )
            )

            customer_returned_quantity = (
                returned_by_transfer.get(
                    transfer_item.id,
                    0,
                )
            )

            returned_to_branch = (
                returned_to_origin_branch.get(
                    transfer_item.id,
                    0,
                )
            )

            pending_customer = max(
                outbound_quantity
                - customer_returned_quantity,
                0,
            )

            available_transfer_return = max(
                customer_returned_quantity
                - returned_to_branch,
                0,
            )

            pending_transfer_return = max(
                transfer_item.quantity
                - returned_to_branch,
                0,
            )

            deadline_date = (
                self._parse_date(
                    transfer.issue_date
                )
                + timedelta(
                    days=(
                        transfer_item
                        .return_deadline_days
                    )
                )
            )

            resolved_deadline_status = (
                self._resolve_deadline_status(
                    deadline_date=deadline_date,
                    today=today,
                )
            )

            if (
                deadline_status is not None
                and resolved_deadline_status
                != deadline_status
            ):
                continue

            total_origin_count += 1

            total_available_quantity += (
                transfer_item.quantity_available
            )

            total_outbound_quantity += (
                outbound_quantity
            )

            total_customer_returned += (
                customer_returned_quantity
            )

            total_customer_pending += (
                pending_customer
            )

            if outbound_quantity > 0:
                if (
                    customer_returned_quantity
                    <= 0
                ):
                    customer_pending_origin_count += 1

                elif (
                    customer_returned_quantity
                    < outbound_quantity
                ):
                    customer_partial_origin_count += 1

                else:
                    customer_completed_origin_count += 1

            transfer_available_quantity += (
                available_transfer_return
            )

            transfer_returned_quantity += (
                returned_to_branch
            )

            transfer_pending_quantity += (
                pending_transfer_return
            )

            if pending_transfer_return > 0:
                deadline_quantities[
                    resolved_deadline_status
                ] += pending_transfer_return

        return DashboardSummaryDTO(
            total_origin_count=(
                total_origin_count
            ),
            total_available_quantity=(
                total_available_quantity
            ),
            deadline=(
                DashboardDeadlineIndicatorsDTO(
                    normal_quantity=(
                        deadline_quantities[
                            self.DEADLINE_NORMAL
                        ]
                    ),
                    attention_quantity=(
                        deadline_quantities[
                            self.DEADLINE_ATTENTION
                        ]
                    ),
                    urgent_quantity=(
                        deadline_quantities[
                            self.DEADLINE_URGENT
                        ]
                    ),
                    overdue_quantity=(
                        deadline_quantities[
                            self.DEADLINE_OVERDUE
                        ]
                    ),
                )
            ),
            customer_returns=(
                DashboardCustomerReturnIndicatorsDTO(
                    outbound_quantity=(
                        total_outbound_quantity
                    ),
                    returned_quantity=(
                        total_customer_returned
                    ),
                    pending_quantity=(
                        total_customer_pending
                    ),
                    pending_origin_count=(
                        customer_pending_origin_count
                    ),
                    partial_origin_count=(
                        customer_partial_origin_count
                    ),
                    completed_origin_count=(
                        customer_completed_origin_count
                    ),
                )
            ),
            supplier_returns=(
                DashboardSupplierReturnIndicatorsDTO(
                    available_quantity=(
                        supplier_available_quantity
                    ),
                    returned_quantity=(
                        supplier_returned_quantity
                    ),
                    pending_quantity=(
                        supplier_pending_quantity
                    ),
                )
            ),
            transfer_returns=(
                DashboardTransferReturnIndicatorsDTO(
                    available_quantity=(
                        transfer_available_quantity
                    ),
                    returned_quantity=(
                        transfer_returned_quantity
                    ),
                    pending_quantity=(
                        transfer_pending_quantity
                    ),
                )
            ),
        )

    def _get_purchase_rows(
        self,
        *,
        supplier_id: int | None,
        part_id: int | None,
        date_from: str | None,
        date_to: str | None,
    ) -> list:
        statement = (
            select(
                PurchaseItem,
                Purchase,
                Part,
                Supplier,
            )
            .join(
                Purchase,
                Purchase.id
                == PurchaseItem.purchase_id,
            )
            .join(
                Part,
                Part.id
                == PurchaseItem.part_id,
            )
            .join(
                Supplier,
                Supplier.id
                == Purchase.supplier_id,
            )
            .where(
                Purchase.status != "CANCELLED"
            )
        )

        if supplier_id is not None:
            statement = statement.where(
                Purchase.supplier_id
                == supplier_id
            )

        if part_id is not None:
            statement = statement.where(
                PurchaseItem.part_id
                == part_id
            )

        if date_from is not None:
            statement = statement.where(
                Purchase.issue_date >= date_from
            )

        if date_to is not None:
            statement = statement.where(
                Purchase.issue_date <= date_to
            )

        statement = statement.order_by(
            Purchase.issue_date,
            PurchaseItem.id,
        )

        return list(
            self.session.execute(
                statement
            ).all()
        )

    def _get_transfer_rows(
        self,
        *,
        supplier_id: int | None,
        part_id: int | None,
        date_from: str | None,
        date_to: str | None,
    ) -> list:
        statement = (
            select(
                TransferItem,
                Transfer,
                Part,
            )
            .join(
                Transfer,
                Transfer.id
                == TransferItem.transfer_id,
            )
            .join(
                Part,
                Part.id
                == TransferItem.part_id,
            )
            .where(
                Transfer.status != "CANCELLED"
            )
        )

        if supplier_id is not None:
            statement = statement.where(
                Part.supplier_id
                == supplier_id
            )

        if part_id is not None:
            statement = statement.where(
                TransferItem.part_id
                == part_id
            )

        if date_from is not None:
            statement = statement.where(
                Transfer.issue_date >= date_from
            )

        if date_to is not None:
            statement = statement.where(
                Transfer.issue_date <= date_to
            )

        statement = statement.order_by(
            Transfer.issue_date,
            TransferItem.id,
        )

        return list(
            self.session.execute(
                statement
            ).all()
        )

    def _get_outbound_and_customer_return_quantities(
        self,
        *,
        purchase_item_ids: list[int],
        transfer_item_ids: list[int],
    ) -> tuple[
        dict[int, int],
        dict[int, int],
        dict[int, int],
        dict[int, int],
    ]:
        purchase_allocations = (
            self._get_active_purchase_allocations(
                purchase_item_ids=(
                    purchase_item_ids
                )
            )
        )

        transfer_allocations = (
            self._get_active_transfer_allocations(
                transfer_item_ids=(
                    transfer_item_ids
                )
            )
        )

        outbound_by_purchase: dict[
            int,
            int,
        ] = defaultdict(int)

        outbound_by_transfer: dict[
            int,
            int,
        ] = defaultdict(int)

        outbound_item_ids: set[int] = set()

        for allocation in purchase_allocations:
            outbound_by_purchase[
                allocation.purchase_item_id
            ] += allocation.quantity_allocated

            outbound_item_ids.add(
                allocation.outbound_item_id
            )

        for allocation in transfer_allocations:
            outbound_by_transfer[
                allocation.transfer_item_id
            ] += allocation.quantity_allocated

            outbound_item_ids.add(
                allocation.outbound_item_id
            )

        if not outbound_item_ids:
            return (
                dict(outbound_by_purchase),
                dict(outbound_by_transfer),
                {},
                {},
            )

        all_purchase_allocations = (
            self._get_purchase_allocations_by_outbound(
                outbound_item_ids
            )
        )

        all_transfer_allocations = (
            self._get_transfer_allocations_by_outbound(
                outbound_item_ids
            )
        )

        returned_by_outbound = (
            self._get_customer_return_quantities_by_outbound(
                outbound_item_ids
            )
        )

        purchase_targets = set(
            purchase_item_ids
        )

        transfer_targets = set(
            transfer_item_ids
        )

        returned_by_purchase: dict[
            int,
            int,
        ] = defaultdict(int)

        returned_by_transfer: dict[
            int,
            int,
        ] = defaultdict(int)

        purchase_by_outbound: dict[
            int,
            list[OutboundPurchaseAllocation],
        ] = defaultdict(list)

        transfer_by_outbound: dict[
            int,
            list[OutboundTransferAllocation],
        ] = defaultdict(list)

        for allocation in all_purchase_allocations:
            purchase_by_outbound[
                allocation.outbound_item_id
            ].append(allocation)

        for allocation in all_transfer_allocations:
            transfer_by_outbound[
                allocation.outbound_item_id
            ].append(allocation)

        for outbound_item_id in outbound_item_ids:
            remaining = returned_by_outbound.get(
                outbound_item_id,
                0,
            )

            if remaining <= 0:
                continue

            for allocation in transfer_by_outbound.get(
                outbound_item_id,
                [],
            ):
                if remaining <= 0:
                    break

                returned_quantity = min(
                    remaining,
                    allocation.quantity_allocated,
                )

                if (
                    allocation.transfer_item_id
                    in transfer_targets
                ):
                    returned_by_transfer[
                        allocation.transfer_item_id
                    ] += returned_quantity

                remaining -= returned_quantity

            for allocation in purchase_by_outbound.get(
                outbound_item_id,
                [],
            ):
                if remaining <= 0:
                    break

                returned_quantity = min(
                    remaining,
                    allocation.quantity_allocated,
                )

                if (
                    allocation.purchase_item_id
                    in purchase_targets
                ):
                    returned_by_purchase[
                        allocation.purchase_item_id
                    ] += returned_quantity

                remaining -= returned_quantity

        return (
            dict(outbound_by_purchase),
            dict(outbound_by_transfer),
            dict(returned_by_purchase),
            dict(returned_by_transfer),
        )

    def _get_active_purchase_allocations(
        self,
        *,
        purchase_item_ids: list[int],
    ) -> list[OutboundPurchaseAllocation]:
        if not purchase_item_ids:
            return []

        statement = (
            select(
                OutboundPurchaseAllocation
            )
            .join(
                OutboundItem,
                OutboundItem.id
                == (
                    OutboundPurchaseAllocation
                    .outbound_item_id
                ),
            )
            .join(
                Outbound,
                Outbound.id
                == OutboundItem.outbound_id,
            )
            .where(
                (
                    OutboundPurchaseAllocation
                    .purchase_item_id
                    .in_(purchase_item_ids)
                ),
                Outbound.status
                != "CANCELLED",
            )
            .order_by(
                (
                    OutboundPurchaseAllocation
                    .outbound_item_id
                ),
                OutboundPurchaseAllocation.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def _get_active_transfer_allocations(
        self,
        *,
        transfer_item_ids: list[int],
    ) -> list[OutboundTransferAllocation]:
        if not transfer_item_ids:
            return []

        statement = (
            select(
                OutboundTransferAllocation
            )
            .join(
                OutboundItem,
                OutboundItem.id
                == (
                    OutboundTransferAllocation
                    .outbound_item_id
                ),
            )
            .join(
                Outbound,
                Outbound.id
                == OutboundItem.outbound_id,
            )
            .where(
                (
                    OutboundTransferAllocation
                    .transfer_item_id
                    .in_(transfer_item_ids)
                ),
                Outbound.status
                != "CANCELLED",
            )
            .order_by(
                (
                    OutboundTransferAllocation
                    .outbound_item_id
                ),
                OutboundTransferAllocation.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def _get_purchase_allocations_by_outbound(
        self,
        outbound_item_ids: set[int],
    ) -> list[OutboundPurchaseAllocation]:
        statement = (
            select(
                OutboundPurchaseAllocation
            )
            .where(
                (
                    OutboundPurchaseAllocation
                    .outbound_item_id
                    .in_(outbound_item_ids)
                )
            )
            .order_by(
                (
                    OutboundPurchaseAllocation
                    .outbound_item_id
                ),
                OutboundPurchaseAllocation.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def _get_transfer_allocations_by_outbound(
        self,
        outbound_item_ids: set[int],
    ) -> list[OutboundTransferAllocation]:
        statement = (
            select(
                OutboundTransferAllocation
            )
            .where(
                (
                    OutboundTransferAllocation
                    .outbound_item_id
                    .in_(outbound_item_ids)
                )
            )
            .order_by(
                (
                    OutboundTransferAllocation
                    .outbound_item_id
                ),
                OutboundTransferAllocation.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def _get_customer_return_quantities_by_outbound(
        self,
        outbound_item_ids: set[int],
    ) -> dict[int, int]:
        statement = (
            select(
                CustomerReturnAllocation
            )
            .join(
                CustomerReturnItem,
                CustomerReturnItem.id
                == (
                    CustomerReturnAllocation
                    .customer_return_item_id
                ),
            )
            .join(
                CustomerReturn,
                CustomerReturn.id
                == (
                    CustomerReturnItem
                    .customer_return_id
                ),
            )
            .where(
                (
                    CustomerReturnAllocation
                    .outbound_item_id
                    .in_(outbound_item_ids)
                ),
                CustomerReturn.status
                != "CANCELLED",
            )
            .order_by(
                (
                    CustomerReturnAllocation
                    .outbound_item_id
                ),
                CustomerReturnAllocation.id,
            )
        )

        allocations = list(
            self.session.scalars(
                statement
            ).all()
        )

        quantities: dict[
            int,
            int,
        ] = defaultdict(int)

        for allocation in allocations:
            quantities[
                allocation.outbound_item_id
            ] += allocation.quantity_allocated

        return dict(quantities)

    def _get_supplier_return_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        if not purchase_item_ids:
            return {}

        statement = (
            select(
                SupplierReturnItem
            )
            .join(
                SupplierReturn,
                SupplierReturn.id
                == (
                    SupplierReturnItem
                    .supplier_return_id
                ),
            )
            .where(
                (
                    SupplierReturnItem
                    .purchase_item_id
                    .in_(purchase_item_ids)
                ),
                SupplierReturn.status
                != "CANCELLED",
            )
            .order_by(
                SupplierReturnItem.id
            )
        )

        items = list(
            self.session.scalars(
                statement
            ).all()
        )

        quantities: dict[
            int,
            int,
        ] = defaultdict(int)

        for item in items:
            quantities[
                item.purchase_item_id
            ] += item.quantity

        return dict(quantities)

    def _get_transfer_return_quantities(
        self,
        transfer_item_ids: list[int],
    ) -> dict[int, int]:
        if not transfer_item_ids:
            return {}

        statement = (
            select(
                TransferReturnItem
            )
            .join(
                TransferReturn,
                TransferReturn.id
                == (
                    TransferReturnItem
                    .transfer_return_id
                ),
            )
            .where(
                (
                    TransferReturnItem
                    .transfer_item_id
                    .in_(transfer_item_ids)
                ),
                TransferReturn.status
                != "CANCELLED",
            )
            .order_by(
                TransferReturnItem.id
            )
        )

        items = list(
            self.session.scalars(
                statement
            ).all()
        )

        quantities: dict[
            int,
            int,
        ] = defaultdict(int)

        for item in items:
            quantities[
                item.transfer_item_id
            ] += item.quantity

        return dict(quantities)

    @staticmethod
    def _parse_date(
        value: str,
    ) -> date:
        """
        Converte datas ISO persistidas
        pelo SIGC para date.
        """

        return datetime.fromisoformat(
            value
        ).date()

    @classmethod
    def _resolve_deadline_status(
        cls,
        *,
        deadline_date: date,
        today: date,
    ) -> str:
        """
        Classifica o prazo conforme
        as regras oficiais do SIGC.
        """

        days_remaining = (
            deadline_date - today
        ).days

        if days_remaining < 0:
            return cls.DEADLINE_OVERDUE

        if days_remaining <= 7:
            return cls.DEADLINE_URGENT

        if days_remaining <= 30:
            return cls.DEADLINE_ATTENTION

        return cls.DEADLINE_NORMAL