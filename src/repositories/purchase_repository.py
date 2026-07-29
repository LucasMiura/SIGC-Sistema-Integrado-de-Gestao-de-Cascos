from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.purchase import Purchase


class PurchaseRepository:
    """
    Responsável pela persistência de compras.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        purchase_id: int,
    ) -> Purchase | None:
        """
        Busca uma compra pelo identificador.
        """

        statement = select(
            Purchase
        ).where(
            Purchase.id == purchase_id
        )

        return self.session.scalar(statement)

    def get_by_invoice(
        self,
        supplier_id: int,
        invoice_number: str,
        invoice_series: str | None,
    ) -> Purchase | None:
        """
        Busca uma compra pela nota fiscal, série e fornecedor.
        """

        statement = select(
            Purchase
        ).where(
            Purchase.supplier_id == supplier_id,
            Purchase.invoice_number == invoice_number,
            Purchase.invoice_series == invoice_series,
        )

        return self.session.scalar(statement)

    def list_all(
        self,
    ) -> list[Purchase]:
        """
        Lista todas as compras.
        """

        statement = select(
            Purchase
        ).order_by(
            Purchase.issue_date.desc(),
            Purchase.id.desc(),
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Purchase]:
        """
        Lista as compras de determinado fornecedor.
        """

        statement = (
            select(
                Purchase
            )
            .where(
                Purchase.supplier_id == supplier_id
            )
            .order_by(
                Purchase.issue_date.desc(),
                Purchase.id.desc(),
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        purchase: Purchase,
    ) -> Purchase:
        """
        Adiciona uma compra.
        """

        self.session.add(purchase)
        self.session.flush()

        return purchase

    def save(
        self,
        purchase: Purchase,
    ) -> Purchase:
        """
        Salva as alterações de uma compra.
        """

        self.session.add(purchase)
        self.session.flush()

        return purchase