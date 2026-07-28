from unittest.mock import Mock

import pytest

from src.models.supplier import Supplier
from src.models.supplier_contact import SupplierContact
from src.services.supplier_contact_service import (
    SupplierContactService,
)


@pytest.fixture
def contact_repository() -> Mock:
    """Cria um mock do repository de contatos."""

    return Mock()


@pytest.fixture
def supplier_repository() -> Mock:
    """Cria um mock do repository de fornecedores."""

    return Mock()


@pytest.fixture
def service(
    contact_repository: Mock,
    supplier_repository: Mock,
) -> SupplierContactService:
    """Cria o serviço com repositories simulados."""

    return SupplierContactService(
        repository=contact_repository,
        supplier_repository=supplier_repository,
    )


def create_supplier(
    supplier_id: int = 1,
) -> Supplier:
    """Cria um fornecedor para os testes."""

    return Supplier(
        id=supplier_id,
        name="Fornecedor Teste",
        document="12.345.678/0001-90",
        address="Registro/SP",
        notes=None,
        is_active=1,
    )


def create_contact(
    *,
    contact_id: int = 10,
    supplier_id: int = 1,
    name: str = "João Silva",
    email: str | None = "joao@fornecedor.com",
    phone: str | None = "(11) 99999-1111",
    position: str | None = "Garantia",
    is_primary: int = 0,
    is_active: int = 1,
) -> SupplierContact:
    """Cria um contato para os testes."""

    return SupplierContact(
        id=contact_id,
        supplier_id=supplier_id,
        name=name,
        email=email,
        phone=phone,
        position=position,
        is_primary=is_primary,
        is_active=is_active,
    )


def test_should_create_supplier_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.add.side_effect = (
        lambda contact: contact
    )

    contact = service.create(
        supplier_id=1,
        name="João Silva",
        email="joao@fornecedor.com",
        phone="(11) 99999-1111",
        position="Garantia",
        is_primary=False,
    )

    assert contact.supplier_id == 1
    assert contact.name == "João Silva"
    assert contact.email == "joao@fornecedor.com"
    assert contact.phone == "(11) 99999-1111"
    assert contact.position == "Garantia"
    assert contact.is_primary == 0
    assert contact.is_active == 1

    contact_repository.add.assert_called_once_with(
        contact
    )


def test_should_normalize_contact_fields(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.add.side_effect = (
        lambda contact: contact
    )

    contact = service.create(
        supplier_id=1,
        name="  João Silva  ",
        email="  JOAO@FORNECEDOR.COM  ",
        phone="   ",
        position="  Garantia  ",
    )

    assert contact.name == "João Silva"
    assert contact.email == "joao@fornecedor.com"
    assert contact.phone is None
    assert contact.position == "Garantia"


def test_should_raise_when_supplier_is_not_found(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create(
            supplier_id=999,
            name="João Silva",
        )

    contact_repository.add.assert_not_called()


def test_should_return_required_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()
    contact = create_contact()

    supplier_repository.get_by_id.return_value = supplier
    contact_repository.get_by_id.return_value = contact

    result = service.get_required(
        supplier_id=1,
        contact_id=10,
    )

    assert result == contact

    supplier_repository.get_by_id.assert_called_once_with(1)
    contact_repository.get_by_id.assert_called_once_with(10)


def test_should_raise_when_contact_is_not_found(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Contato não encontrado.",
    ):
        service.get_required(
            supplier_id=1,
            contact_id=999,
        )


def test_should_raise_when_contact_belongs_to_another_supplier(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.get_by_id.return_value = (
        create_contact(
            supplier_id=2,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "O contato não pertence ao fornecedor informado."
        ),
    ):
        service.get_required(
            supplier_id=1,
            contact_id=10,
        )


def test_should_list_contacts_by_supplier(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contacts = [
        create_contact(contact_id=10),
        create_contact(
            contact_id=11,
            name="Maria Souza",
        ),
    ]

    contact_repository.list_by_supplier.return_value = (
        contacts
    )

    result = service.list_by_supplier(1)

    assert result == contacts

    contact_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_update_only_informed_fields(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact()

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        phone="(13) 99999-2222",
    )

    assert updated.phone == "(13) 99999-2222"
    assert updated.name == "João Silva"
    assert updated.email == "joao@fornecedor.com"
    assert updated.position == "Garantia"

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_clear_optional_fields(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact()

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        email=None,
        phone="   ",
        position=None,
    )

    assert updated.email is None
    assert updated.phone is None
    assert updated.position is None


def test_should_create_primary_contact_and_remove_previous_primary(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    current_primary = create_contact(
        contact_id=20,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.get_primary_by_supplier.return_value = (
        current_primary
    )
    contact_repository.save.side_effect = (
        lambda contact: contact
    )
    contact_repository.add.side_effect = (
        lambda contact: contact
    )

    new_contact = service.create(
        supplier_id=1,
        name="Maria Souza",
        is_primary=True,
    )

    assert current_primary.is_primary == 0
    assert new_contact.is_primary == 1

    contact_repository.save.assert_called_once_with(
        current_primary
    )
    contact_repository.add.assert_called_once_with(
        new_contact
    )


def test_should_define_existing_contact_as_primary(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        contact_id=10,
        is_primary=0,
    )

    previous_primary = create_contact(
        contact_id=20,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.get_primary_by_supplier.return_value = (
        previous_primary
    )
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        is_primary=True,
    )

    assert previous_primary.is_primary == 0
    assert updated.is_primary == 1

    assert contact_repository.save.call_count == 2

    contact_repository.save.assert_any_call(
        previous_primary
    )
    contact_repository.save.assert_any_call(
        contact
    )


def test_should_not_remove_same_contact_when_already_primary(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        contact_id=10,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.get_primary_by_supplier.return_value = (
        contact
    )
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        is_primary=True,
    )

    assert updated.is_primary == 1

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_deactivate_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=1,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.deactivate(
        supplier_id=1,
        contact_id=10,
    )

    assert updated.is_active == 0
    assert updated.is_primary == 0

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_raise_when_contact_is_already_inactive(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=0,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact

    with pytest.raises(
        ValueError,
        match="O contato já está inativo.",
    ):
        service.deactivate(
            supplier_id=1,
            contact_id=10,
        )

    contact_repository.save.assert_not_called()


def test_should_activate_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=0,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.activate(
        supplier_id=1,
        contact_id=10,
    )

    assert updated.is_active == 1

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_raise_when_contact_is_already_active(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact

    with pytest.raises(
        ValueError,
        match="O contato já está ativo.",
    ):
        service.activate(
            supplier_id=1,
            contact_id=10,
        )

    contact_repository.save.assert_not_called()