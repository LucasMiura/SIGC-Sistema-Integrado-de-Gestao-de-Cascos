from src.models.part import Part
from src.models.supplier import Supplier
from src.repositories.part_repository import PartRepository
from src.repositories.supplier_repository import SupplierRepository


FIELD_NOT_PROVIDED = object()


class PartService:
    """Regras de negócio relacionadas às peças."""

    def __init__(
        self,
        part_repository: PartRepository,
        supplier_repository: SupplierRepository,
    ):
        self.part_repository = part_repository
        self.supplier_repository = supplier_repository

    def get_by_id(
        self,
        part_id: int,
    ) -> Part | None:
        """Busca uma peça pelo identificador."""

        self._validate_positive_id(
            part_id,
            "O identificador da peça deve ser maior que zero.",
        )

        return self.part_repository.get_by_id(
            part_id
        )

    def get_required(
        self,
        part_id: int,
    ) -> Part:
        """Busca uma peça ou informa que ela não existe."""

        part = self.get_by_id(part_id)

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        return part

    def list_all(self) -> list[Part]:
        """Lista todas as peças."""

        return self.part_repository.list_all()

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Part]:
        """Lista as peças de um fornecedor existente."""

        self._get_required_supplier(
            supplier_id
        )

        return self.part_repository.list_by_supplier(
            supplier_id
        )

    def create(
        self,
        supplier_id: int,
        part_code: str,
        name: str,
        return_deadline_days: int,
        description: str | None = None,
    ) -> Part:
        """Cadastra uma nova peça."""

        supplier = self._get_required_supplier(
            supplier_id
        )

        self._ensure_supplier_is_active(
            supplier
        )

        normalized_part_code = (
            self._normalize_required_text(
                part_code,
                "O código original da peça é obrigatório.",
            )
        )

        normalized_name = (
            self._normalize_required_text(
                name,
                "O nome da peça é obrigatório.",
            )
        )

        normalized_description = (
            self._normalize_optional_text(
                description
            )
        )

        self._validate_return_deadline(
            return_deadline_days
        )

        existing_part = (
            self.part_repository
            .get_by_supplier_and_code(
                supplier_id,
                normalized_part_code,
            )
        )

        if existing_part is not None:
            raise ValueError(
                "Já existe uma peça com este código "
                "para o fornecedor informado."
            )

        part = Part(
            supplier_id=supplier_id,
            part_code=normalized_part_code,
            name=normalized_name,
            description=normalized_description,
            return_deadline_days=return_deadline_days,
            is_active=1,
        )

        return self.part_repository.add(part)

    def update(
        self,
        part_id: int,
        supplier_id: int | object = FIELD_NOT_PROVIDED,
        part_code: str | object = FIELD_NOT_PROVIDED,
        name: str | object = FIELD_NOT_PROVIDED,
        description: str | None | object = FIELD_NOT_PROVIDED,
        return_deadline_days: int | object = FIELD_NOT_PROVIDED,
    ) -> Part:
        """Atualiza parcialmente uma peça."""

        part = self.get_required(part_id)

        new_supplier_id = part.supplier_id
        new_part_code = part.part_code

        if supplier_id is not FIELD_NOT_PROVIDED:
            if not isinstance(supplier_id, int):
                raise ValueError(
                    "O fornecedor da peça é obrigatório."
                )

            supplier = self._get_required_supplier(
                supplier_id
            )

            self._ensure_supplier_is_active(
                supplier
            )

            new_supplier_id = supplier_id

        if part_code is not FIELD_NOT_PROVIDED:
            if not isinstance(part_code, str):
                raise ValueError(
                    "O código original da peça é obrigatório."
                )

            new_part_code = (
                self._normalize_required_text(
                    part_code,
                    "O código original da peça é obrigatório.",
                )
            )

        if (
            new_supplier_id != part.supplier_id
            or new_part_code != part.part_code
        ):
            existing_part = (
                self.part_repository
                .get_by_supplier_and_code(
                    new_supplier_id,
                    new_part_code,
                )
            )

            if (
                existing_part is not None
                and existing_part.id != part.id
            ):
                raise ValueError(
                    "Já existe uma peça com este código "
                    "para o fornecedor informado."
                )

        if name is not FIELD_NOT_PROVIDED:
            if not isinstance(name, str):
                raise ValueError(
                    "O nome da peça é obrigatório."
                )

            part.name = self._normalize_required_text(
                name,
                "O nome da peça é obrigatório.",
            )

        if description is not FIELD_NOT_PROVIDED:
            if description is not None and not isinstance(
                description,
                str,
            ):
                raise ValueError(
                    "A descrição da peça é inválida."
                )

            part.description = (
                self._normalize_optional_text(
                    description
                )
            )

        if (
            return_deadline_days
            is not FIELD_NOT_PROVIDED
        ):
            if not isinstance(
                return_deadline_days,
                int,
            ):
                raise ValueError(
                    "O prazo de devolução deve ser "
                    "informado em dias."
                )

            self._validate_return_deadline(
                return_deadline_days
            )

            part.return_deadline_days = (
                return_deadline_days
            )

        part.supplier_id = new_supplier_id
        part.part_code = new_part_code

        return self.part_repository.save(part)

    def activate(
        self,
        part_id: int,
    ) -> Part:
        """Ativa uma peça inativa."""

        part = self.get_required(part_id)

        if part.is_active:
            raise ValueError(
                "A peça já está ativa."
            )

        supplier = self._get_required_supplier(
            part.supplier_id
        )

        self._ensure_supplier_is_active(
            supplier
        )

        part.is_active = 1

        return self.part_repository.save(part)

    def deactivate(
        self,
        part_id: int,
    ) -> Part:
        """Desativa uma peça ativa."""

        part = self.get_required(part_id)

        if not part.is_active:
            raise ValueError(
                "A peça já está inativa."
            )

        part.is_active = 0

        return self.part_repository.save(part)

    def _get_required_supplier(
        self,
        supplier_id: int,
    ) -> Supplier:
        """Busca um fornecedor obrigatório."""

        self._validate_positive_id(
            supplier_id,
            (
                "O identificador do fornecedor "
                "deve ser maior que zero."
            ),
        )

        supplier = (
            self.supplier_repository.get_by_id(
                supplier_id
            )
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        return supplier

    @staticmethod
    def _ensure_supplier_is_active(
        supplier: Supplier,
    ) -> None:
        """Impede uso de fornecedor inativo."""

        if not supplier.is_active:
            raise ValueError(
                "O fornecedor informado está inativo."
            )

    @staticmethod
    def _validate_positive_id(
        value: int,
        message: str,
    ) -> None:
        """Valida identificadores positivos."""

        if not isinstance(value, int) or value <= 0:
            raise ValueError(message)

    @staticmethod
    def _validate_return_deadline(
        return_deadline_days: int,
    ) -> None:
        """Valida o prazo padrão da peça."""

        if (
            not isinstance(
                return_deadline_days,
                int,
            )
            or isinstance(
                return_deadline_days,
                bool,
            )
        ):
            raise ValueError(
                "O prazo de devolução deve ser "
                "informado em dias."
            )

        if return_deadline_days <= 0:
            raise ValueError(
                "O prazo de devolução deve ser "
                "maior que zero."
            )

        if return_deadline_days > 3650:
            raise ValueError(
                "O prazo de devolução não pode "
                "ser maior que 3650 dias."
            )

    @staticmethod
    def _normalize_required_text(
        value: str,
        empty_message: str,
    ) -> str:
        """Normaliza um texto obrigatório."""

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(empty_message)

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """Normaliza um texto opcional."""

        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None