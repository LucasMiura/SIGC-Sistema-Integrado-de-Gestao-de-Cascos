from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.core_movement import CoreMovement


class CoreMovementRepository:
    """Responsável pela persistência do histórico de movimentações."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        movement_id: int,
    ) -> CoreMovement | None:
        statement = select(CoreMovement).where(
            CoreMovement.id == movement_id
        )
        return self.session.scalar(statement)

    def list_by_part(
        self,
        part_id: int,
    ) -> list[CoreMovement]:
        statement = (
            select(CoreMovement)
            .where(CoreMovement.part_id == part_id)
            .order_by(
                CoreMovement.created_at,
                CoreMovement.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def list_by_reference(
        self,
        reference_type: str,
        reference_id: int,
    ) -> list[CoreMovement]:
        statement = (
            select(CoreMovement)
            .where(
                CoreMovement.reference_type == reference_type,
                CoreMovement.reference_id == reference_id,
            )
            .order_by(CoreMovement.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        movement: CoreMovement,
    ) -> CoreMovement:
        self.session.add(movement)
        self.session.flush()
        return movement