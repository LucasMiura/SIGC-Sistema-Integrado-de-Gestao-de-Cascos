from unittest.mock import Mock
from types import SimpleNamespace

import pytest

from src.models.purchase import Purchase
from src.models.supplier import Supplier
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.services.purchase_service import (
    PurchaseService,
)


@pytest.fixture
def purchase_repository() -> Mock:
    """
    Cria um mock do repositório de compras.
    """

    return Mock(
        spec=PurchaseRepository,
    )


@pytest.fixture
def purchase_item_repository() -> Mock:
    """
    Cria um mock do repositório de itens da compra.
    """

    return Mock(
        spec=PurchaseItemRepository,
    )


@pytest.fixture
def supplier_repository() -> Mock:
    """
    Cria um mock do repositório de fornecedores.
    """

    return Mock(
        spec=SupplierRepository,
    )


@pytest.fixture
def part_repository() -> Mock:
    """
    Cria um mock do repositório de peças.
    """

    return Mock(
        spec=PartRepository,
    )


@pytest.fixture
def service(
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> PurchaseService:
    """
    Cria o serviço com suas dependências simuladas.
    """

    return PurchaseService(
        purchase_repository=purchase_repository,
        purchase_item_repository=(
            purchase_item_repository
        ),
        supplier_repository=supplier_repository,
        part_repository=part_repository,
    )


def create_supplier(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    is_active: int = 1,
) -> Supplier:
    """
    Cria um fornecedor para os testes.
    """

    return Supplier(
        id=supplier_id,
        name=name,
        document="12.345.678/0001-90",
        address="Rua de Teste, 100",
        notes="Fornecedor criado para teste.",
        is_active=is_active,
    )


def create_purchase(
    *,
    purchase_id: int = 10,
    supplier_id: int = 1,
    invoice_number: str = "NF-12345",
    invoice_series: str | None = "1",
    issue_date: str = "2026-07-29",
    created_by: int = 1,
    status: str = "RECEIVED",
    notes: str | None = "Compra criada para teste.",
) -> Purchase:
    """
    Cria uma compra para os testes.
    """

    return Purchase(
        id=purchase_id,
        supplier_id=supplier_id,
        invoice_number=invoice_number,
        invoice_series=invoice_series,
        issue_date=issue_date,
        created_by=created_by,
        status=status,
        notes=notes,
    )

def create_part(
    *,
    part_id: int = 20,
    supplier_id: int = 1,
    part_code: str = "PEC-001",
    name: str = "Compressor de ar",
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria uma peça simplificada para os testes.
    """

    return SimpleNamespace(
        id=part_id,
        supplier_id=supplier_id,
        part_code=part_code,
        name=name,
        is_active=is_active,
    )


def create_purchase_item(
    *,
    purchase_item_id: int = 30,
    purchase_id: int = 10,
    part_id: int = 20,
    quantity_purchased: int = 10,
    quantity_available: int = 10,
) -> SimpleNamespace:
    """
    Cria um item de compra simplificado para os testes.
    """

    return SimpleNamespace(
        id=purchase_item_id,
        purchase_id=purchase_id,
        part_id=part_id,
        quantity_purchased=quantity_purchased,
        quantity_available=quantity_available,
    )

def test_should_create_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()

    supplier_repository.get_by_id.return_value = (
        supplier
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
        issue_date="2026-07-29",
        created_by=1,
        status="RECEIVED",
        notes="Compra criada para teste.",
    )

    assert created.supplier_id == 1
    assert created.invoice_number == "NF-12345"
    assert created.invoice_series == "1"
    assert created.issue_date == "2026-07-29"
    assert created.created_by == 1
    assert created.status == "RECEIVED"
    assert created.notes == "Compra criada para teste."

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_normalize_purchase_fields_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="  NF-12345  ",
        invoice_series="  1  ",
        issue_date="  2026-07-29  ",
        created_by=1,
        status="  received  ",
        notes="  Compra de teste  ",
    )

    assert created.invoice_number == "NF-12345"
    assert created.invoice_series == "1"
    assert created.issue_date == "2026-07-29"
    assert created.status == "RECEIVED"
    assert created.notes == "Compra de teste"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_create_purchase_without_optional_fields(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
        issue_date="2026-07-29",
        created_by=1,
        status="PENDING",
        notes=None,
    )

    assert created.invoice_series is None
    assert created.notes is None
    assert created.status == "PENDING"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_convert_blank_optional_fields_to_none(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="   ",
        issue_date="2026-07-29",
        created_by=1,
        status="RECEIVED",
        notes="   ",
    )

    assert created.invoice_series is None
    assert created.notes is None

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_raise_when_supplier_is_not_found_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create_purchase(
            supplier_id=999,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    supplier_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_supplier_is_inactive_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
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
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_invoice_number_is_blank(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="O número da nota fiscal é obrigatório.",
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="   ",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_issue_date_is_blank(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="   ",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "invalid_status",
    [
        "",
        "   ",
        "ACTIVE",
        "FINISHED",
        "UNKNOWN",
    ],
)
def test_should_raise_for_invalid_status_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
    invalid_status: str,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    expected_message = (
        "O status da compra é obrigatório."
        if not invalid_status.strip()
        else (
            "Status da compra inválido. "
            "Valores permitidos: "
            "CANCELLED, PENDING, RECEIVED."
        )
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status=invalid_status,
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_invoice_already_exists(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        create_purchase()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        ),
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.add.assert_not_called()

def test_should_add_item_to_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase = create_purchase()
    part = create_part()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    part_repository.get_by_id.return_value = part

    purchase_item_repository.list_by_purchase.return_value = (
        []
    )

    purchase_item_repository.add.side_effect = (
        lambda purchase_item: purchase_item
    )

    created_item = service.add_item(
        purchase_id=10,
        part_id=20,
        quantity_purchased=15,
    )

    assert created_item.purchase_id == 10
    assert created_item.part_id == 20
    assert created_item.quantity_purchased == 15
    assert created_item.quantity_available == 15

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_item_repository.add.assert_called_once_with(
        created_item
    )


def test_should_raise_when_purchase_is_not_found_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.add_item(
            purchase_id=999,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )

    part_repository.get_by_id.assert_not_called()

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_purchase_is_cancelled_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens "
            "a uma compra cancelada."
        ),
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_not_called()

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_is_not_found_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.add_item(
            purchase_id=10,
            part_id=999,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_is_inactive_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="A peça informada está inativa.",
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_belongs_to_another_supplier(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            supplier_id=1,
        )
    )

    part_repository.get_by_id.return_value = (
        create_part(
            supplier_id=2,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "A peça informada não pertence "
            "ao fornecedor da compra."
        ),
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "invalid_quantity",
    [
        0,
        -1,
        -10,
    ],
)
def test_should_raise_for_invalid_quantity_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    invalid_quantity: int,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade comprada deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=invalid_quantity,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_is_already_in_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
    ]

    with pytest.raises(
        ValueError,
        match="Esta peça já foi adicionada à compra.",
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_item_repository.add.assert_not_called()


def test_should_allow_different_part_in_same_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            part_id=21,
            part_code="PEC-002",
            name="Alternador",
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
    ]

    purchase_item_repository.add.side_effect = (
        lambda purchase_item: purchase_item
    )

    created_item = service.add_item(
        purchase_id=10,
        part_id=21,
        quantity_purchased=5,
    )

    assert created_item.purchase_id == 10
    assert created_item.part_id == 21
    assert created_item.quantity_purchased == 5
    assert created_item.quantity_available == 5

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_item_repository.add.assert_called_once_with(
        created_item
    )

def test_should_get_purchase_by_id(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    result = service.get_purchase(
        10
    )

    assert result is purchase

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )


def test_should_raise_when_purchase_is_not_found_on_get(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.get_purchase(
            999
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )


def test_should_list_all_purchases(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    first_purchase = create_purchase()

    second_purchase = create_purchase(
        purchase_id=11,
        supplier_id=2,
        invoice_number="NF-67890",
        invoice_series="2",
        issue_date="2026-07-30",
        status="PENDING",
        notes=None,
    )

    purchase_repository.list_all.return_value = [
        first_purchase,
        second_purchase,
    ]

    result = service.list_purchases()

    assert result == [
        first_purchase,
        second_purchase,
    ]

    purchase_repository.list_all.assert_called_once_with()


def test_should_return_empty_purchase_list(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.list_all.return_value = []

    result = service.list_purchases()

    assert result == []

    purchase_repository.list_all.assert_called_once_with()


def test_should_list_purchases_by_supplier(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()

    first_purchase = create_purchase()

    second_purchase = create_purchase(
        purchase_id=11,
        invoice_number="NF-67890",
        invoice_series="2",
        issue_date="2026-07-30",
        status="PENDING",
        notes=None,
    )

    supplier_repository.get_by_id.return_value = (
        supplier
    )

    purchase_repository.list_by_supplier.return_value = [
        first_purchase,
        second_purchase,
    ]

    result = service.list_purchases_by_supplier(
        1
    )

    assert result == [
        first_purchase,
        second_purchase,
    ]

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    purchase_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_return_empty_list_for_supplier_without_purchases(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.list_by_supplier.return_value = []

    result = service.list_purchases_by_supplier(
        1
    )

    assert result == []

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    purchase_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_raise_when_supplier_is_not_found_on_purchase_list(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.list_purchases_by_supplier(
            999
        )

    supplier_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_repository.list_by_supplier.assert_not_called()


def test_should_list_purchase_items(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase()

    first_item = create_purchase_item()

    second_item = create_purchase_item(
        purchase_item_id=31,
        part_id=21,
        quantity_purchased=5,
        quantity_available=3,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = [
        first_item,
        second_item,
    ]

    result = service.list_purchase_items(
        10
    )

    assert result == [
        first_item,
        second_item,
    ]

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )


def test_should_return_empty_purchase_item_list(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    purchase_item_repository.list_by_purchase.return_value = []

    result = service.list_purchase_items(
        10
    )

    assert result == []

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )


def test_should_raise_when_purchase_is_not_found_on_item_list(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.list_purchase_items(
            999
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()

def test_should_update_purchase_invoice_number(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_number="  NF-99999  ",
    )

    assert updated is purchase
    assert updated.invoice_number == "NF-99999"

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-99999",
        invoice_series="1",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_invoice_series(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_series="  2  ",
    )

    assert updated.invoice_series == "2"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="2",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_clear_purchase_invoice_series(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series="1",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_series=None,
    )

    assert updated.invoice_series is None

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_convert_blank_invoice_series_to_none_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series="1",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_series="   ",
    )

    assert updated.invoice_series is None

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_issue_date(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        issue_date="  2026-08-01  ",
    )

    assert updated.issue_date == "2026-08-01"

    purchase_repository.get_by_invoice.assert_not_called()

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_status(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        status="  received  ",
    )

    assert updated.status == "RECEIVED"

    purchase_repository.get_by_invoice.assert_not_called()

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_notes(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        notes="  Observação atualizada  ",
    )

    assert updated.notes == "Observação atualizada"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_clear_purchase_notes(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        notes="Observação antiga",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        notes=None,
    )

    assert updated.notes is None

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_convert_blank_notes_to_none_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        notes="Observação antiga",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        notes="   ",
    )

    assert updated.notes is None

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_multiple_purchase_fields(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_number="NF-88888",
        invoice_series="3",
        issue_date="2026-08-10",
        status="RECEIVED",
        notes="Compra atualizada",
    )

    assert updated.invoice_number == "NF-88888"
    assert updated.invoice_series == "3"
    assert updated.issue_date == "2026-08-10"
    assert updated.status == "RECEIVED"
    assert updated.notes == "Compra atualizada"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-88888",
        invoice_series="3",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_allow_update_without_fields(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
    )

    assert updated is purchase

    purchase_repository.get_by_invoice.assert_not_called()

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_supplier_without_items(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
) -> None:
    purchase = create_purchase(
        supplier_id=1,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = (
        []
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        supplier_id=2,
    )

    assert updated.supplier_id == 2

    supplier_repository.get_by_id.assert_called_once_with(
        2
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=2,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_supplier_when_all_items_are_compatible(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase = create_purchase(
        supplier_id=1,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
        create_purchase_item(
            purchase_item_id=31,
            part_id=21,
        ),
    ]

    part_repository.get_by_id.side_effect = [
        create_part(
            part_id=20,
            supplier_id=2,
        ),
        create_part(
            part_id=21,
            supplier_id=2,
        ),
    ]

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        supplier_id=2,
    )

    assert updated.supplier_id == 2

    assert part_repository.get_by_id.call_count == 2

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_purchase_is_not_found_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.update_purchase(
            purchase_id=999,
            notes="Nova observação",
        )

    purchase_repository.save.assert_not_called()


def test_should_raise_when_purchase_is_cancelled_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Uma compra cancelada não pode ser alterada."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            notes="Nova observação",
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_new_supplier_is_not_found(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    supplier_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=999,
        )

    supplier_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_new_supplier_is_inactive(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

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
        service.update_purchase(
            purchase_id=10,
            supplier_id=2,
        )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_item_is_incompatible_with_new_supplier(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            supplier_id=1,
        )
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
    ]

    part_repository.get_by_id.return_value = (
        create_part(
            part_id=20,
            supplier_id=1,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível alterar o fornecedor "
            "porque existem peças incompatíveis "
            "na compra."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=2,
        )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_item_part_is_not_found_on_supplier_update(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=999,
        ),
    ]

    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível alterar o fornecedor "
            "porque existem peças incompatíveis "
            "na compra."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=2,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_updated_invoice_already_exists(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        purchase_id=10,
    )

    duplicated_purchase = create_purchase(
        purchase_id=11,
        invoice_number="NF-99999",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        duplicated_purchase
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            invoice_number="NF-99999",
        )

    purchase_repository.save.assert_not_called()


def test_should_allow_invoice_lookup_to_return_same_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        purchase_id=10,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_number="NF-99999",
    )

    assert updated.invoice_number == "NF-99999"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_invoice_number_is_blank_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    with pytest.raises(
        ValueError,
        match="O número da nota fiscal é obrigatório.",
    ):
        service.update_purchase(
            purchase_id=10,
            invoice_number="   ",
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_issue_date_is_blank_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.update_purchase(
            purchase_id=10,
            issue_date="   ",
        )

    purchase_repository.save.assert_not_called()


@pytest.mark.parametrize(
    "invalid_status",
    [
        "",
        "   ",
        "ACTIVE",
        "FINISHED",
        "UNKNOWN",
    ],
)
def test_should_raise_for_invalid_status_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
    invalid_status: str,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    expected_message = (
        "O status da compra é obrigatório."
        if not invalid_status.strip()
        else (
            "Status da compra inválido. "
            "Valores permitidos: "
            "CANCELLED, PENDING, RECEIVED."
        )
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.update_purchase(
            purchase_id=10,
            status=invalid_status,
        )

    purchase_repository.save.assert_not_called()


def test_should_reject_cancelled_status_on_regular_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="PENDING",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Utilize a operação específica "
            "para cancelar a compra."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            status="CANCELLED",
        )

    purchase_repository.save.assert_not_called()

def test_should_cancel_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=10,
            quantity_available=10,
        ),
        create_purchase_item(
            purchase_item_id=31,
            quantity_purchased=5,
            quantity_available=5,
        ),
    ]

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    cancelled_purchase = service.cancel_purchase(
        purchase_id=10,
    )

    assert cancelled_purchase is purchase
    assert cancelled_purchase.status == "CANCELLED"

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_purchase_is_not_found_on_cancel(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.cancel_purchase(
            purchase_id=999,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()

    purchase_repository.save.assert_not_called()


def test_should_raise_when_purchase_is_already_cancelled(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match="A compra já está cancelada.",
    ):
        service.cancel_purchase(
            purchase_id=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_not_called()

    purchase_repository.save.assert_not_called()


def test_should_raise_when_purchase_has_stock_movements(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="RECEIVED",
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=10,
            quantity_available=8,
        ),
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível cancelar uma compra "
            "que já possui movimentações."
        ),
    ):
        service.cancel_purchase(
            purchase_id=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_repository.save.assert_not_called()


def test_should_allow_cancel_purchase_without_items(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = (
        []
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    cancelled_purchase = service.cancel_purchase(
        purchase_id=10,
    )

    assert cancelled_purchase.status == "CANCELLED"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_allow_cancel_when_all_quantities_are_intact(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="RECEIVED",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=30,
            quantity_available=30,
        ),
        create_purchase_item(
            purchase_item_id=31,
            quantity_purchased=7,
            quantity_available=7,
        ),
        create_purchase_item(
            purchase_item_id=32,
            quantity_purchased=100,
            quantity_available=100,
        ),
    ]

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    cancelled_purchase = service.cancel_purchase(
        purchase_id=10,
    )

    assert cancelled_purchase.status == "CANCELLED"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_any_item_has_stock_movement(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=30,
            quantity_available=30,
        ),
        create_purchase_item(
            purchase_item_id=31,
            quantity_purchased=10,
            quantity_available=9,
        ),
        create_purchase_item(
            purchase_item_id=32,
            quantity_purchased=5,
            quantity_available=5,
        ),
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível cancelar uma compra "
            "que já possui movimentações."
        ),
    ):
        service.cancel_purchase(
            purchase_id=10,
        )

    purchase_repository.save.assert_not_called()