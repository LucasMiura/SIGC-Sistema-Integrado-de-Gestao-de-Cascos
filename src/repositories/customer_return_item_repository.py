from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.customer_return_item import CustomerReturnItem


class CustomerReturnItemRepository:
    """Responsável pela persistência dos itens de devolução."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        customer_return_item_id: int,
    ) -> CustomerReturnItem | None:
        statement = select(CustomerReturnItem).where(
            CustomerReturnItem.id == customer_return_item_id
        )
        return self.session.scalar(statement)

    def list_by_customer_return(
        self,
        customer_return_id: int,
    ) -> list[CustomerReturnItem]:
        statement = (
            select(CustomerReturnItem)
            .where(
                CustomerReturnItem.customer_return_id
                == customer_return_id
            )
            .order_by(CustomerReturnItem.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        item: CustomerReturnItem,
    ) -> CustomerReturnItem:
        self.session.add(item)
        self.session.flush()
        return item