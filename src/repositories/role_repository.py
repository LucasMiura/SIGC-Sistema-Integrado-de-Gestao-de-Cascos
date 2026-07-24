from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.role import Role


class RoleRepository:
    """Responsável pela persistência de perfis de acesso."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, role_id: int) -> Role | None:
        statement = select(Role).where(Role.id == role_id)
        return self.session.scalar(statement)

    def get_by_name(self, name: str) -> Role | None:
        statement = select(Role).where(Role.name == name)
        return self.session.scalar(statement)

    def list_all(self) -> list[Role]:
        statement = select(Role).order_by(Role.name)
        return list(self.session.scalars(statement).all())

    def add(self, role: Role) -> Role:
        self.session.add(role)
        self.session.flush()
        return role