from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.models.outbound import Outbound
from src.services.outbound_service import OutboundService


@pytest.fixture
def outbound_repository() -> Mock:
    repository = Mock()

    repository.add.side_effect = (
        lambda outbound: outbound
    )

    repository.save.side_effect = (
        lambda outbound: outbound
    )

    return repository


@pytest.fixture
def outbound_item_repository() -> Mock:
    repository = Mock()

    repository.add.side_effect = (
        lambda outbound_item: outbound_item
    )

    return repository


@pytest.fixture
def allocation_repository() -> Mock:
    repository = Mock()

    repository.add.side_effect = (
        lambda allocation: allocation
    )

    return repository


@pytest.fixture
def purchase_item_repository() -> Mock:
    return Mock()


@pytest.fixture
def part_repository() -> Mock:
    return Mock()


@pytest.fixture
def service(
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> OutboundService:
    return OutboundService(
        outbound_repository=outbound_repository,
        outbound_item_repository=(
            outbound_item_repository
        ),
        outbound_purchase_allocation_repository=(
            allocation_repository
        ),
        purchase_item_repository=(
            purchase_item_repository
        ),
        part_repository=part_repository,
    )


def create_outbound(
    outbound_id: int = 10,
    destination_type: str = "WORK_ORDER",
    work_order_number: str | None = "OS-12345",
    sales_invoice_number: str | None = None,
    created_by: int = 30,
    status: str = "ACTIVE",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=outbound_id,
        destination_type=destination_type,
        work_order_number=work_order_number,
        sales_invoice_number=sales_invoice_number,
        created_by=created_by,
        status=status,
    )


def test_should_create_outbound_with_work_order(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        created_by=30,
    )

    assert isinstance(
        outbound,
        Outbound,
    )

    assert outbound.destination_type == "WORK_ORDER"
    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None
    assert outbound.created_by == 30
    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_not_called()

    outbound_repository.add.assert_called_once_with(
        outbound
    )


def test_should_create_outbound_with_sales_invoice(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="SALE",
        sales_invoice_number="NFV-12345",
        created_by=30,
    )

    assert isinstance(
        outbound,
        Outbound,
    )

    assert outbound.destination_type == "SALE"
    assert outbound.work_order_number is None
    assert outbound.sales_invoice_number == "NFV-12345"
    assert outbound.created_by == 30
    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.add.assert_called_once_with(
        outbound
    )


def test_should_create_outbound_with_both_reference_numbers(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number="NFV-12345",
        created_by=30,
    )

    assert outbound.work_order_number == "OS-12345"

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.add.assert_called_once_with(
        outbound
    )


def test_should_normalize_outbound_fields_on_create(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="  WORK_ORDER  ",
        work_order_number="  OS-12345  ",
        sales_invoice_number="  NFV-12345  ",
        created_by=30,
        status="  active  ",
    )

    assert outbound.destination_type == "WORK_ORDER"
    assert outbound.work_order_number == "OS-12345"

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )


def test_should_convert_blank_work_order_to_none(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="SALE",
        work_order_number="   ",
        sales_invoice_number="NFV-12345",
        created_by=30,
    )

    assert outbound.work_order_number is None

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )


def test_should_convert_blank_sales_invoice_to_none(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number="   ",
        created_by=30,
    )

    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_return_repository_result_on_create(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    persisted_outbound = create_outbound()

    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.add.side_effect = None

    outbound_repository.add.return_value = (
        persisted_outbound
    )

    result = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        created_by=30,
    )

    assert result is persisted_outbound

    outbound_repository.add.assert_called_once()

    created_outbound = (
        outbound_repository.add.call_args.args[0]
    )

    assert isinstance(
        created_outbound,
        Outbound,
    )

    assert (
        created_outbound.destination_type
        == "WORK_ORDER"
    )

    assert (
        created_outbound.work_order_number
        == "OS-12345"
    )

    assert (
        created_outbound.sales_invoice_number
        is None
    )

    assert created_outbound.created_by == 30
    assert created_outbound.status == "ACTIVE"


def test_should_raise_error_when_destination_type_is_blank(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.create_outbound(
            destination_type="   ",
            work_order_number="OS-12345",
            created_by=30,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


@pytest.mark.parametrize(
    "created_by",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_created_by_is_invalid(
    service: OutboundService,
    outbound_repository: Mock,
    created_by: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário deve ser "
            "maior que zero."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=created_by,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_reference_numbers_are_missing(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            created_by=30,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_reference_numbers_are_blank(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="   ",
            sales_invoice_number="   ",
            created_by=30,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_outbound_is_created_cancelled(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Uma saída não pode ser criada "
            "já cancelada."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=30,
            status="CANCELLED",
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_create_status_is_invalid(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=30,
            status=status,
        )

    outbound_repository.add.assert_not_called()


def test_should_raise_error_when_work_order_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    existing_outbound = create_outbound(
        outbound_id=11,
    )

    outbound_repository.get_by_work_order_number.return_value = (
        existing_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "ordem de serviço."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=30,
        )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.add.assert_not_called()


def test_should_raise_error_when_sales_invoice_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    existing_outbound = create_outbound(
        outbound_id=11,
        work_order_number=None,
        sales_invoice_number="NFV-12345",
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        existing_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "nota fiscal de venda."
        ),
    ):
        service.create_outbound(
            destination_type="SALE",
            sales_invoice_number="NFV-12345",
            created_by=30,
        )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.add.assert_not_called()


def test_should_not_check_blank_optional_reference_for_duplicates(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number="   ",
        created_by=30,
    )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_not_called()

    outbound_repository.add.assert_called_once()

def create_part(
    part_id: int = 40,
    is_active: bool = True,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=part_id,
        is_active=is_active,
    )


def create_purchase_item(
    purchase_item_id: int,
    part_id: int = 40,
    quantity_available: int = 10,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=purchase_item_id,
        part_id=part_id,
        quantity_available=quantity_available,
    )


def create_outbound_item(
    outbound_item_id: int = 50,
    outbound_id: int = 10,
    part_id: int = 40,
    quantity: int = 8,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=outbound_item_id,
        outbound_id=outbound_id,
        part_id=part_id,
        quantity=quantity,
    )


def test_should_add_outbound_item_using_single_purchase_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound = create_outbound()

    part = create_part()

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=10,
    )

    persisted_outbound_item = create_outbound_item(
        quantity=8,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    part_repository.get_by_id.return_value = (
        part
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    purchase_item_repository.list_available_by_part.return_value = [
        purchase_item
    ]

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    result = service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=8,
    )

    assert result is persisted_outbound_item

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        40
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )

    purchase_item_repository.list_available_by_part.assert_called_once_with(
        40
    )

    outbound_item_repository.add.assert_called_once()

    created_outbound_item = (
        outbound_item_repository.add.call_args.args[0]
    )

    assert created_outbound_item.outbound_id == 10
    assert created_outbound_item.part_id == 40
    assert created_outbound_item.quantity == 8

    assert purchase_item.quantity_available == 2

    allocation_repository.add.assert_called_once()

    allocation = (
        allocation_repository.add.call_args.args[0]
    )

    assert allocation.outbound_item_id == 50
    assert allocation.purchase_item_id == 60
    assert allocation.quantity_allocated == 8


def test_should_add_outbound_item_using_fifo_allocation(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=3,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=5,
    )

    third_purchase_item = create_purchase_item(
        purchase_item_id=62,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
        third_purchase_item,
    ]

    persisted_outbound_item = create_outbound_item(
        outbound_item_id=50,
        quantity=12,
    )

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    result = service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=12,
    )

    assert result is persisted_outbound_item

    assert first_purchase_item.quantity_available == 0
    assert second_purchase_item.quantity_available == 0
    assert third_purchase_item.quantity_available == 6

    assert allocation_repository.add.call_count == 3

    allocations = [
        call.args[0]
        for call in allocation_repository.add.call_args_list
    ]

    assert allocations[0].outbound_item_id == 50
    assert allocations[0].purchase_item_id == 60
    assert allocations[0].quantity_allocated == 3

    assert allocations[1].outbound_item_id == 50
    assert allocations[1].purchase_item_id == 61
    assert allocations[1].quantity_allocated == 5

    assert allocations[2].outbound_item_id == 50
    assert allocations[2].purchase_item_id == 62
    assert allocations[2].quantity_allocated == 4


def test_should_use_exact_available_quantity_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=3,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=5,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
    ]

    persisted_outbound_item = create_outbound_item(
        quantity=8,
    )

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=8,
    )

    assert first_purchase_item.quantity_available == 0
    assert second_purchase_item.quantity_available == 0

    assert allocation_repository.add.call_count == 2


def test_should_stop_fifo_allocation_after_requested_quantity(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=10,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
    ]

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        create_outbound_item(
            quantity=4,
        )
    )

    service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=4,
    )

    assert first_purchase_item.quantity_available == 6
    assert second_purchase_item.quantity_available == 10

    allocation_repository.add.assert_called_once()

    allocation = (
        allocation_repository.add.call_args.args[0]
    )

    assert allocation.purchase_item_id == 60
    assert allocation.quantity_allocated == 4


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            outbound_id=outbound_id,
            part_id=40,
            quantity=5,
        )

    outbound_repository.get_by_id.assert_not_called()
    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "part_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_part_id_is_invalid_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    part_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da peça deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=part_id,
            quantity=5,
        )

    outbound_repository.get_by_id.assert_not_called()
    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_quantity_is_invalid_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade da saída deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=quantity,
        )

    outbound_repository.get_by_id.assert_not_called()
    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.add_item(
            outbound_id=999,
            part_id=40,
            quantity=5,
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_outbound_is_cancelled_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens "
            "a uma saída cancelada."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=5,
        )

    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_part_is_not_found_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.add_item(
            outbound_id=10,
            part_id=999,
            quantity=5,
        )

    part_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_part_is_inactive_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            is_active=False,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível realizar a saída "
            "de uma peça inativa."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=5,
        )

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_part_is_already_in_outbound(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = [
        create_outbound_item(
            part_id=40,
        )
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Esta peça já foi adicionada à saída."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=5,
        )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )

    purchase_item_repository.list_available_by_part.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_allow_different_part_in_same_outbound(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            part_id=41,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        create_outbound_item(
            part_id=40,
        )
    ]

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        part_id=41,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        purchase_item
    ]

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        create_outbound_item(
            part_id=41,
            quantity=5,
        )
    )

    result = service.add_item(
        outbound_id=10,
        part_id=41,
        quantity=5,
    )

    assert result.part_id == 41
    assert purchase_item.quantity_available == 5

    outbound_item_repository.add.assert_called_once()
    allocation_repository.add.assert_called_once()


def test_should_raise_error_when_stock_is_insufficient(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=2,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=3,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Quantidade disponível insuficiente "
            "para a saída."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=6,
        )

    assert first_purchase_item.quantity_available == 2
    assert second_purchase_item.quantity_available == 3

    outbound_item_repository.add.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_no_stock_is_available(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    purchase_item_repository.list_available_by_part.return_value = (
        []
    )

    with pytest.raises(
        ValueError,
        match=(
            "Quantidade disponível insuficiente "
            "para a saída."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=1,
        )

    outbound_item_repository.add.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_fifo_allocation_is_incomplete(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        purchase_item
    ]

    persisted_outbound_item = create_outbound_item(
        quantity=8,
    )

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    def prevent_quantity_reduction(
        allocation: object,
    ) -> object:
        purchase_item.quantity_available = 0
        return allocation

    allocation_repository.add.side_effect = (
        prevent_quantity_reduction
    )

    result = service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=8,
    )

    assert result is persisted_outbound_item

    allocation_repository.add.assert_called_once()

def test_should_get_outbound(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.get_outbound(
        10
    )

    assert result is outbound

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_get(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.get_outbound(
            outbound_id
        )

    outbound_repository.get_by_id.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_get(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.get_outbound(
            999
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )


def test_should_list_all_outbounds(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
        ),
        create_outbound(
            outbound_id=11,
            work_order_number=None,
            sales_invoice_number="NFV-67890",
        ),
    ]

    outbound_repository.list_all.return_value = (
        outbounds
    )

    result = service.list_outbounds()

    assert result is outbounds

    outbound_repository.list_all.assert_called_once_with()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_return_empty_outbound_list(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.list_all.return_value = []

    result = service.list_outbounds()

    assert result == []

    outbound_repository.list_all.assert_called_once_with()


def test_should_list_outbounds_filtered_by_status(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            status="ACTIVE",
        ),
    ]

    outbound_repository.list_by_status.return_value = (
        outbounds
    )

    result = service.list_outbounds(
        status="  active  ",
    )

    assert result is outbounds

    outbound_repository.list_by_status.assert_called_once_with(
        "ACTIVE"
    )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_list_outbounds_filtered_by_destination_type(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            destination_type="WORK_ORDER",
        ),
    ]

    outbound_repository.list_by_destination_type.return_value = (
        outbounds
    )

    result = service.list_outbounds(
        destination_type="  WORK_ORDER  ",
    )

    assert result is outbounds

    outbound_repository.list_by_destination_type.assert_called_once_with(
        "WORK_ORDER"
    )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()


def test_should_raise_error_when_multiple_filters_are_sent(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match="Informe apenas um filtro por vez.",
    ):
        service.list_outbounds(
            status="ACTIVE",
            destination_type="WORK_ORDER",
        )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_status_filter_is_invalid(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.list_outbounds(
            status=status,
        )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


@pytest.mark.parametrize(
    "destination_type",
    [
        "",
        "   ",
    ],
)
def test_should_raise_error_when_destination_type_filter_is_blank(
    service: OutboundService,
    outbound_repository: Mock,
    destination_type: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.list_outbounds(
            destination_type=destination_type,
        )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_list_outbounds_by_status(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            status="CANCELLED",
        ),
    ]

    outbound_repository.list_by_status.return_value = (
        outbounds
    )

    result = service.list_outbounds_by_status(
        "  cancelled  "
    )

    assert result is outbounds

    outbound_repository.list_by_status.assert_called_once_with(
        "CANCELLED"
    )


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_status_is_invalid_on_list_by_status(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.list_outbounds_by_status(
            status
        )

    outbound_repository.list_by_status.assert_not_called()


def test_should_list_outbounds_by_destination_type(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            destination_type="SALE",
            work_order_number=None,
            sales_invoice_number="NFV-12345",
        ),
    ]

    outbound_repository.list_by_destination_type.return_value = (
        outbounds
    )

    result = service.list_outbounds_by_destination_type(
        "  SALE  "
    )

    assert result is outbounds

    outbound_repository.list_by_destination_type.assert_called_once_with(
        "SALE"
    )


@pytest.mark.parametrize(
    "destination_type",
    [
        "",
        "   ",
    ],
)
def test_should_raise_error_when_destination_type_is_blank_on_list(
    service: OutboundService,
    outbound_repository: Mock,
    destination_type: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.list_outbounds_by_destination_type(
            destination_type
        )

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_list_outbound_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    items = [
        create_outbound_item(
            outbound_item_id=50,
            part_id=40,
            quantity=5,
        ),
        create_outbound_item(
            outbound_item_id=51,
            part_id=41,
            quantity=3,
        ),
    ]

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = (
        items
    )

    result = service.list_outbound_items(
        10
    )

    assert result is items

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )


def test_should_return_empty_outbound_item_list(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    result = service.list_outbound_items(
        10
    )

    assert result == []

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_list_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.list_outbound_items(
            outbound_id
        )

    outbound_repository.get_by_id.assert_not_called()

    outbound_item_repository.list_by_outbound.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_list_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.list_outbound_items(
            999
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_item_repository.list_by_outbound.assert_not_called()

def create_allocation(
    allocation_id: int = 70,
    outbound_item_id: int = 50,
    purchase_item_id: int = 60,
    quantity_allocated: int = 5,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=allocation_id,
        outbound_item_id=outbound_item_id,
        purchase_item_id=purchase_item_id,
        quantity_allocated=quantity_allocated,
    )


def test_should_update_outbound_destination_type(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        destination_type="  INTERNAL_USE  ",
    )

    assert result is outbound
    assert outbound.destination_type == "INTERNAL_USE"

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_update_outbound_work_order_number(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    result = service.update_outbound(
        outbound_id=10,
        work_order_number="  OS-67890  ",
    )

    assert result is outbound

    assert (
        outbound.work_order_number
        == "OS-67890"
    )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-67890"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_update_outbound_sales_invoice_number(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        destination_type="SALE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    result = service.update_outbound(
        outbound_id=10,
        sales_invoice_number="  NFV-67890  ",
    )

    assert result is outbound

    assert (
        outbound.sales_invoice_number
        == "NFV-67890"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-67890"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_update_all_outbound_fields(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    result = service.update_outbound(
        outbound_id=10,
        destination_type="  SALE  ",
        work_order_number="  OS-67890  ",
        sales_invoice_number="  NFV-67890  ",
        status="  active  ",
    )

    assert result is outbound

    assert outbound.destination_type == "SALE"

    assert (
        outbound.work_order_number
        == "OS-67890"
    )

    assert (
        outbound.sales_invoice_number
        == "NFV-67890"
    )

    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-67890"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-67890"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_return_repository_result_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    persisted_outbound = create_outbound(
        outbound_id=10,
        destination_type="INTERNAL_USE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.save.side_effect = None

    outbound_repository.save.return_value = (
        persisted_outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        destination_type="INTERNAL_USE",
    )

    assert result is persisted_outbound

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_save_outbound_when_no_update_field_is_sent(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
    )

    assert result is outbound

    assert outbound.destination_type == "WORK_ORDER"
    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None
    assert outbound.status == "ACTIVE"

    outbound_repository.save.assert_called_once_with(
        outbound
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_update(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.update_outbound(
            outbound_id=outbound_id,
            destination_type="SALE",
        )

    outbound_repository.get_by_id.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.update_outbound(
            outbound_id=999,
            destination_type="SALE",
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_cancelled_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível alterar uma saída "
            "cancelada."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            destination_type="SALE",
        )

    outbound_repository.save.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_destination_type_is_blank_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.update_outbound(
            outbound_id=10,
            destination_type="   ",
        )

    outbound_repository.save.assert_not_called()


def test_should_convert_blank_work_order_to_none_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
        sales_invoice_number="NFV-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        work_order_number="   ",
    )

    assert result is outbound
    assert outbound.work_order_number is None

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_convert_blank_sales_invoice_to_none_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
        sales_invoice_number="NFV-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        sales_invoice_number="   ",
    )

    assert result is outbound

    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None

    outbound_repository.get_by_sales_invoice_number.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_raise_error_when_update_removes_all_reference_numbers(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
        sales_invoice_number=None,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            work_order_number="   ",
        )

    assert outbound.work_order_number is None
    assert outbound.sales_invoice_number is None

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_updated_work_order_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        work_order_number="OS-12345",
    )

    duplicated_outbound = create_outbound(
        outbound_id=11,
        work_order_number="OS-67890",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        duplicated_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "ordem de serviço."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            work_order_number="OS-67890",
        )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-67890"
    )

    outbound_repository.save.assert_not_called()


def test_should_allow_same_work_order_on_same_outbound(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        work_order_number="OS-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        work_order_number="OS-12345",
    )

    assert result is outbound

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_raise_error_when_updated_sales_invoice_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        sales_invoice_number=None,
    )

    duplicated_outbound = create_outbound(
        outbound_id=11,
        work_order_number=None,
        sales_invoice_number="NFV-67890",
        destination_type="SALE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        duplicated_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "nota fiscal de venda."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            sales_invoice_number="NFV-67890",
        )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-67890"
    )

    outbound_repository.save.assert_not_called()


def test_should_allow_same_sales_invoice_on_same_outbound(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        destination_type="SALE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        sales_invoice_number="NFV-12345",
    )

    assert result is outbound

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_status_is_invalid_on_update(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.update_outbound(
            outbound_id=10,
            status=status,
        )

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_status_cancelled_is_used_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Utilize a operação específica "
            "para cancelar a saída."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            status="CANCELLED",
        )

    outbound_repository.save.assert_not_called()


def test_should_cancel_outbound_without_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )

    allocation_repository.list_by_outbound_item.assert_not_called()

    purchase_item_repository.get_by_id.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_cancel_outbound_and_restore_single_allocation(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_item = create_outbound_item(
        outbound_item_id=50,
        quantity=5,
    )

    allocation = create_allocation(
        outbound_item_id=50,
        purchase_item_id=60,
        quantity_allocated=5,
    )

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=2,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    allocation_repository.list_by_outbound_item.return_value = [
        allocation
    ]

    purchase_item_repository.get_by_id.return_value = (
        purchase_item
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    assert purchase_item.quantity_available == 7

    allocation_repository.list_by_outbound_item.assert_called_once_with(
        50
    )

    purchase_item_repository.get_by_id.assert_called_once_with(
        60
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_cancel_outbound_and_restore_multiple_allocations(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    first_outbound_item = create_outbound_item(
        outbound_item_id=50,
        part_id=40,
        quantity=8,
    )

    second_outbound_item = create_outbound_item(
        outbound_item_id=51,
        part_id=41,
        quantity=4,
    )

    first_allocation = create_allocation(
        allocation_id=70,
        outbound_item_id=50,
        purchase_item_id=60,
        quantity_allocated=3,
    )

    second_allocation = create_allocation(
        allocation_id=71,
        outbound_item_id=50,
        purchase_item_id=61,
        quantity_allocated=5,
    )

    third_allocation = create_allocation(
        allocation_id=72,
        outbound_item_id=51,
        purchase_item_id=62,
        quantity_allocated=4,
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        part_id=40,
        quantity_available=0,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        part_id=40,
        quantity_available=2,
    )

    third_purchase_item = create_purchase_item(
        purchase_item_id=62,
        part_id=41,
        quantity_available=1,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        first_outbound_item,
        second_outbound_item,
    ]

    allocation_repository.list_by_outbound_item.side_effect = [
        [
            first_allocation,
            second_allocation,
        ],
        [
            third_allocation,
        ],
    ]

    purchase_items_by_id = {
        60: first_purchase_item,
        61: second_purchase_item,
        62: third_purchase_item,
    }

    purchase_item_repository.get_by_id.side_effect = (
        lambda purchase_item_id: purchase_items_by_id[
            purchase_item_id
        ]
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    assert first_purchase_item.quantity_available == 3
    assert second_purchase_item.quantity_available == 7
    assert third_purchase_item.quantity_available == 5

    assert (
        allocation_repository
        .list_by_outbound_item.call_count
        == 2
    )

    allocation_repository.list_by_outbound_item.assert_any_call(
        50
    )

    allocation_repository.list_by_outbound_item.assert_any_call(
        51
    )

    assert purchase_item_repository.get_by_id.call_count == 3

    purchase_item_repository.get_by_id.assert_any_call(
        60
    )

    purchase_item_repository.get_by_id.assert_any_call(
        61
    )

    purchase_item_repository.get_by_id.assert_any_call(
        62
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_cancel_outbound_item_without_allocations(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_item = create_outbound_item()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    allocation_repository.list_by_outbound_item.return_value = (
        []
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    allocation_repository.list_by_outbound_item.assert_called_once_with(
        50
    )

    purchase_item_repository.get_by_id.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_return_repository_result_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    persisted_outbound = create_outbound(
        status="CANCELLED",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    outbound_repository.save.side_effect = None

    outbound_repository.save.return_value = (
        persisted_outbound
    )

    result = service.cancel_outbound(
        10
    )

    assert result is persisted_outbound
    assert outbound.status == "CANCELLED"

    outbound_repository.save.assert_called_once_with(
        outbound
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.cancel_outbound(
            outbound_id
        )

    outbound_repository.get_by_id.assert_not_called()

    outbound_item_repository.list_by_outbound.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.cancel_outbound(
            999
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_item_repository.list_by_outbound.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_already_cancelled(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match="A saída já está cancelada.",
    ):
        service.cancel_outbound(
            10
        )

    outbound_item_repository.list_by_outbound.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_purchase_item_is_not_found_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_item = create_outbound_item(
        outbound_item_id=50,
    )

    allocation = create_allocation(
        outbound_item_id=50,
        purchase_item_id=999,
        quantity_allocated=5,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    allocation_repository.list_by_outbound_item.return_value = [
        allocation
    ]

    purchase_item_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match=(
            "Item de compra relacionado "
            "à saída não encontrado."
        ),
    ):
        service.cancel_outbound(
            10
        )

    purchase_item_repository.get_by_id.assert_called_once_with(
        999
    )

    assert outbound.status == "ACTIVE"

    outbound_repository.save.assert_not_called()