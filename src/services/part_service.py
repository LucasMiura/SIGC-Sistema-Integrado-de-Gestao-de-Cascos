from src.models.part import Part
from src.repositories.part_repository import PartRepository


class PartService:
    """Regras de negócio relacionadas a peças."""

    def __init__(
        self,
        repository: PartRepository,
    ):
        self.repository = repository

    def get_by_id(
        self,
        part_id: int,
    ) -> Part | None:
        return self.repository.get_by_id(part_id)

    def list_all(self) -> list[Part]:
        return self.repository.list_all()

    def create(
        self,
        part_code: str,
        name: str,
        description: str | None = None,
    ) -> Part:
        normalized_code = part_code.strip()
        normalized_name = name.strip()

        if not normalized_code:
            raise ValueError(
                "O código da peça é obrigatório."
            )

        if not normalized_name:
            raise ValueError(
                "O nome da peça é obrigatório."
            )

        existing_part = self.repository.get_by_code(
            normalized_code
        )

        if existing_part is not None:
            raise ValueError(
                "Já existe uma peça com este código."
            )

        part = Part(
            part_code=normalized_code,
            name=normalized_name,
            description=description,
            is_active=1,
        )

        return self.repository.add(part)

    def deactivate(
        self,
        part_id: int,
    ) -> Part:
        part = self.repository.get_by_id(part_id)

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if not part.is_active:
            raise ValueError(
                "A peça já está inativa."
            )

        part.is_active = 0

        return self.repository.save(part)

    def activate(
        self,
        part_id: int,
    ) -> Part:
        part = self.repository.get_by_id(part_id)

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if part.is_active:
            raise ValueError(
                "A peça já está ativa."
            )

        part.is_active = 1

        return self.repository.save(part)