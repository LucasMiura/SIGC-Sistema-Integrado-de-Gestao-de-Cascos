from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem

from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)


class TransferService:
    """Regras de negócio relacionadas às transferências."""

    def __init__(
        self,
        transfer_repository: TransferRepository,
        transfer_item_repository: TransferItemRepository,
        part_repository: PartRepository,
        purchase_item_repository: PurchaseItemRepository,
    ):
        self.transfer_repository = (
            transfer_repository
        )

        self.transfer_item_repository = (
            transfer_item_repository
        )

        self.part_repository = (
            part_repository
        )

        self.purchase_item_repository = (
            purchase_item_repository
        )