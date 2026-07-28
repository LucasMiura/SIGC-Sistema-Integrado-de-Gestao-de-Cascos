from typing import Final

from src.models.supplier import Supplier
from src.repositories.supplier_repository import SupplierRepository


FIELD_NOT_PROVIDED: Final = object()


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
        """
        Busca um fornecedor pelo identificador.

        Retorna None quando o fornecedor não existe.
        """

        return self.repository.get_by_id(supplier_id)

    def get_required(
        self,
        supplier_id: int,
    ) -> Supplier:
        """
        Busca um fornecedor pelo identificador.

        Lança ValueError quando o fornecedor não existe.
        """

        supplier = self.repository.get_by_id(supplier_id)

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        return supplier

    def list_all(self) -> list[Supplier]:
        """Lista todos os fornecedores."""

        return self.repository.list_all()

    def create(
        self,
        name: str,
        document: str | None = None,
        address: str | None = None,
        notes: str | None = None,
    ) -> Supplier:
        """Cadastra um novo fornecedor."""

        normalized_name = self._normalize_required_text(
            value=name,
            field_name="nome do fornecedor",
        )

        normalized_document = self._normalize_optional_text(
            document
        )
        normalized_address = self._normalize_optional_text(
            address
        )
        normalized_notes = self._normalize_optional_text(
            notes
        )

        self._validate_document_is_available(
            document=normalized_document,
        )

        supplier = Supplier(
            name=normalized_name,
            document=normalized_document,
            address=normalized_address,
            notes=normalized_notes,
            is_active=1,
        )

        return self.repository.add(supplier)

    def update(
        self,
        supplier_id: int,
        *,
        name: str | object = FIELD_NOT_PROVIDED,
        document: str | None | object = FIELD_NOT_PROVIDED,
        address: str | None | object = FIELD_NOT_PROVIDED,
        notes: str | None | object = FIELD_NOT_PROVIDED,
    ) -> Supplier:
        """
        Atualiza somente os campos que foram informados.

        O objeto FIELD_NOT_PROVIDED diferencia um campo ausente
        de um campo enviado explicitamente como None.
        """

        supplier = self.get_required(supplier_id)

        if name is not FIELD_NOT_PROVIDED:
            if not isinstance(name, str):
                raise ValueError(
                    "O nome do fornecedor é obrigatório."
                )

            supplier.name = self._normalize_required_text(
                value=name,
                field_name="nome do fornecedor",
            )

        if document is not FIELD_NOT_PROVIDED:
            if document is not None and not isinstance(
                document,
                str,
            ):
                raise ValueError(
                    "O documento do fornecedor é inválido."
                )

            normalized_document = (
                self._normalize_optional_text(document)
            )

            self._validate_document_is_available(
                document=normalized_document,
                current_supplier_id=supplier.id,
            )

            supplier.document = normalized_document

        if address is not FIELD_NOT_PROVIDED:
            if address is not None and not isinstance(
                address,
                str,
            ):
                raise ValueError(
                    "O endereço do fornecedor é inválido."
                )

            supplier.address = self._normalize_optional_text(
                address
            )

        if notes is not FIELD_NOT_PROVIDED:
            if notes is not None and not isinstance(
                notes,
                str,
            ):
                raise ValueError(
                    "As observações do fornecedor são inválidas."
                )

            supplier.notes = self._normalize_optional_text(
                notes
            )

        return self.repository.save(supplier)

    def deactivate(
        self,
        supplier_id: int,
    ) -> Supplier:
        """Desativa um fornecedor ativo."""

        supplier = self.get_required(supplier_id)

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
        """Ativa um fornecedor inativo."""

        supplier = self.get_required(supplier_id)

        if supplier.is_active:
            raise ValueError(
                "O fornecedor já está ativo."
            )

        supplier.is_active = 1

        return self.repository.save(supplier)

    def _validate_document_is_available(
        self,
        document: str | None,
        current_supplier_id: int | None = None,
    ) -> None:
        """
        Verifica se o documento pode ser utilizado.

        O próprio fornecedor é ignorado durante uma atualização.
        """

        if document is None:
            return

        existing_supplier = self.repository.get_by_document(
            document
        )

        if existing_supplier is None:
            return

        if existing_supplier.id == current_supplier_id:
            return

        raise ValueError(
            "Já existe um fornecedor com este documento."
        )

    @staticmethod
    def _normalize_required_text(
        value: str,
        field_name: str,
    ) -> str:
        """Remove espaços e valida textos obrigatórios."""

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                f"O {field_name} é obrigatório."
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """
        Remove espaços de campos opcionais.

        Textos vazios são convertidos para None.
        """

        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        return normalized_value