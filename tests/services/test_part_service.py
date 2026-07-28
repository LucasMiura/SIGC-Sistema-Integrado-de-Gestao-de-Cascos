from unittest.mock import Mock

import pytest

from src.models.part import Part
from src.models.supplier import Supplier
from src.services.part_service import PartService


@pytest.fixture
def part_repository() -> Mock:
    """Repository de peças simulado."""

    return Mock()


@pytest.fixture
def supplier_repository() -> Mock:
    """Repository de fornecedores simulado."""

    return Mock()


@pytest.fixture
def service(
    part_repository: Mock,
    supplier_repository: Mock,
) -> PartService:
    """Service de peças com dependências simuladas."""

    return PartService(
        part_repository=part_repository,
        supplier_repository=supplier_repository,
    )


def create_supplier(
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    is_active: int = 1,
) -> Supplier:
    """Cria um fornecedor para utilização nos testes."""

    return Supplier(
        id=supplier_id,
        name=name,
        document="12345678000199",
        address="Registro/SP",
        notes=None,
        is_active=is_active,
    )


def create_part(
    part_id: int = 10,
    supplier_id: int = 1,
    part_code: str = "ABC123",
    name: str = "Motor de partida",
    description: str | None = "Peça remanufaturada",
    return_deadline_days: int = 90,
    is_active: int = 1,
) -> Part:
    """Cria uma peça para utilização nos testes."""

    return Part(
        id=part_id,
        supplier_id=supplier_id,
        part_code=part_code,
        name=name,
        description=description,
        return_deadline_days=return_deadline_days,
        is_active=is_active,
    )


def test_should_create_part(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=1,
        part_code="ABC123",
        name="Motor de partida",
        description="Peça remanufaturada",
        return_deadline_days=90,
    )

    assert part.supplier_id == 1
    assert part.part_code == "ABC123"
    assert part.name == "Motor de partida"
    assert part.description == "Peça remanufaturada"
    assert part.return_deadline_days == 90
    assert part.is_active == 1

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            1,
            "ABC123",
        )
    )

    part_repository.add.assert_called_once_with(
        part
    )


def test_should_normalize_fields_when_creating_part(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=1,
        part_code="  ABC123  ",
        name="  Motor de partida  ",
        description="  Peça remanufaturada  ",
        return_deadline_days=90,
    )

    assert part.part_code == "ABC123"
    assert part.name == "Motor de partida"
    assert part.description == "Peça remanufaturada"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            1,
            "ABC123",
        )
    )


def test_should_convert_empty_description_to_none(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=1,
        part_code="ABC123",
        name="Motor de partida",
        description="   ",
        return_deadline_days=90,
    )

    assert part.description is None


def test_should_raise_when_supplier_does_not_exist(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_supplier_is_inactive(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_part_code_is_empty(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="O código original da peça é obrigatório.",
    ):
        service.create(
            supplier_id=1,
            part_code="   ",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_part_name_is_empty(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="O nome da peça é obrigatório.",
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="   ",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_part_already_exists_for_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma peça com este código "
            "para o fornecedor informado."
        ),
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_allow_same_code_for_different_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=2,
        part_code="ABC123",
        name="Motor de partida",
        return_deadline_days=120,
    )

    assert part.supplier_id == 2
    assert part.part_code == "ABC123"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            2,
            "ABC123",
        )
    )


@pytest.mark.parametrize(
    (
        "return_deadline_days",
        "expected_message",
    ),
    [
        (
            0,
            (
                "O prazo de devolução deve ser "
                "maior que zero."
            ),
        ),
        (
            -1,
            (
                "O prazo de devolução deve ser "
                "maior que zero."
            ),
        ),
        (
            3651,
            (
                "O prazo de devolução não pode "
                "ser maior que 3650 dias."
            ),
        ),
    ],
)
def test_should_raise_when_return_deadline_is_invalid(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
    return_deadline_days: int,
    expected_message: str,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=return_deadline_days,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_return_deadline_is_boolean(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match=(
            "O prazo de devolução deve ser "
            "informado em dias."
        ),
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=True,
        )

    part_repository.add.assert_not_called()


def test_should_get_part_by_id(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    result = service.get_by_id(10)

    assert result is part

    part_repository.get_by_id.assert_called_once_with(
        10
    )


def test_should_return_none_when_part_does_not_exist(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = None

    result = service.get_by_id(10)

    assert result is None


def test_should_raise_when_getting_part_with_invalid_id(
    service: PartService,
    part_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da peça deve ser "
            "maior que zero."
        ),
    ):
        service.get_by_id(0)

    part_repository.get_by_id.assert_not_called()


def test_should_get_required_part(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    result = service.get_required(10)

    assert result is part


def test_should_raise_when_required_part_does_not_exist(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.get_required(10)


def test_should_list_all_parts(
    service: PartService,
    part_repository: Mock,
) -> None:
    parts = [
        create_part(
            part_id=10,
            part_code="ABC123",
        ),
        create_part(
            part_id=11,
            part_code="XYZ789",
        ),
    ]

    part_repository.list_all.return_value = parts

    result = service.list_all()

    assert result == parts

    part_repository.list_all.assert_called_once_with()


def test_should_list_parts_by_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()

    parts = [
        create_part(
            part_id=10,
        ),
        create_part(
            part_id=11,
            part_code="XYZ789",
        ),
    ]

    supplier_repository.get_by_id.return_value = supplier
    part_repository.list_by_supplier.return_value = parts

    result = service.list_by_supplier(1)

    assert result == parts

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    part_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_raise_when_listing_parts_of_unknown_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.list_by_supplier(1)

    part_repository.list_by_supplier.assert_not_called()


def test_should_update_part_name(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        name="  Alternador  ",
    )

    assert updated.name == "Alternador"
    assert updated.part_code == "ABC123"
    assert updated.supplier_id == 1
    assert updated.return_deadline_days == 90

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_update_part_code(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        part_code="  XYZ789  ",
    )

    assert updated.part_code == "XYZ789"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            1,
            "XYZ789",
        )
    )


def test_should_not_check_duplicate_when_code_is_unchanged(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        name="Novo nome",
    )

    assert updated.name == "Novo nome"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_not_called()
    )


def test_should_change_part_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part()

    new_supplier = create_supplier(
        supplier_id=2,
        name="Novo fornecedor",
    )

    part_repository.get_by_id.return_value = part
    supplier_repository.get_by_id.return_value = (
        new_supplier
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        supplier_id=2,
    )

    assert updated.supplier_id == 2
    assert updated.part_code == "ABC123"

    supplier_repository.get_by_id.assert_called_once_with(
        2
    )

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            2,
            "ABC123",
        )
    )


def test_should_raise_when_new_supplier_is_inactive(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.update(
            part_id=10,
            supplier_id=2,
        )

    part_repository.save.assert_not_called()


def test_should_raise_when_updated_combination_already_exists(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part()

    duplicate = create_part(
        part_id=20,
        supplier_id=2,
        part_code="ABC123",
    )

    part_repository.get_by_id.return_value = part

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    part_repository.get_by_supplier_and_code.return_value = (
        duplicate
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma peça com este código "
            "para o fornecedor informado."
        ),
    ):
        service.update(
            part_id=10,
            supplier_id=2,
        )

    part_repository.save.assert_not_called()


def test_should_allow_duplicate_lookup_to_return_same_part(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    part_repository.get_by_supplier_and_code.return_value = (
        part
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        part_code="XYZ789",
    )

    assert updated.part_code == "XYZ789"

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_clear_optional_description(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        description=None,
    )

    assert updated.description is None


def test_should_convert_empty_updated_description_to_none(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        description="   ",
    )

    assert updated.description is None


def test_should_update_return_deadline(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        return_deadline_days=120,
    )

    assert updated.return_deadline_days == 120


def test_should_raise_when_updated_name_is_empty(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match="O nome da peça é obrigatório.",
    ):
        service.update(
            part_id=10,
            name="   ",
        )

    part_repository.save.assert_not_called()


def test_should_raise_when_updated_code_is_empty(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match="O código original da peça é obrigatório.",
    ):
        service.update(
            part_id=10,
            part_code="   ",
        )

    part_repository.save.assert_not_called()


def test_should_deactivate_part(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part(
        is_active=1,
    )

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.deactivate(10)

    assert updated.is_active == 0

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_raise_when_part_is_already_inactive(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="A peça já está inativa.",
    ):
        service.deactivate(10)

    part_repository.save.assert_not_called()


def test_should_activate_part(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part(
        is_active=0,
    )

    part_repository.get_by_id.return_value = part

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.activate(10)

    assert updated.is_active == 1

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_raise_when_part_is_already_active(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part(
            is_active=1,
        )
    )

    with pytest.raises(
        ValueError,
        match="A peça já está ativa.",
    ):
        service.activate(10)

    part_repository.save.assert_not_called()


def test_should_raise_when_activating_part_with_inactive_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part(
            is_active=0,
        )
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.activate(10)

    part_repository.save.assert_not_called()