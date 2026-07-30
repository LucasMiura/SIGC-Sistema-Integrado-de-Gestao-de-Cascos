from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.models.customer_return import CustomerReturn
from src.models.customer_return_item import CustomerReturnItem
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.services.customer_return_service import (
    CustomerReturnService,
)


@pytest.fixture
def customer_return_repository() -> Mock:
    """Cria um mock do repositório de devoluções."""

    return Mock(
        spec=CustomerReturnRepository,
    )


@pytest.fixture
def customer_return_item_repository() -> Mock:
    """Cria um mock do repositório de itens de devolução."""

    return Mock(
        spec=CustomerReturnItemRepository,
    )


@pytest.fixture
def customer_return_allocation_repository() -> Mock:
    """Cria um mock do repositório de alocações."""

    return Mock(
        spec=CustomerReturnAllocationRepository,
    )


@pytest.fixture
def outbound_repository() -> Mock:
    """Cria um mock do repositório de saídas."""

    return Mock(
        spec=OutboundRepository,
    )


@pytest.fixture
def outbound_item_repository() -> Mock:
    """Cria um mock do repositório de itens de saída."""

    return Mock(
        spec=OutboundItemRepository,
    )


@pytest.fixture
def part_repository() -> Mock:
    """Cria um mock do repositório de peças."""

    return Mock(
        spec=PartRepository,
    )


@pytest.fixture
def service(
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    customer_return_allocation_repository: Mock,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    part_repository: Mock,
) -> CustomerReturnService:
    """Cria o service com suas dependências simuladas."""

    return CustomerReturnService(
        customer_return_repository=(
            customer_return_repository
        ),
        customer_return_item_repository=(
            customer_return_item_repository
        ),
        customer_return_allocation_repository=(
            customer_return_allocation_repository
        ),
        outbound_repository=outbound_repository,
        outbound_item_repository=(
            outbound_item_repository
        ),
        part_repository=part_repository,
    )


def create_customer_return(
    customer_return_id: int = 1,
    return_type: str = "WORK_ORDER",
    reference_number: str = "OS-100",
    customer_name: str = "Cliente Teste",
    status: str = "ACTIVE",
) -> CustomerReturn:
    """Cria uma devolução para os testes."""

    return CustomerReturn(
        id=customer_return_id,
        return_type=return_type,
        reference_number=reference_number,
        customer_name=customer_name,
        created_by=1,
        status=status,
        notes=None,
    )


def create_outbound(
    outbound_id: int = 10,
    destination_type: str = "WORK_ORDER",
    work_order_number: str | None = "OS-100",
    sales_invoice_number: str | None = None,
    status: str = "ACTIVE",
) -> SimpleNamespace:
    """Cria uma saída simplificada para os testes."""

    return SimpleNamespace(
        id=outbound_id,
        destination_type=destination_type,
        work_order_number=work_order_number,
        sales_invoice_number=sales_invoice_number,
        status=status,
    )


def create_outbound_item(
    outbound_item_id: int = 20,
    outbound_id: int = 10,
    part_id: int = 30,
    quantity: int = 5,
) -> SimpleNamespace:
    """Cria um item de saída simplificado."""

    return SimpleNamespace(
        id=outbound_item_id,
        outbound_id=outbound_id,
        part_id=part_id,
        quantity=quantity,
    )


def create_allocation(
    quantity_allocated: int,
    outbound_item_id: int = 20,
) -> SimpleNamespace:
    """Cria uma alocação simplificada."""

    return SimpleNamespace(
        id=1,
        customer_return_item_id=1,
        outbound_item_id=outbound_item_id,
        quantity_allocated=quantity_allocated,
    )


def configure_work_order_outbound(
    outbound_repository: Mock,
    outbound: SimpleNamespace | None = None,
) -> SimpleNamespace:
    """Configura uma saída por Ordem de Serviço."""

    configured_outbound = outbound or create_outbound()

    outbound_repository.get_by_work_order_number.return_value = (
        configured_outbound
    )

    return configured_outbound


def configure_sale_outbound(
    outbound_repository: Mock,
    outbound: SimpleNamespace | None = None,
) -> SimpleNamespace:
    """Configura uma saída por Nota Fiscal de venda."""

    configured_outbound = outbound or create_outbound(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NF-100",
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        configured_outbound
    )

    return configured_outbound


def test_should_create_work_order_customer_return(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    outbound_repository: Mock,
) -> None:
    configure_work_order_outbound(
        outbound_repository
    )

    customer_return_repository.add.side_effect = (
        lambda customer_return: customer_return
    )

    created = service.create_customer_return(
        return_type=" work_order ",
        reference_number=" OS-100 ",
        customer_name=" Cliente Teste ",
        created_by=1,
        status=" active ",
        notes=" Observação ",
    )

    assert created.return_type == "WORK_ORDER"
    assert created.reference_number == "OS-100"
    assert created.customer_name == "Cliente Teste"
    assert created.created_by == 1
    assert created.status == "ACTIVE"
    assert created.notes == "Observação"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-100"
    )

    customer_return_repository.add.assert_called_once_with(
        created
    )


def test_should_create_sale_customer_return(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    outbound_repository: Mock,
) -> None:
    configure_sale_outbound(
        outbound_repository
    )

    customer_return_repository.add.side_effect = (
        lambda customer_return: customer_return
    )

    created = service.create_customer_return(
        return_type="sale",
        reference_number="NF-100",
        customer_name="Cliente Balcão",
        created_by=1,
    )

    assert created.return_type == "SALE"
    assert created.reference_number == "NF-100"
    assert created.customer_name == "Cliente Balcão"
    assert created.status == "ACTIVE"

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NF-100"
    )


@pytest.mark.parametrize(
    (
        "return_type",
        "reference_number",
        "customer_name",
        "expected_message",
    ),
    [
        (
            "",
            "OS-100",
            "Cliente",
            "O tipo de devolução é obrigatório.",
        ),
        (
            "WORK_ORDER",
            "",
            "Cliente",
            "O número de referência é obrigatório.",
        ),
        (
            "WORK_ORDER",
            "OS-100",
            "",
            "O nome do cliente é obrigatório.",
        ),
        (
            "   ",
            "OS-100",
            "Cliente",
            "O tipo de devolução é obrigatório.",
        ),
        (
            "WORK_ORDER",
            "   ",
            "Cliente",
            "O número de referência é obrigatório.",
        ),
        (
            "WORK_ORDER",
            "OS-100",
            "   ",
            "O nome do cliente é obrigatório.",
        ),
    ],
)
def test_should_reject_missing_required_return_data(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    return_type: str,
    reference_number: str,
    customer_name: str,
    expected_message: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create_customer_return(
            return_type=return_type,
            reference_number=reference_number,
            customer_name=customer_name,
            created_by=1,
        )

    customer_return_repository.add.assert_not_called()


def test_should_reject_invalid_return_type(
    service: CustomerReturnService,
    customer_return_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O tipo de devolução deve ser "
            "WORK_ORDER ou SALE."
        ),
    ):
        service.create_customer_return(
            return_type="TRANSFER",
            reference_number="TR-100",
            customer_name="Cliente Teste",
            created_by=1,
        )

    customer_return_repository.add.assert_not_called()


def test_should_reject_invalid_return_status(
    service: CustomerReturnService,
    customer_return_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O status da devolução deve ser "
            "ACTIVE ou CANCELLED."
        ),
    ):
        service.create_customer_return(
            return_type="WORK_ORDER",
            reference_number="OS-100",
            customer_name="Cliente Teste",
            created_by=1,
            status="FINISHED",
        )

    customer_return_repository.add.assert_not_called()


def test_should_reject_missing_status(
    service: CustomerReturnService,
    customer_return_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match="O status da devolução é obrigatório.",
    ):
        service.create_customer_return(
            return_type="WORK_ORDER",
            reference_number="OS-100",
            customer_name="Cliente Teste",
            created_by=1,
            status=" ",
        )

    customer_return_repository.add.assert_not_called()


def test_should_normalize_empty_notes_to_none(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    outbound_repository: Mock,
) -> None:
    configure_work_order_outbound(
        outbound_repository
    )

    customer_return_repository.add.side_effect = (
        lambda customer_return: customer_return
    )

    created = service.create_customer_return(
        return_type="WORK_ORDER",
        reference_number="OS-100",
        customer_name="Cliente Teste",
        created_by=1,
        notes="   ",
    )

    assert created.notes is None


def test_should_reject_when_original_outbound_is_not_found(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída original não encontrada.",
    ):
        service.create_customer_return(
            return_type="WORK_ORDER",
            reference_number="OS-INEXISTENTE",
            customer_name="Cliente Teste",
            created_by=1,
        )

    customer_return_repository.add.assert_not_called()


def test_should_reject_when_reference_type_does_not_match_outbound(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    outbound_repository: Mock,
) -> None:
    configure_work_order_outbound(
        outbound_repository,
        outbound=create_outbound(
            destination_type="SALE",
            work_order_number="OS-100",
            sales_invoice_number="NF-100",
        ),
    )

    with pytest.raises(
        ValueError,
        match=(
            "A referência informada não corresponde "
            "ao tipo de devolução."
        ),
    ):
        service.create_customer_return(
            return_type="WORK_ORDER",
            reference_number="OS-100",
            customer_name="Cliente Teste",
            created_by=1,
        )

    customer_return_repository.add.assert_not_called()


def test_should_reject_when_original_outbound_is_not_active(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    outbound_repository: Mock,
) -> None:
    configure_work_order_outbound(
        outbound_repository,
        outbound=create_outbound(
            status="CANCELLED",
        ),
    )

    with pytest.raises(
        ValueError,
        match="A saída original não está ativa.",
    ):
        service.create_customer_return(
            return_type="WORK_ORDER",
            reference_number="OS-100",
            customer_name="Cliente Teste",
            created_by=1,
        )

    customer_return_repository.add.assert_not_called()


def test_should_add_item_to_original_outbound(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    customer_return_allocation_repository: Mock,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    part_repository: Mock,
) -> None:
    customer_return = create_customer_return()

    outbound = configure_work_order_outbound(
        outbound_repository
    )

    outbound_item = create_outbound_item(
        outbound_id=outbound.id,
        part_id=30,
        quantity=5,
    )

    customer_return_repository.get_by_id.return_value = (
        customer_return
    )

    part_repository.get_by_id.return_value = (
        SimpleNamespace(
            id=30,
            is_active=1,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = (
        []
    )

    def add_return_item(
        item: CustomerReturnItem,
    ) -> CustomerReturnItem:
        item.id = 100
        return item

    customer_return_item_repository.add.side_effect = (
        add_return_item
    )

    customer_return_allocation_repository.add.side_effect = (
        lambda allocation: allocation
    )

    created_item = service.add_item(
        customer_return_id=1,
        part_id=30,
        quantity=3,
    )

    assert created_item.customer_return_id == 1
    assert created_item.part_id == 30
    assert created_item.quantity == 3
    assert created_item.id == 100

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        outbound.id
    )

    customer_return_item_repository.add.assert_called_once()

    customer_return_allocation_repository.add.assert_called_once()

    allocation = (
        customer_return_allocation_repository
        .add.call_args.args[0]
    )

    assert allocation.customer_return_item_id == 100
    assert allocation.outbound_item_id == outbound_item.id
    assert allocation.quantity_allocated == 3


def test_should_use_only_items_from_original_outbound(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    customer_return_allocation_repository: Mock,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    part_repository: Mock,
) -> None:
    customer_return = create_customer_return(
        reference_number="OS-B"
    )

    second_outbound = create_outbound(
        outbound_id=2,
        work_order_number="OS-B",
    )

    outbound_repository.get_by_work_order_number.return_value = (
        second_outbound
    )

    second_outbound_item = create_outbound_item(
        outbound_item_id=202,
        outbound_id=2,
        part_id=30,
        quantity=5,
    )

    customer_return_repository.get_by_id.return_value = (
        customer_return
    )

    part_repository.get_by_id.return_value = (
        SimpleNamespace(
            id=30,
            is_active=1,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        second_outbound_item
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = (
        []
    )

    def add_return_item(
        item: CustomerReturnItem,
    ) -> CustomerReturnItem:
        item.id = 300
        return item

    customer_return_item_repository.add.side_effect = (
        add_return_item
    )

    service.add_item(
        customer_return_id=1,
        part_id=30,
        quantity=3,
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        2
    )

    allocation = (
        customer_return_allocation_repository
        .add.call_args.args[0]
    )

    assert allocation.outbound_item_id == 202
    assert allocation.quantity_allocated == 3


def test_should_reject_item_not_present_in_original_outbound(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    customer_return_allocation_repository: Mock,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    part_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return()
    )

    outbound = configure_work_order_outbound(
        outbound_repository
    )

    part_repository.get_by_id.return_value = (
        SimpleNamespace(
            id=30,
            is_active=1,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        create_outbound_item(
            outbound_id=outbound.id,
            part_id=99,
        )
    ]

    with pytest.raises(
        ValueError,
        match=(
            "A peça não pertence à saída original "
            "informada."
        ),
    ):
        service.add_item(
            customer_return_id=1,
            part_id=30,
            quantity=1,
        )

    customer_return_item_repository.add.assert_not_called()

    customer_return_allocation_repository.add.assert_not_called()


def test_should_reject_quantity_above_pending_outbound_balance(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    customer_return_allocation_repository: Mock,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    part_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return()
    )

    outbound = configure_work_order_outbound(
        outbound_repository
    )

    outbound_item = create_outbound_item(
        outbound_id=outbound.id,
        part_id=30,
        quantity=5,
    )

    part_repository.get_by_id.return_value = (
        SimpleNamespace(
            id=30,
            is_active=1,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_allocation(
            quantity_allocated=3,
            outbound_item_id=outbound_item.id,
        )
    ]

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade devolvida é superior "
            "à quantidade pendente da saída original."
        ),
    ):
        service.add_item(
            customer_return_id=1,
            part_id=30,
            quantity=3,
        )

    customer_return_item_repository.add.assert_not_called()

    customer_return_allocation_repository.add.assert_not_called()


def test_should_accept_exact_pending_outbound_balance(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    customer_return_allocation_repository: Mock,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    part_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return()
    )

    outbound = configure_work_order_outbound(
        outbound_repository
    )

    outbound_item = create_outbound_item(
        outbound_id=outbound.id,
        part_id=30,
        quantity=5,
    )

    part_repository.get_by_id.return_value = (
        SimpleNamespace(
            id=30,
            is_active=1,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_allocation(
            quantity_allocated=3,
            outbound_item_id=outbound_item.id,
        )
    ]

    def add_return_item(
        item: CustomerReturnItem,
    ) -> CustomerReturnItem:
        item.id = 100
        return item

    customer_return_item_repository.add.side_effect = (
        add_return_item
    )

    created_item = service.add_item(
        customer_return_id=1,
        part_id=30,
        quantity=2,
    )

    assert created_item.quantity == 2

    allocation = (
        customer_return_allocation_repository
        .add.call_args.args[0]
    )

    assert allocation.quantity_allocated == 2
    assert allocation.outbound_item_id == outbound_item.id


def test_should_reject_item_when_customer_return_is_not_found(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Devolução do cliente não encontrada.",
    ):
        service.add_item(
            customer_return_id=999,
            part_id=30,
            quantity=1,
        )

    customer_return_item_repository.add.assert_not_called()


def test_should_reject_item_when_customer_return_is_not_active(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens a uma "
            "devolução que não esteja ativa."
        ),
    ):
        service.add_item(
            customer_return_id=1,
            part_id=30,
            quantity=1,
        )

    customer_return_item_repository.add.assert_not_called()


def test_should_reject_item_when_part_is_not_found(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    part_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return()
    )

    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.add_item(
            customer_return_id=1,
            part_id=999,
            quantity=1,
        )

    customer_return_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
        -10,
    ],
)
def test_should_reject_non_positive_return_quantity(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
    part_repository: Mock,
    quantity: int,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return()
    )

    part_repository.get_by_id.return_value = (
        SimpleNamespace(
            id=30,
            is_active=1,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade devolvida deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            customer_return_id=1,
            part_id=30,
            quantity=quantity,
        )

    customer_return_item_repository.add.assert_not_called()


def test_should_get_customer_return(
    service: CustomerReturnService,
    customer_return_repository: Mock,
) -> None:
    expected = create_customer_return()

    customer_return_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_customer_return(1)

    assert result == expected

    customer_return_repository.get_by_id.assert_called_once_with(
        1
    )


def test_should_raise_when_getting_missing_customer_return(
    service: CustomerReturnService,
    customer_return_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Devolução do cliente não encontrada.",
    ):
        service.get_customer_return(999)


def test_should_list_customer_returns(
    service: CustomerReturnService,
    customer_return_repository: Mock,
) -> None:
    expected = [
        create_customer_return(
            customer_return_id=1,
        ),
        create_customer_return(
            customer_return_id=2,
            reference_number="OS-200",
        ),
    ]

    customer_return_repository.list_all.return_value = (
        expected
    )

    result = service.list_customer_returns()

    assert result == expected

    customer_return_repository.list_all.assert_called_once_with()


def test_should_list_customer_return_items(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        create_customer_return()
    )

    expected = [
        SimpleNamespace(
            id=1,
            customer_return_id=1,
            part_id=30,
            quantity=2,
        ),
        SimpleNamespace(
            id=2,
            customer_return_id=1,
            part_id=31,
            quantity=1,
        ),
    ]

    customer_return_item_repository.list_by_customer_return.return_value = (
        expected
    )

    result = service.list_customer_return_items(1)

    assert result == expected

    customer_return_item_repository.list_by_customer_return.assert_called_once_with(
        1
    )


def test_should_reject_listing_items_from_missing_return(
    service: CustomerReturnService,
    customer_return_repository: Mock,
    customer_return_item_repository: Mock,
) -> None:
    customer_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Devolução do cliente não encontrada.",
    ):
        service.list_customer_return_items(999)

    customer_return_item_repository.list_by_customer_return.assert_not_called()