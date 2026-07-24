from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound import Outbound


class OutboundRepository:
    """Responsável pela persistência de saídas."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, outbound_id: int) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.id == outbound_id
        )
        return self.session.scalar(statement)

    def list_all(self) -> list[Outbound]:
        statement = select(Outbound).order_by(
            Outbound.created_at,
            Outbound.id,
        )
        return list(self.session.scalars(statement).all())

    def add(self, outbound: Outbound) -> Outbound:
        self.session.add(outbound)
        self.session.flush()
        return outbound