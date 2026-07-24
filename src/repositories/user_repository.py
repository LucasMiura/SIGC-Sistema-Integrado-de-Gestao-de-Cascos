from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:
    """Responsável pela persistência de usuários."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        return self.session.scalar(statement)

    def get_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        return self.session.scalar(statement)

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement)

    def list_all(self) -> list[User]:
        statement = select(User).order_by(User.full_name)
        return list(self.session.scalars(statement).all())

    def add(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()
        return user