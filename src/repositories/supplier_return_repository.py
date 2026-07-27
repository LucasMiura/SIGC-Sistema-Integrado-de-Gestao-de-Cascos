from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier_return import SupplierReturn


class SupplierReturnRepository:
    """Responsável pela persistência das remessas aos fornecedores."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        supplier_return_id: int,
    ) -> SupplierReturn | None:
        statement = select(SupplierReturn).where(
            SupplierReturn.id == supplier_return_id
        )

        return self.session.scalar(statement)

    def get_by_dispatch_invoice_number(
        self,
        dispatch_invoice_number: str,
    ) -> SupplierReturn | None:
        statement = select(SupplierReturn).where(
            SupplierReturn.dispatch_invoice_number
            == dispatch_invoice_number
        )

        return self.session.scalar(statement)

    def list_all(
        self,
    ) -> list[SupplierReturn]:
        statement = select(SupplierReturn).order_by(
            SupplierReturn.issue_date,
            SupplierReturn.id,
        )

        return list(
            self.session.scalars(statement).all()
        )

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierReturn]:
        statement = (
            select(SupplierReturn)
            .where(
                SupplierReturn.supplier_id
                == supplier_id
            )
            .order_by(
                SupplierReturn.issue_date,
                SupplierReturn.id,
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def add(
        self,
        supplier_return: SupplierReturn,
    ) -> SupplierReturn:
        self.session.add(supplier_return)
        self.session.flush()

        return supplier_return

    def save(
        self,
        supplier_return: SupplierReturn,
    ) -> SupplierReturn:
        self.session.add(supplier_return)
        self.session.flush()

        return supplier_return