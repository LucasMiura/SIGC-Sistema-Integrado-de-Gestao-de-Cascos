from src.models.role import Role
from src.repositories.role_repository import RoleRepository


class RoleService:
    """Regras de negócio relacionadas a perfis de acesso."""

    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def get_by_id(self, role_id: int) -> Role | None:
        return self.repository.get_by_id(role_id)

    def list_all(self) -> list[Role]:
        return self.repository.list_all()

    def create(
        self,
        name: str,
        description: str | None = None,
    ) -> Role:
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError(
                "O nome do perfil é obrigatório."
            )

        existing_role = self.repository.get_by_name(
            normalized_name
        )

        if existing_role is not None:
            raise ValueError(
                "Já existe um perfil com este nome."
            )

        role = Role(
            name=normalized_name,
            description=description,
        )

        return self.repository.add(role)