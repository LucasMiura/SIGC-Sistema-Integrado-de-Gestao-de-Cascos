from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.models.transfer_return_item import (
    TransferReturnItem,
)
from src.models.transfer_return import (
    TransferReturn,
)


class TransferReturnItemRepository:
    """
    Responsável pela persistência dos itens
    devolvidos às filiais de origem.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        transfer_return_item_id: int,
    ) -> TransferReturnItem | None:
        statement = (
            select(TransferReturnItem)
            .where(
                TransferReturnItem.id
                == transfer_return_item_id
            )
        )

        return self.session.scalar(
            statement
        )

    def get_by_transfer_return_and_transfer_item(
        self,
        transfer_return_id: int,
        transfer_item_id: int,
    ) -> TransferReturnItem | None:
        statement = (
            select(TransferReturnItem)
            .where(
                TransferReturnItem
                .transfer_return_id
                == transfer_return_id,
                TransferReturnItem
                .transfer_item_id
                == transfer_item_id,
            )
        )

        return self.session.scalar(
            statement
        )

    def list_by_transfer_return(
        self,
        transfer_return_id: int,
    ) -> list[TransferReturnItem]:
        statement = (
            select(TransferReturnItem)
            .where(
                TransferReturnItem
                .transfer_return_id
                == transfer_return_id
            )
            .order_by(
                TransferReturnItem.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_transfer_item(
        self,
        transfer_item_id: int,
    ) -> list[TransferReturnItem]:
        statement = (
            select(TransferReturnItem)
            .where(
                TransferReturnItem.transfer_item_id
                == transfer_item_id
            )
            .order_by(
                TransferReturnItem.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def get_returned_quantity_by_transfer_item(
        self,
        transfer_item_id: int,
    ) -> int:
        """
        Retorna a quantidade efetivamente devolvida
        à filial em devoluções ainda ativas.

        Itens pertencentes a devoluções canceladas
        permanecem registrados para histórico, mas
        deixam de consumir o saldo disponível.
        """

        statement = (
            select(
                func.coalesce(
                    func.sum(
                        TransferReturnItem.quantity
                    ),
                    0,
                )
            )
            .join(
                TransferReturn,
                (
                    TransferReturn.id
                    == TransferReturnItem
                    .transfer_return_id
                ),
            )
            .where(
                TransferReturnItem.transfer_item_id
                == transfer_item_id,
                TransferReturn.status == "ACTIVE",
            )
        )

        returned_quantity = self.session.scalar(
            statement
        )

        return int(
            returned_quantity or 0
        )

    def add(
        self,
        transfer_return_item: TransferReturnItem,
    ) -> TransferReturnItem:
        self.session.add(
            transfer_return_item
        )

        self.session.flush()

        return transfer_return_item

    def save(
        self,
        transfer_return_item: TransferReturnItem,
    ) -> TransferReturnItem:
        self.session.add(
            transfer_return_item
        )

        self.session.flush()

        return transfer_return_item