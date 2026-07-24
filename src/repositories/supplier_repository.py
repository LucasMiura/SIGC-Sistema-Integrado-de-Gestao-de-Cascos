from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier import Supplier


class SupplierRepository:
    """Responsável pela persistência de fornecedores."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, supplier_id: int) -> Supplier | None:
        statement = select(Supplier).where(Supplier.id == supplier_id)
        return self.session.scalar(statement)

    def list_all(self) -> list[Supplier]:
        statement = select(Supplier).order_by(Supplier.name)
        return list(self.session.scalars(statement).all())

    def add(self, supplier: Supplier) -> Supplier:
        self.session.add(supplier)
        self.session.flush()
        return supplier