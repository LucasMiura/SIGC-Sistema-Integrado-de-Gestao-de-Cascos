import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from datetime import datetime

from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.supplier import Supplier
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
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
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService
from src.services.supplier_return_service import (
    SupplierReturnService,
)


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)

        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = PurchaseItemRepository(session)

        outbound_repository = OutboundRepository(session)
        outbound_item_repository = OutboundItemRepository(session)
        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(session)
        )

        customer_return_repository = CustomerReturnRepository(session)
        customer_return_item_repository = (
            CustomerReturnItemRepository(session)
        )
        customer_return_allocation_repository = (
            CustomerReturnAllocationRepository(session)
        )

        supplier_return_repository = (
            SupplierReturnRepository(session)
        )
        supplier_return_item_repository = (
            SupplierReturnItemRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier = Supplier(
                name="Fornecedor Teste FIFO",
                document="00.000.000/0001-04",
                address="Endereco de Teste",
                notes="Fornecedor criado para teste FIFO.",
                is_active=1,
            )

            supplier = supplier_repository.add(supplier)

        else:
            supplier = suppliers[0]

        suffix = datetime.now().strftime("%Y%m%d%H%M%S%f")

        part = Part(
            supplier_id=supplier.id,
            part_code=f"TEST-SR-FIFO-{suffix}",
            name="Peca Teste FIFO Remessa",
            description="Peca criada para teste FIFO de remessa.",
            return_deadline_days=90,
            is_active=1,
        )

        part = part_repository.add(part)

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=purchase_item_repository,
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        outbound_service = OutboundService(
            outbound_repository=outbound_repository,
            outbound_item_repository=outbound_item_repository,
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=purchase_item_repository,
            part_repository=part_repository,
        )

        customer_return_service = CustomerReturnService(
            customer_return_repository=(
                customer_return_repository
            ),
            customer_return_item_repository=(
                customer_return_item_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
            outbound_repository=outbound_repository,
            outbound_item_repository=(
                outbound_item_repository
            ),
            part_repository=part_repository,
        )

        supplier_return_service = SupplierReturnService(
            supplier_return_repository=supplier_return_repository,
            supplier_return_item_repository=(
                supplier_return_item_repository
            ),
            supplier_repository=supplier_repository,
            purchase_repository=purchase_repository,
            purchase_item_repository=purchase_item_repository,
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
        )

        purchase_a = purchase_service.create_purchase(
            supplier_id=supplier.id,
            invoice_number=f"NF-FIFO-A-{suffix}",
            invoice_series="1",
            issue_date="2026-07-27",
            created_by=1,
            status="RECEIVED",
            notes="Primeira compra do teste FIFO.",
        )

        purchase_item_a = purchase_service.add_item(
            purchase_id=purchase_a.id,
            part_id=part.id,
            quantity_purchased=5,
        )

        purchase_b = purchase_service.create_purchase(
            supplier_id=supplier.id,
            invoice_number=f"NF-FIFO-B-{suffix}",
            invoice_series="1",
            issue_date="2026-07-28",
            created_by=1,
            status="RECEIVED",
            notes="Segunda compra do teste FIFO.",
        )

        purchase_item_b = purchase_service.add_item(
            purchase_id=purchase_b.id,
            part_id=part.id,
            quantity_purchased=5,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number=f"OS-FIFO-{suffix}",
            created_by=1,
            status="ACTIVE",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part.id,
            quantity=8,
        )

        customer_return = (
            customer_return_service.create_customer_return(
                return_type="WORK_ORDER",
                reference_number=f"OS-FIFO-{suffix}",
                customer_name="Cliente Teste FIFO",
                created_by=1,
                status="ACTIVE",
                notes="Devolucao criada para teste FIFO.",
            )
        )

        customer_return_service.add_item(
            customer_return_id=customer_return.id,
            part_id=part.id,
            quantity=6,
        )

        available_a = (
            supplier_return_service.get_available_quantity(
                purchase_item_a.id
            )
        )

        available_b = (
            supplier_return_service.get_available_quantity(
                purchase_item_b.id
            )
        )

        assert available_a == 5, (
            "A primeira origem deveria possuir 5 unidades "
            f"disponiveis, mas possui {available_a}."
        )

        assert available_b == 1, (
            "A segunda origem deveria possuir 1 unidade "
            f"disponivel, mas possui {available_b}."
        )

        outbound_allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(outbound_item.id)
        )

        session.commit()

        print("\nTeste FIFO de remessa concluido com sucesso!")

        print("\nCompras:")
        print(
            f"- PurchaseItem {purchase_item_a.id}: "
            "5 unidades compradas"
        )
        print(
            f"- PurchaseItem {purchase_item_b.id}: "
            "5 unidades compradas"
        )

        print("\nAlocacoes FIFO da saida:")

        for allocation in outbound_allocations:
            print(
                f"- PurchaseItem "
                f"{allocation.purchase_item_id}: "
                f"{allocation.quantity_allocated} unidade(s)"
            )

        print("\nDevolucao do cliente:")
        print("- Quantidade devolvida: 6")

        print("\nDisponivel para remessa:")
        print(
            f"- PurchaseItem {purchase_item_a.id}: "
            f"{available_a} unidade(s)"
        )
        print(
            f"- PurchaseItem {purchase_item_b.id}: "
            f"{available_b} unidade(s)"
        )

        print("\nResultado esperado:")
        print("- A saida consumiu 5 unidades da primeira compra.")
        print("- A saida consumiu 3 unidades da segunda compra.")
        print("- A devolucao de 6 unidades foi distribuida em FIFO.")
        print("- Primeira compra: 5 unidades disponiveis.")
        print("- Segunda compra: 1 unidade disponivel.")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()