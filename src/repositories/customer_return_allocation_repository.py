from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return import (
    CustomerReturn,
)
from src.models.customer_return_item import (
    CustomerReturnItem,
)

class CustomerReturnAllocationRepository:
    """Responsável pela persistência das alocações de devolução."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        allocation_id: int,
    ) -> CustomerReturnAllocation | None:
        statement = select(
            CustomerReturnAllocation
        ).where(
            CustomerReturnAllocation.id == allocation_id
        )
        return self.session.scalar(statement)

    def list_by_return_item(
        self,
        customer_return_item_id: int,
    ) -> list[CustomerReturnAllocation]:
        statement = (
            select(CustomerReturnAllocation)
            .where(
                CustomerReturnAllocation.customer_return_item_id
                == customer_return_item_id
            )
            .order_by(CustomerReturnAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def list_by_outbound_item(
        self,
        outbound_item_id: int,
    ) -> list[CustomerReturnAllocation]:
        """
        Lista apenas alocações pertencentes
        a devoluções de clientes ativas.

        Alocações canceladas permanecem no banco
        para preservação do histórico.
        """

        statement = (
            select(CustomerReturnAllocation)
            .join(
                CustomerReturnItem,
                (
                    CustomerReturnItem.id
                    == CustomerReturnAllocation
                    .customer_return_item_id
                ),
            )
            .join(
                CustomerReturn,
                (
                    CustomerReturn.id
                    == CustomerReturnItem
                    .customer_return_id
                ),
            )
            .where(
                CustomerReturnAllocation.outbound_item_id
                == outbound_item_id,
                CustomerReturn.status == "ACTIVE",
            )
            .order_by(
                CustomerReturnAllocation.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        allocation: CustomerReturnAllocation,
    ) -> CustomerReturnAllocation:
        self.session.add(allocation)
        self.session.flush()
        return allocation