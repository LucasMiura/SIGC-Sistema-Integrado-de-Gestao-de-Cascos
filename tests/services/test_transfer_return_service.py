from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.models.transfer_return import TransferReturn
from src.models.transfer_return_item import (
    TransferReturnItem,
)
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.repositories.transfer_return_item_repository import (
    TransferReturnItemRepository,
)
from src.repositories.transfer_return_repository import (
    TransferReturnRepository,
)
from src.services.transfer_return_service import (
    TransferReturnService,
)


@pytest.fixture
def transfer_return_repository() -> Mock:
    return Mock(
        spec=TransferReturnRepository,
    )


@pytest.fixture
def transfer_return_item_repository() -> Mock:
    return Mock(
        spec=TransferReturnItemRepository,
    )


@pytest.fixture
def transfer_repository() -> Mock:
    return Mock(
        spec=TransferRepository,
    )


@pytest.fixture
def transfer_item_repository() -> Mock:
    return Mock(
        spec=TransferItemRepository,
    )


@pytest.fixture
def outbound_transfer_allocation_repository() -> Mock:
    repository = Mock(
        spec=OutboundTransferAllocationRepository,
    )

    repository.list_by_transfer_item.return_value = []
    repository.list_by_outbound_item.return_value = []

    return repository


@pytest.fixture
def customer_return_allocation_repository() -> Mock:
    repository = Mock(
        spec=CustomerReturnAllocationRepository,
    )

    repository.list_by_outbound_item.return_value = []

    return repository


@pytest.fixture
def service(
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> TransferReturnService:
    return TransferReturnService(
        transfer_return_repository=(
            transfer_return_repository
        ),
        transfer_return_item_repository=(
            transfer_return_item_repository
        ),
        transfer_repository=transfer_repository,
        transfer_item_repository=(
            transfer_item_repository
        ),
        outbound_transfer_allocation_repository=(
            outbound_transfer_allocation_repository
        ),
        customer_return_allocation_repository=(
            customer_return_allocation_repository
        ),
    )


def create_transfer(
    transfer_id: int = 10,
    status: str = "ACTIVE",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_id,
        origin_branch_id=2,
        destination_branch_id=1,
        invoice_number="NF-TRANSFER-100",
        issue_date="2026-08-05",
        status=status,
        created_by=30,
    )


def create_transfer_item(
    transfer_item_id: int = 20,
    transfer_id: int = 10,
    part_id: int = 40,
    quantity: int = 8,
    quantity_available: int = 0,
    return_deadline_days: int = 45,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_item_id,
        transfer_id=transfer_id,
        part_id=part_id,
        quantity=quantity,
        quantity_available=quantity_available,
        return_deadline_days=return_deadline_days,
    )


def create_transfer_return(
    transfer_return_id: int = 30,
    transfer_id: int = 10,
    dispatch_invoice_number: str = "NF-RETURN-100",
    dispatch_invoice_series: str | None = "1",
    issue_date: str = "2026-08-05",
    created_by: int = 50,
    status: str = "ACTIVE",
    notes: str | None = "Devolução de teste.",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_return_id,
        transfer_id=transfer_id,
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


def create_transfer_return_item(
    transfer_return_item_id: int = 60,
    transfer_return_id: int = 30,
    transfer_item_id: int = 20,
    quantity: int = 4,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_return_item_id,
        transfer_return_id=transfer_return_id,
        transfer_item_id=transfer_item_id,
        quantity=quantity,
    )


def create_outbound_transfer_allocation(
    outbound_item_id: int = 70,
    transfer_item_id: int = 20,
    quantity_allocated: int = 8,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=1,
        outbound_item_id=outbound_item_id,
        transfer_item_id=transfer_item_id,
        quantity_allocated=quantity_allocated,
    )


def create_customer_return_allocation(
    outbound_item_id: int = 70,
    quantity_allocated: int = 6,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=1,
        customer_return_item_id=80,
        outbound_item_id=outbound_item_id,
        quantity_allocated=quantity_allocated,
    )


def configure_valid_creation(
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    transfer_return_repository.get_by_dispatch_invoice_number.return_value = (
        None
    )


def configure_valid_add_item(
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        create_transfer_return()
    )

    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item()
    )

    transfer_return_item_repository.get_by_transfer_return_and_transfer_item.return_value = (
        None
    )


def configure_available_quantity(
    transfer_item_repository: Mock,
    transfer_return_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
    returned_by_customer: int = 6,
    already_returned_to_branch: int = 0,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item()
    )

    outbound_transfer_allocation_repository.list_by_transfer_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=20,
            quantity_allocated=8,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=20,
            quantity_allocated=8,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=70,
            quantity_allocated=(
                returned_by_customer
            ),
        )
    ]

    transfer_return_item_repository.get_returned_quantity_by_transfer_item.return_value = (
        already_returned_to_branch
    )


def test_should_create_transfer_return(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    configure_valid_creation(
        transfer_return_repository,
        transfer_repository,
    )

    transfer_return_repository.add.side_effect = (
        lambda transfer_return: transfer_return
    )

    created = service.create_transfer_return(
        transfer_id=10,
        dispatch_invoice_number=" NF-RETURN-100 ",
        dispatch_invoice_series=" 1 ",
        issue_date=" 2026-08-05 ",
        created_by=50,
        status=" active ",
        notes=" Devolução parcial ",
    )

    assert created.transfer_id == 10

    assert (
        created.dispatch_invoice_number
        == "NF-RETURN-100"
    )

    assert created.dispatch_invoice_series == "1"
    assert created.issue_date == "2026-08-05"
    assert created.created_by == 50
    assert created.status == "ACTIVE"
    assert created.notes == "Devolução parcial"

    transfer_repository.get_by_id.assert_called_once_with(
        10
    )

    transfer_return_repository.get_by_dispatch_invoice_number.assert_called_once_with(
        "NF-RETURN-100"
    )

    transfer_return_repository.add.assert_called_once_with(
        created
    )


def test_should_create_without_optional_fields(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    configure_valid_creation(
        transfer_return_repository,
        transfer_repository,
    )

    transfer_return_repository.add.side_effect = (
        lambda transfer_return: transfer_return
    )

    created = service.create_transfer_return(
        transfer_id=10,
        dispatch_invoice_number="NF-RETURN-100",
        issue_date="2026-08-05",
        created_by=50,
    )

    assert created.dispatch_invoice_series is None
    assert created.notes is None
    assert created.status == "ACTIVE"


def test_should_convert_blank_optional_fields_to_none(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    configure_valid_creation(
        transfer_return_repository,
        transfer_repository,
    )

    transfer_return_repository.add.side_effect = (
        lambda transfer_return: transfer_return
    )

    created = service.create_transfer_return(
        transfer_id=10,
        dispatch_invoice_number="NF-RETURN-100",
        dispatch_invoice_series="   ",
        issue_date="2026-08-05",
        created_by=50,
        notes="   ",
    )

    assert created.dispatch_invoice_series is None
    assert created.notes is None


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_transfer_id_on_create(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da transferência "
            "deve ser maior que zero."
        ),
    ):
        service.create_transfer_return(
            transfer_id=transfer_id,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
        )

    transfer_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "created_by",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_created_by(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    created_by: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário deve ser "
            "maior que zero."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=created_by,
        )

    transfer_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "dispatch_invoice_number",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_invoice_number(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    dispatch_invoice_number: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O número da Nota Fiscal de Simples "
            "Remessa é obrigatório."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number=(
                dispatch_invoice_number
            ),
            issue_date="2026-08-05",
            created_by=50,
        )

    transfer_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "issue_date",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_issue_date(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    issue_date: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date=issue_date,
            created_by=50,
        )

    transfer_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_status(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    status: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O status da devolução à filial "
            "é obrigatório."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
            status=status,
        )

    transfer_return_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_reject_invalid_status(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    status: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O status da devolução à filial deve "
            "ser ACTIVE ou CANCELLED."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
            status=status,
        )

    transfer_return_repository.add.assert_not_called()


def test_should_reject_creation_with_cancelled_status(
    service: TransferReturnService,
    transfer_return_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Uma devolução à filial não pode ser "
            "criada já cancelada."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
            status="CANCELLED",
        )

    transfer_return_repository.add.assert_not_called()


def test_should_reject_missing_transfer_on_create(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Transferência não encontrada.",
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
        )

    transfer_return_repository.add.assert_not_called()


def test_should_reject_cancelled_transfer_on_create(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível registrar devolução "
            "para uma transferência que não está "
            "ativa."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
        )

    transfer_return_repository.add.assert_not_called()


def test_should_reject_duplicated_invoice_number(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    transfer_return_repository.get_by_dispatch_invoice_number.return_value = (
        create_transfer_return()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma devolução à filial "
            "cadastrada com esse número de Nota "
            "Fiscal de Simples Remessa."
        ),
    ):
        service.create_transfer_return(
            transfer_id=10,
            dispatch_invoice_number="NF-RETURN-100",
            issue_date="2026-08-05",
            created_by=50,
        )

    transfer_return_repository.add.assert_not_called()


def test_should_add_transfer_return_item(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_valid_add_item(
        transfer_return_repository,
        transfer_return_item_repository,
        transfer_item_repository,
    )

    configure_available_quantity(
        transfer_item_repository,
        transfer_return_item_repository,
        outbound_transfer_allocation_repository,
        customer_return_allocation_repository,
        returned_by_customer=6,
        already_returned_to_branch=2,
    )

    def add_item(
        transfer_return_item: TransferReturnItem,
    ) -> TransferReturnItem:
        transfer_return_item.id = 60
        return transfer_return_item

    transfer_return_item_repository.add.side_effect = (
        add_item
    )

    created = service.add_item(
        transfer_return_id=30,
        transfer_item_id=20,
        quantity=4,
    )

    assert created.id == 60
    assert created.transfer_return_id == 30
    assert created.transfer_item_id == 20
    assert created.quantity == 4

    transfer_return_item_repository.add.assert_called_once_with(
        created
    )


@pytest.mark.parametrize(
    "transfer_return_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_return_id_on_add_item(
    service: TransferReturnService,
    transfer_return_item_repository: Mock,
    transfer_return_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da devolução à filial "
            "deve ser maior que zero."
        ),
    ):
        service.add_item(
            transfer_return_id=transfer_return_id,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "transfer_item_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_transfer_item_id_on_add(
    service: TransferReturnService,
    transfer_return_item_repository: Mock,
    transfer_item_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do item de "
            "transferência deve ser maior que zero."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=transfer_item_id,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_quantity_on_add(
    service: TransferReturnService,
    transfer_return_item_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade devolvida deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=quantity,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_missing_transfer_return_on_add(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Devolução à filial não encontrada.",
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_cancelled_return_on_add(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        create_transfer_return(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens a uma "
            "devolução à filial que não está ativa."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_missing_transfer_item_on_add(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        create_transfer_return()
    )

    transfer_item_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Item de transferência não encontrado.",
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_item_from_different_transfer(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        create_transfer_return(
            transfer_id=10,
        )
    )

    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item(
            transfer_id=99,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "O item informado não pertence à "
            "transferência vinculada à devolução."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_duplicated_item(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    configure_valid_add_item(
        transfer_return_repository,
        transfer_return_item_repository,
        transfer_item_repository,
    )

    transfer_return_item_repository.get_by_transfer_return_and_transfer_item.return_value = (
        create_transfer_return_item()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Este item de transferência já foi "
            "adicionado à devolução."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_when_no_quantity_is_available(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_valid_add_item(
        transfer_return_repository,
        transfer_return_item_repository,
        transfer_item_repository,
    )

    configure_available_quantity(
        transfer_item_repository,
        transfer_return_item_repository,
        outbound_transfer_allocation_repository,
        customer_return_allocation_repository,
        returned_by_customer=4,
        already_returned_to_branch=4,
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não existe quantidade disponível para "
            "devolução à filial neste item de "
            "transferência."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=1,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_reject_quantity_above_available(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
    transfer_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_valid_add_item(
        transfer_return_repository,
        transfer_return_item_repository,
        transfer_item_repository,
    )

    configure_available_quantity(
        transfer_item_repository,
        transfer_return_item_repository,
        outbound_transfer_allocation_repository,
        customer_return_allocation_repository,
        returned_by_customer=6,
        already_returned_to_branch=4,
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade devolvida é maior que a "
            "quantidade disponível para devolução "
            "à filial. Quantidade máxima permitida: 2."
        ),
    ):
        service.add_item(
            transfer_return_id=30,
            transfer_item_id=20,
            quantity=3,
        )

    transfer_return_item_repository.add.assert_not_called()


def test_should_calculate_available_quantity(
    service: TransferReturnService,
    transfer_item_repository: Mock,
    transfer_return_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_available_quantity(
        transfer_item_repository,
        transfer_return_item_repository,
        outbound_transfer_allocation_repository,
        customer_return_allocation_repository,
        returned_by_customer=6,
        already_returned_to_branch=4,
    )

    result = service.get_available_quantity(
        20
    )

    assert result == 2


def test_should_return_zero_when_balance_is_negative(
    service: TransferReturnService,
    transfer_item_repository: Mock,
    transfer_return_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    configure_available_quantity(
        transfer_item_repository,
        transfer_return_item_repository,
        outbound_transfer_allocation_repository,
        customer_return_allocation_repository,
        returned_by_customer=2,
        already_returned_to_branch=5,
    )

    result = service.get_available_quantity(
        20
    )

    assert result == 0


def test_should_distribute_customer_return_in_transfer_fifo(
    service: TransferReturnService,
    transfer_item_repository: Mock,
    transfer_return_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item(
            transfer_item_id=21,
        )
    )

    outbound_transfer_allocation_repository.list_by_transfer_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=21,
            quantity_allocated=5,
        )
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=20,
            quantity_allocated=4,
        ),
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=21,
            quantity_allocated=5,
        ),
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=70,
            quantity_allocated=6,
        )
    ]

    transfer_return_item_repository.get_returned_quantity_by_transfer_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        21
    )

    assert result == 2


def test_should_not_process_same_outbound_item_twice(
    service: TransferReturnService,
    transfer_item_repository: Mock,
    transfer_return_item_repository: Mock,
    outbound_transfer_allocation_repository: Mock,
    customer_return_allocation_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item()
    )

    outbound_transfer_allocation_repository.list_by_transfer_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=20,
            quantity_allocated=3,
        ),
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=20,
            quantity_allocated=2,
        ),
    ]

    outbound_transfer_allocation_repository.list_by_outbound_item.return_value = [
        create_outbound_transfer_allocation(
            outbound_item_id=70,
            transfer_item_id=20,
            quantity_allocated=5,
        )
    ]

    customer_return_allocation_repository.list_by_outbound_item.return_value = [
        create_customer_return_allocation(
            outbound_item_id=70,
            quantity_allocated=4,
        )
    ]

    transfer_return_item_repository.get_returned_quantity_by_transfer_item.return_value = (
        0
    )

    result = service.get_available_quantity(
        20
    )

    assert result == 4

    outbound_transfer_allocation_repository.list_by_outbound_item.assert_called_once_with(
        70
    )

    customer_return_allocation_repository.list_by_outbound_item.assert_called_once_with(
        70
    )


def test_should_get_transfer_return(
    service: TransferReturnService,
    transfer_return_repository: Mock,
) -> None:
    expected = create_transfer_return()

    transfer_return_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_transfer_return(
        30
    )

    assert result == expected

def test_should_cancel_transfer_return(
    service: TransferReturnService,
    transfer_return_repository: Mock,
) -> None:
    transfer_return = create_transfer_return(
        status="ACTIVE",
    )

    transfer_return_repository.get_by_id.return_value = (
        transfer_return
    )

    transfer_return_repository.save.side_effect = (
        lambda entity: entity
    )

    result = service.cancel_transfer_return(
        30
    )

    assert result.status == "CANCELLED"

    transfer_return_repository.save.assert_called_once_with(
        transfer_return
    )

def test_should_reject_already_cancelled_transfer_return(
    service: TransferReturnService,
    transfer_return_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        create_transfer_return(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "A devolução à filial já está "
            "cancelada."
        ),
    ):
        service.cancel_transfer_return(
            30
        )

    transfer_return_repository.save.assert_not_called()


def test_should_reject_missing_transfer_return_on_get(
    service: TransferReturnService,
    transfer_return_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Devolução à filial não encontrada.",
    ):
        service.get_transfer_return(
            30
        )


def test_should_list_transfer_returns(
    service: TransferReturnService,
    transfer_return_repository: Mock,
) -> None:
    expected = [
        create_transfer_return(
            transfer_return_id=30,
        ),
        create_transfer_return(
            transfer_return_id=31,
            dispatch_invoice_number="NF-RETURN-200",
        ),
    ]

    transfer_return_repository.list_all.return_value = (
        expected
    )

    result = service.list_transfer_returns()

    assert result == expected

    transfer_return_repository.list_all.assert_called_once_with()


def test_should_list_returns_by_transfer(
    service: TransferReturnService,
    transfer_repository: Mock,
    transfer_return_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    expected = [
        create_transfer_return(),
    ]

    transfer_return_repository.list_by_transfer.return_value = (
        expected
    )

    result = service.list_by_transfer(
        10
    )

    assert result == expected

    transfer_return_repository.list_by_transfer.assert_called_once_with(
        10
    )


def test_should_reject_missing_transfer_on_list(
    service: TransferReturnService,
    transfer_repository: Mock,
    transfer_return_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Transferência não encontrada.",
    ):
        service.list_by_transfer(
            10
        )

    transfer_return_repository.list_by_transfer.assert_not_called()


def test_should_list_transfer_return_items(
    service: TransferReturnService,
    transfer_return_repository: Mock,
    transfer_return_item_repository: Mock,
) -> None:
    transfer_return_repository.get_by_id.return_value = (
        create_transfer_return()
    )

    expected = [
        create_transfer_return_item(),
    ]

    transfer_return_item_repository.list_by_transfer_return.return_value = (
        expected
    )

    result = service.list_items(
        30
    )

    assert result == expected