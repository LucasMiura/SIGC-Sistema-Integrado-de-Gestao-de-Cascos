from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.customer_return import CustomerReturn


class CustomerReturnRepository:
    """Responsável pela persistência de devoluções de clientes."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        customer_return_id: int,
    ) -> CustomerReturn | None:
        statement = select(CustomerReturn).where(
            CustomerReturn.id == customer_return_id
        )
        return self.session.scalar(statement)

    def list_all(self) -> list[CustomerReturn]:
        statement = select(CustomerReturn).order_by(
            CustomerReturn.created_at,
            CustomerReturn.id,
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        customer_return: CustomerReturn,
    ) -> CustomerReturn:
        self.session.add(customer_return)
        self.session.flush()
        return customer_return