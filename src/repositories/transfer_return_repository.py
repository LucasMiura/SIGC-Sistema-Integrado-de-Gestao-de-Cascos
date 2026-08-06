from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.transfer_return import TransferReturn


class TransferReturnRepository:
    """
    Responsável pela persistência das remessas
    devolvidas às filiais de origem.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        transfer_return_id: int,
    ) -> TransferReturn | None:
        statement = (
            select(TransferReturn)
            .where(
                TransferReturn.id
                == transfer_return_id
            )
        )

        return self.session.scalar(
            statement
        )

    def get_by_dispatch_invoice_number(
        self,
        dispatch_invoice_number: str,
    ) -> TransferReturn | None:
        statement = (
            select(TransferReturn)
            .where(
                TransferReturn
                .dispatch_invoice_number
                == dispatch_invoice_number
            )
        )

        return self.session.scalar(
            statement
        )

    def list_all(
        self,
    ) -> list[TransferReturn]:
        statement = (
            select(TransferReturn)
            .order_by(
                TransferReturn.issue_date,
                TransferReturn.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_transfer(
        self,
        transfer_id: int,
    ) -> list[TransferReturn]:
        statement = (
            select(TransferReturn)
            .where(
                TransferReturn.transfer_id
                == transfer_id
            )
            .order_by(
                TransferReturn.issue_date,
                TransferReturn.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        transfer_return: TransferReturn,
    ) -> TransferReturn:
        self.session.add(
            transfer_return
        )

        self.session.flush()

        return transfer_return

    def save(
        self,
        transfer_return: TransferReturn,
    ) -> TransferReturn:
        self.session.add(
            transfer_return
        )

        self.session.flush()

        return transfer_return