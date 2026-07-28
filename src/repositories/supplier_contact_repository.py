from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier_contact import SupplierContact


class SupplierContactRepository:
    """Persistência dos contatos de fornecedores."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        contact_id: int,
    ) -> SupplierContact | None:
        """Busca um contato pelo identificador."""

        statement = select(
            SupplierContact
        ).where(
            SupplierContact.id == contact_id
        )

        return self.session.scalar(statement)

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierContact]:
        """Lista os contatos de um fornecedor."""

        statement = (
            select(SupplierContact)
            .where(
                SupplierContact.supplier_id
                == supplier_id
            )
            .order_by(
                SupplierContact.is_primary.desc(),
                SupplierContact.name,
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def get_primary_by_supplier(
        self,
        supplier_id: int,
    ) -> SupplierContact | None:
        """Busca o contato principal de um fornecedor."""

        statement = select(
            SupplierContact
        ).where(
            SupplierContact.supplier_id
            == supplier_id,
            SupplierContact.is_primary == 1,
        )

        return self.session.scalar(statement)

    def add(
        self,
        contact: SupplierContact,
    ) -> SupplierContact:
        """Adiciona um contato à sessão."""

        self.session.add(contact)
        self.session.flush()

        return contact

    def save(
        self,
        contact: SupplierContact,
    ) -> SupplierContact:
        """Salva alterações realizadas em um contato."""

        self.session.add(contact)
        self.session.flush()

        return contact