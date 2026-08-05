from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.services.transfer_service import (
    TransferService,
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
def part_repository() -> Mock:
    return Mock(
        spec=PartRepository,
    )


@pytest.fixture
def service(
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> TransferService:
    return TransferService(
        transfer_repository=transfer_repository,
        transfer_item_repository=(
            transfer_item_repository
        ),
        part_repository=part_repository,
    )


def create_transfer(
    transfer_id: int = 10,
    origin_branch_id: int = 2,
    destination_branch_id: int = 1,
    invoice_number: str = "NF-TRANSFER-100",
    issue_date: str = "2026-08-05",
    status: str = "ACTIVE",
    created_by: int = 30,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=transfer_id,
        origin_branch_id=origin_branch_id,
        destination_branch_id=destination_branch_id,
        invoice_number=invoice_number,
        issue_date=issue_date,
        status=status,
        created_by=created_by,
    )


def create_transfer_item(
    transfer_item_id: int = 20,
    transfer_id: int = 10,
    part_id: int = 40,
    quantity: int = 10,
    quantity_available: int = 10,
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


def create_part(
    part_id: int = 40,
    is_active: int = 1,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=part_id,
        part_code="PECA-TESTE",
        name="Peça Teste",
        is_active=is_active,
    )


def configure_valid_transfer_creation(
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_invoice_number.return_value = (
        None
    )


def configure_valid_add_item(
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    transfer_item_repository.get_by_transfer_and_part.return_value = (
        None
    )


def test_should_create_transfer(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    configure_valid_transfer_creation(
        transfer_repository
    )

    transfer_repository.add.side_effect = (
        lambda transfer: transfer
    )

    created = service.create_transfer(
        origin_branch_id=2,
        destination_branch_id=1,
        invoice_number=" NF-TRANSFER-100 ",
        issue_date=" 2026-08-05 ",
        created_by=30,
        status=" active ",
    )

    assert created.origin_branch_id == 2
    assert created.destination_branch_id == 1
    assert created.invoice_number == "NF-TRANSFER-100"
    assert created.issue_date == "2026-08-05"
    assert created.created_by == 30
    assert created.status == "ACTIVE"

    transfer_repository.get_by_invoice_number.assert_called_once_with(
        "NF-TRANSFER-100"
    )

    transfer_repository.add.assert_called_once_with(
        created
    )


def test_should_return_repository_result_on_create(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    configure_valid_transfer_creation(
        transfer_repository
    )

    persisted_transfer = create_transfer()

    transfer_repository.add.return_value = (
        persisted_transfer
    )

    result = service.create_transfer(
        origin_branch_id=2,
        destination_branch_id=1,
        invoice_number="NF-TRANSFER-100",
        issue_date="2026-08-05",
        created_by=30,
    )

    assert result is persisted_transfer


@pytest.mark.parametrize(
    "origin_branch_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_origin_branch_id(
    service: TransferService,
    transfer_repository: Mock,
    origin_branch_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da filial de origem "
            "deve ser maior que zero."
        ),
    ):
        service.create_transfer(
            origin_branch_id=origin_branch_id,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
        )

    transfer_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "destination_branch_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_destination_branch_id(
    service: TransferService,
    transfer_repository: Mock,
    destination_branch_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da filial de destino "
            "deve ser maior que zero."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=(
                destination_branch_id
            ),
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
        )

    transfer_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "created_by",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_created_by(
    service: TransferService,
    transfer_repository: Mock,
    created_by: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário deve ser "
            "maior que zero."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=created_by,
        )

    transfer_repository.add.assert_not_called()


def test_should_reject_same_origin_and_destination_branch(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A filial de origem deve ser diferente "
            "da filial de destino."
        ),
    ):
        service.create_transfer(
            origin_branch_id=1,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
        )

    transfer_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "invoice_number",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_invoice_number(
    service: TransferService,
    transfer_repository: Mock,
    invoice_number: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O número da Nota Fiscal de "
            "transferência é obrigatório."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number=invoice_number,
            issue_date="2026-08-05",
            created_by=30,
        )

    transfer_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "issue_date",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_issue_date(
    service: TransferService,
    transfer_repository: Mock,
    issue_date: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date=issue_date,
            created_by=30,
        )

    transfer_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
    ],
)
def test_should_reject_blank_status(
    service: TransferService,
    transfer_repository: Mock,
    status: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O status da transferência "
            "é obrigatório."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
            status=status,
        )

    transfer_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_reject_invalid_status(
    service: TransferService,
    transfer_repository: Mock,
    status: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O status da transferência deve ser "
            "ACTIVE ou CANCELLED."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
            status=status,
        )

    transfer_repository.add.assert_not_called()


def test_should_reject_creation_with_cancelled_status(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Uma transferência não pode ser criada "
            "já cancelada."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
            status="CANCELLED",
        )

    transfer_repository.add.assert_not_called()


def test_should_reject_duplicated_invoice_number(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_invoice_number.return_value = (
        create_transfer()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma transferência cadastrada "
            "com esse número de Nota Fiscal."
        ),
    ):
        service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number="NF-TRANSFER-100",
            issue_date="2026-08-05",
            created_by=30,
        )

    transfer_repository.add.assert_not_called()


def test_should_add_transfer_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> None:
    configure_valid_add_item(
        transfer_repository,
        transfer_item_repository,
        part_repository,
    )

    def add_item(
        transfer_item: TransferItem,
    ) -> TransferItem:
        transfer_item.id = 20
        return transfer_item

    transfer_item_repository.add.side_effect = (
        add_item
    )

    created = service.add_item(
        transfer_id=10,
        part_id=40,
        quantity=10,
        return_deadline_days=45,
    )

    assert created.id == 20
    assert created.transfer_id == 10
    assert created.part_id == 40
    assert created.quantity == 10
    assert created.quantity_available == 10
    assert created.return_deadline_days == 45

    transfer_item_repository.get_by_transfer_and_part.assert_called_once_with(
        transfer_id=10,
        part_id=40,
    )

    transfer_item_repository.add.assert_called_once_with(
        created
    )


def test_should_return_repository_result_on_add_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> None:
    configure_valid_add_item(
        transfer_repository,
        transfer_item_repository,
        part_repository,
    )

    persisted_item = create_transfer_item()

    transfer_item_repository.add.return_value = (
        persisted_item
    )

    result = service.add_item(
        transfer_id=10,
        part_id=40,
        quantity=10,
        return_deadline_days=45,
    )

    assert result is persisted_item


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_transfer_id_on_add_item(
    service: TransferService,
    transfer_item_repository: Mock,
    transfer_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da transferência "
            "deve ser maior que zero."
        ),
    ):
        service.add_item(
            transfer_id=transfer_id,
            part_id=40,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "part_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_part_id_on_add_item(
    service: TransferService,
    transfer_item_repository: Mock,
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
            transfer_id=10,
            part_id=part_id,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_quantity_on_add_item(
    service: TransferService,
    transfer_item_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade recebida deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            transfer_id=10,
            part_id=40,
            quantity=quantity,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "return_deadline_days",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_deadline_on_add_item(
    service: TransferService,
    transfer_item_repository: Mock,
    return_deadline_days: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O prazo de devolução deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            transfer_id=10,
            part_id=40,
            quantity=10,
            return_deadline_days=(
                return_deadline_days
            ),
        )

    transfer_item_repository.add.assert_not_called()


def test_should_reject_missing_transfer_on_add_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Transferência não encontrada.",
    ):
        service.add_item(
            transfer_id=10,
            part_id=40,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


def test_should_reject_cancelled_transfer_on_add_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens a uma "
            "transferência que não está ativa."
        ),
    ):
        service.add_item(
            transfer_id=10,
            part_id=40,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


def test_should_reject_missing_part_on_add_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.add_item(
            transfer_id=10,
            part_id=40,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


def test_should_reject_inactive_part_on_add_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
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
            transfer_id=10,
            part_id=40,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


def test_should_reject_duplicated_part_on_add_item(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
    part_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    transfer_item_repository.get_by_transfer_and_part.return_value = (
        create_transfer_item()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Esta peça já foi adicionada "
            "à transferência."
        ),
    ):
        service.add_item(
            transfer_id=10,
            part_id=40,
            quantity=10,
            return_deadline_days=45,
        )

    transfer_item_repository.add.assert_not_called()


def test_should_get_transfer(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    expected = create_transfer()

    transfer_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_transfer(
        10
    )

    assert result == expected

    transfer_repository.get_by_id.assert_called_once_with(
        10
    )


@pytest.mark.parametrize(
    "transfer_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_transfer_id_on_get(
    service: TransferService,
    transfer_repository: Mock,
    transfer_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da transferência "
            "deve ser maior que zero."
        ),
    ):
        service.get_transfer(
            transfer_id
        )

    transfer_repository.get_by_id.assert_not_called()


def test_should_reject_missing_transfer_on_get(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Transferência não encontrada.",
    ):
        service.get_transfer(
            10
        )


def test_should_list_transfers(
    service: TransferService,
    transfer_repository: Mock,
) -> None:
    expected = [
        create_transfer(
            transfer_id=10,
        ),
        create_transfer(
            transfer_id=11,
            invoice_number="NF-TRANSFER-200",
        ),
    ]

    transfer_repository.list_all.return_value = (
        expected
    )

    result = service.list_transfers()

    assert result == expected

    transfer_repository.list_all.assert_called_once_with()


def test_should_list_transfer_items(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer()
    )

    expected = [
        create_transfer_item(
            transfer_item_id=20,
        ),
        create_transfer_item(
            transfer_item_id=21,
            part_id=41,
        ),
    ]

    transfer_item_repository.list_by_transfer.return_value = (
        expected
    )

    result = service.list_items(
        10
    )

    assert result == expected

    transfer_item_repository.list_by_transfer.assert_called_once_with(
        10
    )


def test_should_reject_listing_items_from_missing_transfer(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Transferência não encontrada.",
    ):
        service.list_items(
            10
        )

    transfer_item_repository.list_by_transfer.assert_not_called()


def test_should_get_transfer_item(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    expected = create_transfer_item()

    transfer_item_repository.get_by_id.return_value = (
        expected
    )

    result = service.get_transfer_item(
        20
    )

    assert result == expected

    transfer_item_repository.get_by_id.assert_called_once_with(
        20
    )


@pytest.mark.parametrize(
    "transfer_item_id",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_transfer_item_id_on_get(
    service: TransferService,
    transfer_item_repository: Mock,
    transfer_item_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do item de "
            "transferência deve ser maior que zero."
        ),
    ):
        service.get_transfer_item(
            transfer_item_id
        )

    transfer_item_repository.get_by_id.assert_not_called()


def test_should_reject_missing_transfer_item_on_get(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Item de transferência não encontrado.",
    ):
        service.get_transfer_item(
            20
        )


def test_should_get_available_quantity(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item(
            quantity_available=6,
        )
    )

    result = service.get_available_quantity(
        20
    )

    assert result == 6


def test_should_return_zero_when_available_quantity_is_negative(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item(
            quantity_available=-2,
        )
    )

    result = service.get_available_quantity(
        20
    )

    assert result == 0


def test_should_reduce_available_quantity(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item = create_transfer_item(
        quantity=10,
        quantity_available=10,
    )

    transfer_item_repository.get_by_id.return_value = (
        transfer_item
    )

    transfer_item_repository.save.side_effect = (
        lambda item: item
    )

    result = service.reduce_available_quantity(
        transfer_item_id=20,
        quantity=4,
    )

    assert result.quantity_available == 6

    transfer_item_repository.save.assert_called_once_with(
        transfer_item
    )


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_quantity_on_reduce(
    service: TransferService,
    transfer_item_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade a movimentar deve ser "
            "maior que zero."
        ),
    ):
        service.reduce_available_quantity(
            transfer_item_id=20,
            quantity=quantity,
        )

    transfer_item_repository.get_by_id.assert_not_called()
    transfer_item_repository.save.assert_not_called()


def test_should_reject_quantity_above_available_balance_on_reduce(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item(
            quantity=10,
            quantity_available=6,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade informada é superior "
            "ao saldo disponível do item de "
            "transferência."
        ),
    ):
        service.reduce_available_quantity(
            transfer_item_id=20,
            quantity=7,
        )

    transfer_item_repository.save.assert_not_called()


def test_should_allow_reducing_exact_available_balance(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item = create_transfer_item(
        quantity=10,
        quantity_available=6,
    )

    transfer_item_repository.get_by_id.return_value = (
        transfer_item
    )

    transfer_item_repository.save.side_effect = (
        lambda item: item
    )

    result = service.reduce_available_quantity(
        transfer_item_id=20,
        quantity=6,
    )

    assert result.quantity_available == 0


def test_should_restore_available_quantity(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item = create_transfer_item(
        quantity=10,
        quantity_available=6,
    )

    transfer_item_repository.get_by_id.return_value = (
        transfer_item
    )

    transfer_item_repository.save.side_effect = (
        lambda item: item
    )

    result = service.restore_available_quantity(
        transfer_item_id=20,
        quantity=4,
    )

    assert result.quantity_available == 10

    transfer_item_repository.save.assert_called_once_with(
        transfer_item
    )


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_reject_invalid_quantity_on_restore(
    service: TransferService,
    transfer_item_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade a restaurar deve ser "
            "maior que zero."
        ),
    ):
        service.restore_available_quantity(
            transfer_item_id=20,
            quantity=quantity,
        )

    transfer_item_repository.get_by_id.assert_not_called()
    transfer_item_repository.save.assert_not_called()


def test_should_reject_restore_above_original_quantity(
    service: TransferService,
    transfer_item_repository: Mock,
) -> None:
    transfer_item_repository.get_by_id.return_value = (
        create_transfer_item(
            quantity=10,
            quantity_available=9,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade restaurada não pode "
            "ultrapassar a quantidade originalmente "
            "recebida."
        ),
    ):
        service.restore_available_quantity(
            transfer_item_id=20,
            quantity=2,
        )

    transfer_item_repository.save.assert_not_called()


def test_should_cancel_transfer_without_movements(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer = create_transfer(
        status="ACTIVE",
    )

    transfer_repository.get_by_id.return_value = (
        transfer
    )

    transfer_item_repository.list_by_transfer.return_value = [
        create_transfer_item(
            quantity=10,
            quantity_available=10,
        )
    ]

    transfer_repository.save.side_effect = (
        lambda saved_transfer: saved_transfer
    )

    result = service.cancel_transfer(
        10
    )

    assert result.status == "CANCELLED"

    transfer_repository.save.assert_called_once_with(
        transfer
    )


def test_should_cancel_transfer_without_items(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer = create_transfer(
        status="ACTIVE",
    )

    transfer_repository.get_by_id.return_value = (
        transfer
    )

    transfer_item_repository.list_by_transfer.return_value = (
        []
    )

    transfer_repository.save.side_effect = (
        lambda saved_transfer: saved_transfer
    )

    result = service.cancel_transfer(
        10
    )

    assert result.status == "CANCELLED"


def test_should_reject_already_cancelled_transfer(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match="A transferência já está cancelada.",
    ):
        service.cancel_transfer(
            10
        )

    transfer_item_repository.list_by_transfer.assert_not_called()
    transfer_repository.save.assert_not_called()


def test_should_reject_cancelling_transfer_with_movements(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer(
            status="ACTIVE",
        )
    )

    transfer_item_repository.list_by_transfer.return_value = [
        create_transfer_item(
            quantity=10,
            quantity_available=6,
        )
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível cancelar uma "
            "transferência que possui movimentações."
        ),
    ):
        service.cancel_transfer(
            10
        )

    transfer_repository.save.assert_not_called()


def test_should_reject_cancelling_when_one_of_multiple_items_has_movements(
    service: TransferService,
    transfer_repository: Mock,
    transfer_item_repository: Mock,
) -> None:
    transfer_repository.get_by_id.return_value = (
        create_transfer(
            status="ACTIVE",
        )
    )

    transfer_item_repository.list_by_transfer.return_value = [
        create_transfer_item(
            transfer_item_id=20,
            quantity=10,
            quantity_available=10,
        ),
        create_transfer_item(
            transfer_item_id=21,
            part_id=41,
            quantity=5,
            quantity_available=4,
        ),
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível cancelar uma "
            "transferência que possui movimentações."
        ),
    ):
        service.cancel_transfer(
            10
        )

    transfer_repository.save.assert_not_called()