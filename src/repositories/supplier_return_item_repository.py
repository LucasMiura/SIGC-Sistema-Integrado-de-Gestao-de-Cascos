from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.models.supplier_return_item import (
    SupplierReturnItem,
)
from src.models.supplier_return import (
    SupplierReturn,
)


class SupplierReturnItemRepository:
    """Responsável pela persistência dos itens das remessas."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        supplier_return_item_id: int,
    ) -> SupplierReturnItem | None:
        statement = select(SupplierReturnItem).where(
            SupplierReturnItem.id
            == supplier_return_item_id
        )

        return self.session.scalar(statement)
    
    def get_by_supplier_return_and_purchase_item(
        self,
        supplier_return_id: int,
        purchase_item_id: int,
    ) -> SupplierReturnItem | None:
        statement = select(SupplierReturnItem).where(
            SupplierReturnItem.supplier_return_id
            == supplier_return_id,
            SupplierReturnItem.purchase_item_id
            == purchase_item_id,
        )

        return self.session.scalar(statement)

    def list_by_supplier_return(
        self,
        supplier_return_id: int,
    ) -> list[SupplierReturnItem]:
        statement = (
            select(SupplierReturnItem)
            .where(
                SupplierReturnItem.supplier_return_id
                == supplier_return_id
            )
            .order_by(
                SupplierReturnItem.id
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def list_by_purchase_item(
        self,
        purchase_item_id: int,
    ) -> list[SupplierReturnItem]:
        statement = (
            select(SupplierReturnItem)
            .where(
                SupplierReturnItem.purchase_item_id
                == purchase_item_id
            )
            .order_by(
                SupplierReturnItem.id
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def get_returned_quantity_by_purchase_item(
        self,
        purchase_item_id: int,
    ) -> int:
        """
        Retorna a quantidade efetivamente remetida
        em remessas ainda ativas.

        Itens de remessas canceladas permanecem no
        histórico, mas deixam de consumir o saldo.
        """

        statement = (
            select(
                func.coalesce(
                    func.sum(
                        SupplierReturnItem.quantity
                    ),
                    0,
                )
            )
            .join(
                SupplierReturn,
                (
                    SupplierReturn.id
                    == SupplierReturnItem
                    .supplier_return_id
                ),
            )
            .where(
                SupplierReturnItem.purchase_item_id
                == purchase_item_id,
                SupplierReturn.status == "ACTIVE",
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
        supplier_return_item: SupplierReturnItem,
    ) -> SupplierReturnItem:
        self.session.add(supplier_return_item)
        self.session.flush()

        return supplier_return_item