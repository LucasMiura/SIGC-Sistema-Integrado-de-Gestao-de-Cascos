from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.supplier import Supplier
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import PurchaseRepository
from src.repositories.supplier_repository import SupplierRepository
from src.services.purchase_service import PurchaseService


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)
        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = PurchaseItemRepository(session)

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor de Teste",
                document="00.000.000/0001-00",
                address="Endereço de Teste",
                notes="Registro criado para teste.",
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        parts = part_repository.list_all()

        if not parts:
            part_entity = Part(
                part_code="TEST-001",
                name="Peça de Teste",
                description="Registro criado para teste.",
                is_active=1,
            )

            part_entity = part_repository.add(
                part_entity
            )
        else:
            part_entity = parts[0]

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=purchase_item_repository,
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        purchase = purchase_service.create_purchase(
            supplier_id=supplier_entity.id,
            invoice_number="NF-TEST-001",
            invoice_series="1",
            issue_date="2026-07-24",
            created_by=1,
            status="RECEIVED",
            notes="Compra criada através de teste.",
        )

        purchase_item = purchase_service.add_item(
            purchase_id=purchase.id,
            part_id=part_entity.id,
            quantity_purchased=10,
        )

        session.commit()

        print("Compra criada com sucesso!")
        print(f"ID da compra: {purchase.id}")
        print(f"ID do item: {purchase_item.id}")
        print(
            "Quantidade comprada: "
            f"{purchase_item.quantity_purchased}"
        )
        print(
            "Quantidade disponível: "
            f"{purchase_item.quantity_available}"
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()