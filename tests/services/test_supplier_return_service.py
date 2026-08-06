from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.models.supplier_return import SupplierReturn
from src.models.supplier_return_item import (
    SupplierReturnItem,
)
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
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
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)
from src.services.supplier_return_service import (
    SupplierReturnService,
)


@pytest.fixture
def supplier_return_repository() -> Mock:
    return Mock(
        spec=SupplierReturnRepository,
    )


@pytest.fixture
def supplier_return_item_repository() -> Mock:
    return Mock(
        spec=SupplierReturnItemRepository,
    )


@pytest.fixture
def supplier_repository() -> Mock:
    return Mock(
        spec=SupplierRepository,
    )


@pytest.fixture
def purchase_repository() -> Mock:
    return Mock(
        spec=PurchaseRepository,
    )


@pytest.fixture
def purchase_item_repository() -> Mock:
    return Mock(
        spec=PurchaseItemRepository,
    )


@pytest.fixture
def outbound_purchase_allocation_repository() -> Mock:
    return Mock(
        spec=OutboundPurchaseAllocationRepository,
    )


@pytest.fixture
def customer_return_allocation_repository() -> Mock:
    return Mock(
        spec=CustomerReturnAllocationRepository,
    )


@pytest.fixture
def service(
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    supplier_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> SupplierReturnService:
    return SupplierReturnService(
        supplier_return_repository=(
            supplier_return_repository
        ),
        supplier_return_item_repository=(
            supplier_return_item_repository
        ),
        supplier_repository=supplier_repository,
        purchase_repository=purchase_repository,
        purchase_item_repository=(
            purchase_item_repository
        ),
        outbound_purchase_allocation_repository=(
            outbound_purchase_allocation_repository
        ),
        outbound_transfer_allocation_repository=(
            outbound_transfer_allocation_repository
        ),
        customer_return_allocation_repository=(
            customer_return_allocation_repository
        ),
    )


@pytest.fixture
def outbound_transfer_allocation_repository() -> Mock:
    repository = Mock(
        spec=OutboundTransferAllocationRepository,
    )

    repository.list_by_outbound_item.return_value = []

    return repository

def create_supplier(
    supplier_id: int = 10,
    is_active: int = 1,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=supplier_id,
        name="Fornecedor Teste",
        is_active=is_active,
    )


def create_supplier_return(
    supplier_return_id: int = 20,
    supplier_id: int = 10,
    dispatch_invoice_number: str = "NF-REMESSA-100",
    dispatch_invoice_series: str | None = "1",
    issue_date: str = "2026-07-30",
    created_by: int = 30,
    status: str = "ACTIVE",
    notes: str | None = "Remessa de teste.",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=supplier_return_id,
        supplier_id=supplier_id,
        dispatch_invoice_number=(
            dispatch_invoice_number
        ),
        dispatch_invoice_series=(
            dispatch_invoice_series
        ),
        issue_date=issue_date,
        created_by=created_by,
        status=status,
        notes=notes,
    )


def create_purchase(
    purchase_id: int = 40,
    supplier_id: int = 10,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=purchase_id,
        supplier_id=supplier_id,
        invoice_number="NF-COMPRA-100",
        status="RECEIVED",
    )


def create_purchase_item(
    purchase_item_id: int = 50,
    purchase_id: int = 40,
    part_id: int = 60,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=purchase_item_id,
        purchase_id=purchase_id,
        part_id=part_id,
    )


def create_supplier_return_item(
    supplier_return_item_id: int = 70,
    supplier_return_id: int = 20,
    purchase_item_id: int = 50,
    quantity: int = 4,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=supplier_return_item_id,
        supplier_return_id=supplier_return_id,
        purchase_item_id=purchase_item_id,
        quantity=quantity,
    )


def create_outbound_purchase_allocation(
    outbound_item_id: int,
    purchase_item_id: int,
    quantity_allocated: int,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=1,
        outbound_item_id=outbound_item_id,
        purchase_item_id=purchase_item_id,
        quantity_allocated=quantity_allocated,
    )


def create_customer_return_allocation(
    outbound_item_id: int,
    quantity_allocated: int,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=1,
        customer_return_item_id=1,
        outbound_item_id=outbound_item_id,
        quantity_allocated=quantity_allocated,
    )


def configure_valid_supplier_return_creation(
    supplier_return_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    supplier_return_repository.get_by_dispatch_invoice_number.return_value = (
        None
    )


def configure_valid_add_item(
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        create_supplier_return()
    )

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item()
    )

    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    supplier_return_item_repository.get_by_supplier_return_and_purchase_item.return_value = (
        None
    )

    supplier_return_item_repository.list_by_supplier_return.return_value = (
        []
    )


def test_should_create_supplier_return(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_repository: Mock,
) -> None:
    configure_valid_supplier_return_creation(
        supplier_return_repository,
        supplier_repository,
    )

    supplier_return_repository.add.side_effect = (
        lambda supplier_return: supplier_return
    )

    created = service.create_supplier_return(
        supplier_id=10,
        dispatch_invoice_number=" NF-REMESSA-100 ",
        dispatch_invoice_series=" 1 ",
        issue_date=" 2026-07-30 ",
        created_by=30,
        status=" active ",
        notes=" Remessa parcial ",
    )

    assert created.supplier_id == 10
    assert (
        created.dispatch_invoice_number
        == "NF-REMESSA-100"
    )
    assert created.dispatch_invoice_series == "1"
    assert created.issue_date == "2026-07-30"
    assert created.created_by == 30
    assert created.status == "ACTIVE"
    assert created.notes == "Remessa parcial"

    supplier_repository.get_by_id.assert_called_once_with(
        10
    )

    supplier_return_repository.get_by_dispatch_invoice_number.assert_called_once_with(
        "NF-REMESSA-100"
    )

    supplier_return_repository.add.assert_called_once_with(
        created
    )


def test_should_create_supplier_return_without_optional_fields(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_repository: Mock,
) -> None:
    configure_valid_supplier_return_creation(
        supplier_return_repository,
        supplier_repository,
    )

    supplier_return_repository.add.side_effect = (
        lambda supplier_return: supplier_return
    )

    created = service.create_supplier_return(
        supplier_id=10,
        dispatch_invoice_number="NF-REMESSA-100",
        issue_date="2026-07-30",
        created_by=30,
    )

    assert created.dispatch_invoice_series is None
    assert created.notes is None
    assert created.status == "ACTIVE"


def test_should_convert_blank_optional_fields_to_none(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_repository: Mock,
) -> None:
    configure_valid_supplier_return_creation(
        supplier_return_repository,
        supplier_repository,
    )

    supplier_return_repository.add.side_effect = (
        lambda supplier_return: supplier_return
    )

    created = service.create_supplier_return(
        supplier_id=10,
        dispatch_invoice_number="NF-REMESSA-100",
        dispatch_invoice_series="   ",
        issue_date="2026-07-30",
        created_by=30,
        notes="   ",
    )

    assert created.dispatch_invoice_series is None
    assert created.notes is None


@pytest.mark.parametrize(
    "supplier_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_supplier_id_on_create(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do fornecedor deve ser "
            "maior que zero."
        ),
    ):
        service.create_supplier_return(
            supplier_id=supplier_id,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
        )

    supplier_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "created_by",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_created_by_on_create(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    created_by: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário deve ser "
            "maior que zero."
        ),
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=created_by,
        )

    supplier_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "dispatch_invoice_number",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_dispatch_invoice_number(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    dispatch_invoice_number: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O número da Nota Fiscal de Simples "
            "Remessa é obrigatório."
        ),
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number=(
                dispatch_invoice_number
            ),
            issue_date="2026-07-30",
            created_by=30,
        )

    supplier_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "issue_date",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_issue_date(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    issue_date: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date=issue_date,
            created_by=30,
        )

    supplier_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_status(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    status: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="O status da remessa é obrigatório.",
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
            status=status,
        )

    supplier_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_reject_invalid_status(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    status: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O status da remessa deve ser "
            "ACTIVE ou CANCELLED."
        ),
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
            status=status,
        )

    supplier_return_repository.add.assert_not_called()

def create_outbound_transfer_allocation(
    outbound_item_id: int,
    transfer_item_id: int,
    quantity_allocated: int,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=1,
        outbound_item_id=outbound_item_id,
        transfer_item_id=transfer_item_id,
        quantity_allocated=quantity_allocated,
    )

def test_should_reject_creation_with_cancelled_status(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Uma remessa ao fornecedor não pode ser "
            "criada já cancelada."
        ),
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
            status="CANCELLED",
        )

    supplier_return_repository.add.assert_not_called()


def test_should_reject_when_supplier_is_not_found(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
        )

    supplier_return_repository.add.assert_not_called()


def test_should_reject_when_supplier_is_inactive(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
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
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
        )

    supplier_return_repository.add.assert_not_called()


def test_should_reject_duplicated_dispatch_invoice_number(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    supplier_return_repository.get_by_dispatch_invoice_number.return_value = (
        create_supplier_return()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma remessa cadastrada com esse "
            "número de Nota Fiscal de Simples Remessa."
        ),
    ):
        service.create_supplier_return(
            supplier_id=10,
            dispatch_invoice_number="NF-REMESSA-100",
            issue_date="2026-07-30",
            created_by=30,
        )

    supplier_return_repository.add.assert_not_called()


def test_should_add_supplier_return_item(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_valid_add_item(
        supplier_return_repository,
        supplier_return_item_repository,
        purchase_repository,
        purchase_item_repository,
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=8,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=8,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=6,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        2
    )

    def add_item(
        supplier_return_item: SupplierReturnItem,
    ) -> SupplierReturnItem:
        supplier_return_item.id = 70
        return supplier_return_item

    supplier_return_item_repository.add.side_effect = (
        add_item
    )

    created = service.add_item(
        supplier_return_id=20,
        purchase_item_id=50,
        quantity=4,
    )

    assert created.id == 70
    assert created.supplier_return_id == 20
    assert created.purchase_item_id == 50
    assert created.quantity == 4

    supplier_return_item_repository.add.assert_called_once_with(
        created
    )


@pytest.mark.parametrize(
    "supplier_return_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_supplier_return_id_on_add_item(
    service: SupplierReturnService,
    supplier_return_item_repository: Mock,
    supplier_return_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da remessa deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            supplier_return_id=supplier_return_id,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "purchase_item_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_purchase_item_id_on_add_item(
    service: SupplierReturnService,
    supplier_return_item_repository: Mock,
    purchase_item_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do item de compra deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=purchase_item_id,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_quantity_on_add_item(
    service: SupplierReturnService,
    supplier_return_item_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade remetida deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=quantity,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_when_supplier_return_is_not_found_on_add_item(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Remessa ao fornecedor não encontrada.",
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_when_supplier_return_is_not_active(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        create_supplier_return(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens a uma "
            "remessa que não está ativa."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_when_purchase_item_is_not_found(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        create_supplier_return()
    )

    purchase_item_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Item de compra não encontrado.",
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_when_purchase_is_not_found(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        create_supplier_return()
    )

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item()
    )

    purchase_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Compra de origem não encontrada.",
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_item_from_different_supplier(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        create_supplier_return(
            supplier_id=10,
        )
    )

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item()
    )

    purchase_repository.get_by_id.return_value = (
        create_purchase(
            supplier_id=99,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "O item de compra não pertence ao "
            "fornecedor da remessa."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_duplicated_purchase_item(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    configure_valid_add_item(
        supplier_return_repository,
        supplier_return_item_repository,
        purchase_repository,
        purchase_item_repository,
    )

    supplier_return_item_repository.get_by_supplier_return_and_purchase_item.return_value = (
        create_supplier_return_item()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Este item de compra já foi adicionado "
            "à remessa."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_items_from_different_purchases(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    configure_valid_add_item(
        supplier_return_repository,
        supplier_return_item_repository,
        purchase_repository,
        purchase_item_repository,
    )

    supplier_return_item_repository.list_by_supplier_return.return_value = [
        create_supplier_return_item(
            purchase_item_id=51,
        )
    ]

    purchase_item_repository.get_by_id.side_effect = (
        lambda purchase_item_id: (
            create_purchase_item(
                purchase_item_id=50,
                purchase_id=40,
            )
            if purchase_item_id == 50
            else create_purchase_item(
                purchase_item_id=51,
                purchase_id=99,
            )
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Todos os itens da remessa devem "
            "pertencer à mesma Nota Fiscal "
            "de compra."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_invalid_existing_purchase_item(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    configure_valid_add_item(
        supplier_return_repository,
        supplier_return_item_repository,
        purchase_repository,
        purchase_item_repository,
    )

    supplier_return_item_repository.list_by_supplier_return.return_value = [
        create_supplier_return_item(
            purchase_item_id=51,
        )
    ]

    purchase_item_repository.get_by_id.side_effect = [
        create_purchase_item(
            purchase_item_id=50,
        ),
        None,
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Um item já cadastrado na remessa não "
            "possui uma origem de compra válida."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_when_no_quantity_is_available(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_valid_add_item(
        supplier_return_repository,
        supplier_return_item_repository,
        purchase_repository,
        purchase_item_repository,
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = (
        []
    )

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não existe quantidade disponível para "
            "remessa neste item de compra."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=1,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_reject_quantity_above_available_balance(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_valid_add_item(
        supplier_return_repository,
        supplier_return_item_repository,
        purchase_repository,
        purchase_item_repository,
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=8,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=8,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=6,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        4
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade remetida é maior que a "
            "quantidade disponível para remessa. "
            "Quantidade máxima permitida: 2."
        ),
    ):
        service.add_item(
            supplier_return_id=20,
            purchase_item_id=50,
            quantity=3,
        )

    supplier_return_item_repository.add.assert_not_called()


def test_should_calculate_available_quantity(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item()
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=8,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=8,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=6,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        4
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 2


def test_should_never_return_negative_available_quantity(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
) -> None:
    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item()
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = (
        []
    )

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        5
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 0


@pytest.mark.parametrize(
    "purchase_item_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_purchase_item_id_on_available_quantity(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    purchase_item_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do item de compra deve ser "
            "maior que zero."
        ),
    ):
        service.get_available_quantity(
            purchase_item_id
        )

    purchase_item_repository.get_by_id.assert_not_called()


def test_should_reject_missing_purchase_item_on_available_quantity(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
) -> None:
    purchase_item_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Item de compra não encontrado.",
    ):
        service.get_available_quantity(
            50
        )


def test_should_distribute_customer_return_using_fifo(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=50,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        ),
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=51,
            quantity_allocated=3,
        ),
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=6,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 5


def test_should_allocate_remaining_fifo_quantity_to_second_purchase(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=51,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=51,
            quantity_allocated=3,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        ),
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=51,
            quantity_allocated=3,
        ),
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=6,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        51
    )

    assert result == 1


def test_should_not_process_same_outbound_item_twice(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item()
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=3,
        ),
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=2,
        ),
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=4,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 4

    outbound_purchase_allocation_repository.list_by_outbound_item.assert_called_once_with(
        80
    )

    customer_return_allocation_repository.list_by_outbound_item.assert_called_once_with(
        80
    )


def test_should_get_supplier_return(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
) -> None:
    expected = create_supplier_return()

    supplier_return_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_supplier_return(
        20
    )

    assert result == expected

    supplier_return_repository.get_by_id.assert_called_once_with(
        20
    )


@pytest.mark.parametrize(
    "supplier_return_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_supplier_return_id_on_get(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da remessa deve ser "
            "maior que zero."
        ),
    ):
        service.get_supplier_return(
            supplier_return_id
        )

    supplier_return_repository.get_by_id.assert_not_called()


def test_should_reject_missing_supplier_return_on_get(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Remessa ao fornecedor não encontrada.",
    ):
        service.get_supplier_return(
            20
        )


def test_should_list_supplier_returns(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
) -> None:
    expected = [
        create_supplier_return(
            supplier_return_id=20,
        ),
        create_supplier_return(
            supplier_return_id=21,
            dispatch_invoice_number="NF-REMESSA-200",
        ),
    ]

    supplier_return_repository.list_all.return_value = (
        expected
    )

    result = service.list_supplier_returns()

    assert result == expected

    supplier_return_repository.list_all.assert_called_once_with()


def test_should_list_supplier_return_items(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        create_supplier_return()
    )

    expected = [
        create_supplier_return_item(
            supplier_return_item_id=70,
        ),
        create_supplier_return_item(
            supplier_return_item_id=71,
            purchase_item_id=51,
        ),
    ]

    supplier_return_item_repository.list_by_supplier_return.return_value = (
        expected
    )

    result = service.list_items(
        20
    )

    assert result == expected

    supplier_return_item_repository.list_by_supplier_return.assert_called_once_with(
        20
    )


def test_should_reject_listing_items_from_missing_supplier_return(
    service: SupplierReturnService,
    supplier_return_repository: Mock,
    supplier_return_item_repository: Mock,
) -> None:
    supplier_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Remessa ao fornecedor não encontrada.",
    ):
        service.list_items(
            20
        )

    supplier_return_item_repository.list_by_supplier_return.assert_not_called()

def test_should_not_make_purchase_available_when_return_only_covers_transfer(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    """
    Saída:
    - 3 unidades de transferência;
    - 5 unidades de compra.

    Devolução:
    - 2 unidades.

    Como a transferência foi consumida primeiro,
    nenhuma unidade deve ficar disponível para
    remessa ao fornecedor.
    """

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=50,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=80,
            transfer_item_id=90,
            quantity_allocated=3,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=2,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 0


def test_should_make_only_return_above_transfer_available_for_purchase(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    """
    Saída:
    - 3 unidades de transferência;
    - 5 unidades de compra.

    Devolução:
    - 4 unidades.

    Resultado:
    - 3 unidades pertencem à transferência;
    - somente 1 unidade pertence à compra.
    """

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=50,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=80,
            transfer_item_id=90,
            quantity_allocated=3,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=4,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 1


def test_should_distribute_return_after_multiple_transfer_allocations(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    """
    Saída:
    - Transferência A: 2 unidades;
    - Transferência B: 3 unidades;
    - Compra: 5 unidades.

    Devolução:
    - 7 unidades.

    As primeiras 5 unidades pertencem às transferências.
    Apenas 2 unidades pertencem à compra.
    """

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=50,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=80,
            transfer_item_id=90,
            quantity_allocated=2,
        ),
        create_outbound_transfer_allocation(
            outbound_item_id=80,
            transfer_item_id=91,
            quantity_allocated=3,
        ),
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=7,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 2


def test_should_preserve_purchase_fifo_after_transfer_quantity_is_consumed(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    """
    Saída:
    - Transferência: 3 unidades;
    - Compra A: 5 unidades;
    - Compra B: 4 unidades.

    Devolução:
    - 10 unidades.

    Distribuição:
    - Transferência: 3;
    - Compra A: 5;
    - Compra B: 2.
    """

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=51,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=51,
            quantity_allocated=4,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=80,
            transfer_item_id=90,
            quantity_allocated=3,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        ),
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=51,
            quantity_allocated=4,
        ),
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=10,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        51
    )

    assert result == 2


def test_should_keep_previous_behavior_when_outbound_has_no_transfer_allocation(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    """
    Sem transferência, o cálculo deve continuar
    seguindo somente o FIFO das compras.
    """

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=50,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = (
        []
    )

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=4,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 4


def test_should_subtract_quantity_already_sent_to_supplier_after_origin_distribution(
    service: SupplierReturnService,
    purchase_item_repository: Mock,
    supplier_return_item_repository: Mock,
    outbound_purchase_allocation_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    """
    Saída:
    - Transferência: 3 unidades;
    - Compra: 5 unidades.

    Cliente devolveu:
    - 7 unidades.

    Da compra:
    - 4 unidades foram devolvidas;
    - 2 já foram remetidas ao fornecedor;
    - restam 2 disponíveis.
    """

    purchase_item_repository.get_by_id.return_value = (
        create_purchase_item(
            purchase_item_id=50,
        )
    )

    outbound_purchase_allocation_repository.list_by_purchase_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=80,
            transfer_item_id=90,
            quantity_allocated=3,
        )
    ]

    outbound_purchase_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_purchase_allocation(
            outbound_item_id=80,
            purchase_item_id=50,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=80,
            quantity_allocated=7,
        )
    ]

    supplier_return_item_repository.get_returned_quantity_by_purchase_item.return_value = (
        2
    )

    result = service.get_available_quantity(
        50
    )

    assert result == 2