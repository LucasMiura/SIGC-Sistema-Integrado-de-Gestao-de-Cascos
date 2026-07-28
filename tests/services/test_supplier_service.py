from unittest.mock import Mock

import pytest

from src.models.supplier import Supplier
from src.services.supplier_service import SupplierService


@pytest.fixture
def repository() -> Mock:
    return Mock()


@pytest.fixture
def service(repository: Mock) -> SupplierService:
    return SupplierService(repository)


def create_supplier() -> Supplier:
    return Supplier(
        id=1,
        name="Fornecedor Teste",
        document="123456",
        address="Registro/SP",
        notes="Observação",
        is_active=1,
    )


def test_should_create_supplier(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_document.return_value = None
    repository.add.side_effect = lambda supplier: supplier

    supplier = service.create(
        name="Fornecedor Teste",
        document="123456",
    )

    assert supplier.name == "Fornecedor Teste"
    assert supplier.document == "123456"

    repository.add.assert_called_once()


def test_should_normalize_fields(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_document.return_value = None
    repository.add.side_effect = lambda supplier: supplier

    supplier = service.create(
        name="  Fornecedor  ",
        address="   ",
        notes="  Observação  ",
    )

    assert supplier.name == "Fornecedor"
    assert supplier.address is None
    assert supplier.notes == "Observação"


def test_should_raise_when_document_already_exists(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_document.return_value = create_supplier()

    with pytest.raises(
        ValueError,
        match="Já existe um fornecedor com este documento.",
    ):
        service.create(
            name="Fornecedor",
            document="123456",
        )


def test_should_return_supplier_on_get_required(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier

    result = service.get_required(1)

    assert result == supplier


def test_should_raise_when_supplier_not_found(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.get_required(99)


def test_should_update_only_informed_fields(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier
    repository.get_by_document.return_value = None
    repository.save.side_effect = lambda supplier: supplier

    updated = service.update(
        supplier.id,
        address="Novo endereço",
    )

    assert updated.address == "Novo endereço"
    assert updated.name == "Fornecedor Teste"

    repository.save.assert_called_once()


def test_should_clear_optional_field(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier
    repository.save.side_effect = lambda supplier: supplier

    updated = service.update(
        supplier.id,
        notes=None,
    )

    assert updated.notes is None


def test_should_deactivate_supplier(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier
    repository.save.side_effect = lambda supplier: supplier

    updated = service.deactivate(1)

    assert updated.is_active == 0


def test_should_activate_supplier(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()
    supplier.is_active = 0

    repository.get_by_id.return_value = supplier
    repository.save.side_effect = lambda supplier: supplier

    updated = service.activate(1)

    assert updated.is_active == 1