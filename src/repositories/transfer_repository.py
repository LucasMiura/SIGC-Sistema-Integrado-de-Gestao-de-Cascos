from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.transfer import Transfer


class TransferRepository:
    """Responsável pela persistência de transferências internas."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        transfer_id: int,
    ) -> Transfer | None:
        statement = select(Transfer).where(
            Transfer.id == transfer_id
        )
        return self.session.scalar(statement)

    def list_all(self) -> list[Transfer]:
        statement = select(Transfer).order_by(
            Transfer.created_at,
            Transfer.id,
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        transfer: Transfer,
    ) -> Transfer:
        self.session.add(transfer)
        self.session.flush()
        return transfer