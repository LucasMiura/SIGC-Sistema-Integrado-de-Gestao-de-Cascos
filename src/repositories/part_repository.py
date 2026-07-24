from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.part import Part


class PartRepository:
    """Responsável pela persistência de peças."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, part_id: int) -> Part | None:
        statement = select(Part).where(Part.id == part_id)
        return self.session.scalar(statement)

    def get_by_code(self, part_code: str) -> Part | None:
        statement = select(Part).where(Part.part_code == part_code)
        return self.session.scalar(statement)

    def list_all(self) -> list[Part]:
        statement = select(Part).order_by(Part.name)
        return list(self.session.scalars(statement).all())

    def add(self, part: Part) -> Part:
        self.session.add(part)
        self.session.flush()
        return part