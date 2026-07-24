from src.models.supplier_contact import SupplierContact
from src.repositories.supplier_contact_repository import (
    SupplierContactRepository,
)


class SupplierContactService:
    """Regras de negócio relacionadas aos contatos de fornecedores."""

    def __init__(
        self,
        repository: SupplierContactRepository,
    ):
        self.repository = repository

    def get_by_id(
        self,
        contact_id: int,
    ) -> SupplierContact | None:
        return self.repository.get_by_id(contact_id)

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierContact]:
        return self.repository.list_by_supplier(
            supplier_id
        )

    def create(
        self,
        supplier_id: int,
        name: str,
        email: str | None = None,
        phone: str | None = None,
        position: str | None = None,
        is_primary: int = 0,
    ) -> SupplierContact:
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError(
                "O nome do contato é obrigatório."
            )

        contact = SupplierContact(
            supplier_id=supplier_id,
            name=normalized_name,
            email=email.strip().lower()
            if email
            else None,
            phone=phone.strip()
            if phone
            else None,
            position=position.strip()
            if position
            else None,
            is_primary=is_primary,
            is_active=1,
        )

        return self.repository.add(contact)