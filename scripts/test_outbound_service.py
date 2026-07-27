from datetime import datetime

from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.supplier import Supplier
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)
        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = (
            PurchaseItemRepository(session)
        )

        outbound_repository = OutboundRepository(session)
        outbound_item_repository = (
            OutboundItemRepository(session)
        )
        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor de Teste FIFO",
                document="00.000.000/0001-01",
                address="Endereço de Teste",
                notes="Registro criado para teste FIFO.",
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        test_suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )

        part_entity = Part(
            part_code=f"TEST-FIFO-{test_suffix}",
            name="Peça de Teste FIFO",
            description=(
                "Peça criada exclusivamente para "
                "teste da regra FIFO."
            ),
            is_active=1,
        )

        part_entity = part_repository.add(
            part_entity
        )

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=(
                purchase_item_repository
            ),
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        first_purchase = (
            purchase_service.create_purchase(
                supplier_id=supplier_entity.id,
                invoice_number=(
                    f"NF-FIFO-001-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-24",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Primeira compra criada para "
                    "teste FIFO."
                ),
            )
        )

        first_purchase_item = (
            purchase_service.add_item(
                purchase_id=first_purchase.id,
                part_id=part_entity.id,
                quantity_purchased=5,
            )
        )

        second_purchase = (
            purchase_service.create_purchase(
                supplier_id=supplier_entity.id,
                invoice_number=(
                    f"NF-FIFO-002-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-25",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Segunda compra criada para "
                    "teste FIFO."
                ),
            )
        )

        second_purchase_item = (
            purchase_service.add_item(
                purchase_id=second_purchase.id,
                part_id=part_entity.id,
                quantity_purchased=10,
            )
        )

        outbound_service = OutboundService(
            outbound_repository=outbound_repository,
            outbound_item_repository=(
                outbound_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            part_repository=part_repository,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORKSHOP",
            work_order_number=(
                f"OS-FIFO-{test_suffix}"
            ),
            created_by=1,
            status="COMPLETED",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part_entity.id,
            quantity=8,
        )

        allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(
                outbound_item.id
            )
        )

        session.commit()

        print("Saída criada com sucesso!")
        print(
            f"ID da saída: {outbound.id}"
        )
        print(
            "ID do item de saída: "
            f"{outbound_item.id}"
        )
        print(
            "Quantidade retirada: "
            f"{outbound_item.quantity}"
        )

        print()
        print("Alocações FIFO:")

        for allocation in allocations:
            print(
                f"- PurchaseItem "
                f"{allocation.purchase_item_id}: "
                f"{allocation.quantity_allocated} "
                "unidade(s)"
            )

        print()
        print(
            "Quantidade disponível após a saída:"
        )

        print(
            f"- PurchaseItem "
            f"{first_purchase_item.id}: "
            f"{first_purchase_item.quantity_available}"
        )

        print(
            f"- PurchaseItem "
            f"{second_purchase_item.id}: "
            f"{second_purchase_item.quantity_available}"
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()