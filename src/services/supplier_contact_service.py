from typing import Final

from src.models.supplier_contact import SupplierContact
from src.repositories.supplier_contact_repository import (
    SupplierContactRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)


FIELD_NOT_PROVIDED: Final = object()


class SupplierContactService:
    """Regras de negócio dos contatos de fornecedores."""

    def __init__(
        self,
        repository: SupplierContactRepository,
        supplier_repository: SupplierRepository,
    ):
        self.repository = repository
        self.supplier_repository = supplier_repository

    def get_by_id(
        self,
        contact_id: int,
    ) -> SupplierContact | None:
        """Busca um contato pelo identificador."""

        return self.repository.get_by_id(contact_id)

    def get_required(
        self,
        supplier_id: int,
        contact_id: int,
    ) -> SupplierContact:
        """
        Busca obrigatoriamente um contato pertencente
        ao fornecedor informado.
        """

        self._validate_supplier_exists(supplier_id)

        contact = self.repository.get_by_id(contact_id)

        if contact is None:
            raise ValueError(
                "Contato não encontrado."
            )

        if contact.supplier_id != supplier_id:
            raise ValueError(
                "O contato não pertence ao fornecedor informado."
            )

        return contact

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierContact]:
        """Lista os contatos do fornecedor informado."""

        self._validate_supplier_exists(supplier_id)

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
        is_primary: bool = False,
    ) -> SupplierContact:
        """Cadastra um contato para um fornecedor."""

        self._validate_supplier_exists(supplier_id)

        normalized_name = self._normalize_required_text(
            value=name,
            field_name="nome do contato",
        )

        normalized_email = self._normalize_email(email)
        normalized_phone = self._normalize_optional_text(
            phone
        )
        normalized_position = self._normalize_optional_text(
            position
        )

        if is_primary:
            self._remove_current_primary(supplier_id)

        contact = SupplierContact(
            supplier_id=supplier_id,
            name=normalized_name,
            email=normalized_email,
            phone=normalized_phone,
            position=normalized_position,
            is_primary=int(is_primary),
            is_active=1,
        )

        return self.repository.add(contact)

    def update(
        self,
        supplier_id: int,
        contact_id: int,
        *,
        name: str | object = FIELD_NOT_PROVIDED,
        email: str | None | object = FIELD_NOT_PROVIDED,
        phone: str | None | object = FIELD_NOT_PROVIDED,
        position: str | None | object = FIELD_NOT_PROVIDED,
        is_primary: bool | object = FIELD_NOT_PROVIDED,
    ) -> SupplierContact:
        """Atualiza somente os campos enviados."""

        contact = self.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        if name is not FIELD_NOT_PROVIDED:
            if not isinstance(name, str):
                raise ValueError(
                    "O nome do contato é obrigatório."
                )

            contact.name = self._normalize_required_text(
                value=name,
                field_name="nome do contato",
            )

        if email is not FIELD_NOT_PROVIDED:
            if email is not None and not isinstance(
                email,
                str,
            ):
                raise ValueError(
                    "O e-mail do contato é inválido."
                )

            contact.email = self._normalize_email(email)

        if phone is not FIELD_NOT_PROVIDED:
            if phone is not None and not isinstance(
                phone,
                str,
            ):
                raise ValueError(
                    "O telefone do contato é inválido."
                )

            contact.phone = self._normalize_optional_text(
                phone
            )

        if position is not FIELD_NOT_PROVIDED:
            if position is not None and not isinstance(
                position,
                str,
            ):
                raise ValueError(
                    "O cargo do contato é inválido."
                )

            contact.position = (
                self._normalize_optional_text(position)
            )

        if is_primary is not FIELD_NOT_PROVIDED:
            if not isinstance(is_primary, bool):
                raise ValueError(
                    "A indicação de contato principal é inválida."
                )

            if is_primary:
                self._remove_current_primary(
                    supplier_id=supplier_id,
                    ignored_contact_id=contact.id,
                )

            contact.is_primary = int(is_primary)

        return self.repository.save(contact)

    def activate(
        self,
        supplier_id: int,
        contact_id: int,
    ) -> SupplierContact:
        """Ativa um contato inativo."""

        contact = self.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        if contact.is_active:
            raise ValueError(
                "O contato já está ativo."
            )

        contact.is_active = 1

        return self.repository.save(contact)

    def deactivate(
        self,
        supplier_id: int,
        contact_id: int,
    ) -> SupplierContact:
        """Desativa um contato ativo."""

        contact = self.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        if not contact.is_active:
            raise ValueError(
                "O contato já está inativo."
            )

        contact.is_active = 0
        contact.is_primary = 0

        return self.repository.save(contact)

    def _validate_supplier_exists(
        self,
        supplier_id: int,
    ) -> None:
        """Valida se o fornecedor existe."""

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

    def _remove_current_primary(
        self,
        supplier_id: int,
        ignored_contact_id: int | None = None,
    ) -> None:
        """
        Remove a definição de principal do contato atual.

        O contato ignorado não é alterado durante atualizações.
        """

        current_primary = (
            self.repository.get_primary_by_supplier(
                supplier_id
            )
        )

        if current_primary is None:
            return

        if current_primary.id == ignored_contact_id:
            return

        current_primary.is_primary = 0

        self.repository.save(current_primary)

    @staticmethod
    def _normalize_required_text(
        value: str,
        field_name: str,
    ) -> str:
        """Normaliza e valida textos obrigatórios."""

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
        """Normaliza campos opcionais."""

        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        return normalized_value

    @classmethod
    def _normalize_email(
        cls,
        email: str | None,
    ) -> str | None:
        """Normaliza o endereço de e-mail."""

        normalized_email = cls._normalize_optional_text(
            email
        )

        if normalized_email is None:
            return None

        return normalized_email.lower()