from src.models.supplier import Supplier
from src.repositories.supplier_repository import SupplierRepository


class SupplierService:
    """Regras de negócio relacionadas a fornecedores."""

    def __init__(
        self,
        repository: SupplierRepository,
    ):
        self.repository = repository

    def get_by_id(
        self,
        supplier_id: int,
    ) -> Supplier | None:
        return self.repository.get_by_id(supplier_id)

    def list_all(self) -> list[Supplier]:
        return self.repository.list_all()

    def create(
        self,
        name: str,
        document: str | None = None,
        address: str | None = None,
        notes: str | None = None,
    ) -> Supplier:
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError(
                "O nome do fornecedor é obrigatório."
            )

        normalized_document = (
            document.strip()
            if document
            else None
        )

        if normalized_document:
            existing_supplier = (
                self.repository.get_by_document(
                    normalized_document
                )
            )

            if existing_supplier is not None:
                raise ValueError(
                    "Já existe um fornecedor com este documento."
                )

        supplier = Supplier(
            name=normalized_name,
            document=normalized_document,
            address=address,
            notes=notes,
            is_active=1,
        )

        return self.repository.add(supplier)

    def deactivate(
        self,
        supplier_id: int,
    ) -> Supplier:
        supplier = self.repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        if not supplier.is_active:
            raise ValueError(
                "O fornecedor já está inativo."
            )

        supplier.is_active = 0

        return self.repository.save(supplier)

    def activate(
        self,
        supplier_id: int,
    ) -> Supplier:
        supplier = self.repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        if supplier.is_active:
            raise ValueError(
                "O fornecedor já está ativo."
            )

        supplier.is_active = 1

        return self.repository.save(supplier)