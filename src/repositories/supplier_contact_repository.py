from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier_contact import SupplierContact


class SupplierContactRepository:
    """Responsável pela persistência de contatos de fornecedores."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        contact_id: int,
    ) -> SupplierContact | None:
        statement = select(SupplierContact).where(
            SupplierContact.id == contact_id
        )
        return self.session.scalar(statement)

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierContact]:
        statement = (
            select(SupplierContact)
            .where(SupplierContact.supplier_id == supplier_id)
            .order_by(SupplierContact.name)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        contact: SupplierContact,
    ) -> SupplierContact:
        self.session.add(contact)
        self.session.flush()
        return contact