from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.part import Part


class PartRepository:
    """Responsável pela persistência de peças."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        part_id: int,
    ) -> Part | None:
        """Busca uma peça pelo identificador."""

        statement = select(Part).where(
            Part.id == part_id
        )

        return self.session.scalar(statement)

    def get_by_supplier_and_code(
        self,
        supplier_id: int,
        part_code: str,
    ) -> Part | None:
        """Busca uma peça pelo fornecedor e código original."""

        statement = select(Part).where(
            Part.supplier_id == supplier_id,
            Part.part_code == part_code,
        )

        return self.session.scalar(statement)

    def list_all(self) -> list[Part]:
        """Lista todas as peças."""

        statement = select(Part).order_by(
            Part.name,
            Part.part_code,
            Part.id,
        )

        return list(
            self.session.scalars(statement).all()
        )

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Part]:
        """Lista as peças associadas a um fornecedor."""

        statement = (
            select(Part)
            .where(
                Part.supplier_id == supplier_id
            )
            .order_by(
                Part.name,
                Part.part_code,
                Part.id,
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def add(
        self,
        part: Part,
    ) -> Part:
        """Adiciona uma nova peça à sessão."""

        self.session.add(part)
        self.session.flush()

        return part

    def save(
        self,
        part: Part,
    ) -> Part:
        """Persiste alterações realizadas em uma peça."""

        self.session.add(part)
        self.session.flush()

        return part