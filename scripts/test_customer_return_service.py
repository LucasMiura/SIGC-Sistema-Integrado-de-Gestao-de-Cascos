import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(
            session
        )

        part_repository = PartRepository(
            session
        )

        purchase_repository = PurchaseRepository(
            session
        )

        purchase_item_repository = (
            PurchaseItemRepository(
                session
            )
        )

        outbound_repository = OutboundRepository(
            session
        )

        outbound_item_repository = (
            OutboundItemRepository(
                session
            )
        )

        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(
                session
            )
        )

        customer_return_repository = (
            CustomerReturnRepository(
                session
            )
        )

        customer_return_item_repository = (
            CustomerReturnItemRepository(
                session
            )
        )

        customer_return_allocation_repository = (
            CustomerReturnAllocationRepository(
                session
            )
        )

        purchase_service = PurchaseService(
            purchase_repository=(
                purchase_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            supplier_repository=(
                supplier_repository
            ),
            part_repository=(
                part_repository
            ),
        )

        outbound_service = OutboundService(
            outbound_repository=(
                outbound_repository
            ),
            outbound_item_repository=(
                outbound_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            part_repository=(
                part_repository
            ),
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
            outbound_repository=(
                outbound_repository
            ),
            outbound_item_repository=(
                outbound_item_repository
            ),
            part_repository=(
                part_repository
            ),
        )

        test_suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        suppliers = supplier_repository.list_all()

        if suppliers:
            supplier = suppliers[0]
        else:
            supplier = Supplier(
                name=(
                    "Fornecedor Teste "
                    "Devolucao Cliente"
                ),
                document=(
                    f"TEST-{test_suffix}"
                ),
                address=(
                    "Endereco criado para teste."
                ),
                notes=(
                    "Fornecedor criado para o teste "
                    "manual de devolucao de cliente."
                ),
                is_active=1,
            )

            supplier = supplier_repository.add(
                supplier
            )

        part = Part(
            part_code=(
                f"TEST-CUSTOMER-RETURN-{test_suffix}"
            ),
            name=(
                "Peca Teste Devolucao Cliente"
            ),
            description=(
                "Peca criada exclusivamente para "
                "validar devolucoes vinculadas "
                "a saida original."
            ),
            supplier_id=supplier.id,
            return_deadline_days=90,
            is_active=1,
        )

        part = part_repository.add(
            part
        )

        purchase = purchase_service.create_purchase(
            supplier_id=supplier.id,
            invoice_number=(
                f"NFC-{test_suffix}"
            ),
            invoice_series="1",
            issue_date="2026-07-30",
            created_by=1,
            status="RECEIVED",
            notes=(
                "Compra criada para o teste manual "
                "de devolucao de cliente."
            ),
        )

        purchase_item = purchase_service.add_item(
            purchase_id=purchase.id,
            part_id=part.id,
            quantity_purchased=10,
        )

        first_outbound = (
            outbound_service.create_outbound(
                destination_type="WORK_ORDER",
                work_order_number=(
                    f"OS-A-{test_suffix}"
                ),
                created_by=1,
                status="ACTIVE",
            )
        )

        first_outbound_item = (
            outbound_service.add_item(
                outbound_id=first_outbound.id,
                part_id=part.id,
                quantity=5,
            )
        )

        second_outbound = (
            outbound_service.create_outbound(
                destination_type="WORK_ORDER",
                work_order_number=(
                    f"OS-B-{test_suffix}"
                ),
                created_by=1,
                status="ACTIVE",
            )
        )

        second_outbound_item = (
            outbound_service.add_item(
                outbound_id=second_outbound.id,
                part_id=part.id,
                quantity=5,
            )
        )

        customer_return = (
            customer_return_service
            .create_customer_return(
                return_type="WORK_ORDER",
                reference_number=(
                    second_outbound.work_order_number
                ),
                customer_name=(
                    "Cliente da segunda saida"
                ),
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Devolucao parcial vinculada "
                    "a segunda saida."
                ),
            )
        )

        customer_return_item = (
            customer_return_service.add_item(
                customer_return_id=(
                    customer_return.id
                ),
                part_id=part.id,
                quantity=3,
            )
        )

        return_allocations = (
            customer_return_allocation_repository
            .list_by_return_item(
                customer_return_item.id
            )
        )

        assert customer_return.return_type == (
            "WORK_ORDER"
        )

        assert customer_return.reference_number == (
            second_outbound.work_order_number
        )

        assert customer_return_item.quantity == 3

        assert len(return_allocations) == 1, (
            "A devolucao deveria possuir exatamente "
            "uma alocacao."
        )

        return_allocation = return_allocations[0]

        assert (
            return_allocation.outbound_item_id
            == second_outbound_item.id
        ), (
            "A devolucao foi vinculada a um item "
            "de saida incorreto."
        )

        assert (
            return_allocation.outbound_item_id
            != first_outbound_item.id
        ), (
            "A devolucao utilizou indevidamente "
            "a primeira saida."
        )

        assert (
            return_allocation.quantity_allocated
            == 3
        )

        try:
            customer_return_service.add_item(
                customer_return_id=(
                    customer_return.id
                ),
                part_id=part.id,
                quantity=3,
            )
        except ValueError as error:
            assert str(error) == (
                "A quantidade devolvida é superior "
                "à quantidade pendente da saída original."
            )
        else:
            raise AssertionError(
                "O sistema permitiu devolver uma "
                "quantidade superior ao saldo pendente."
            )

        customer_return_items = (
            customer_return_service
            .list_customer_return_items(
                customer_return.id
            )
        )

        assert len(customer_return_items) == 1, (
            "A tentativa inválida não deveria criar "
            "um novo item de devolucao."
        )

        assert purchase_item.quantity_available == 0

        print()
        print(
            "Teste de devolucao de cliente "
            "concluido com sucesso!"
        )

        print()
        print("Compra:")
        print(
            f"- PurchaseItem {purchase_item.id}: "
            "10 unidades"
        )

        print()
        print("Saidas com a mesma peca:")
        print(
            f"- Primeira saida "
            f"{first_outbound.work_order_number}: "
            "5 unidades"
        )
        print(
            f"- Segunda saida "
            f"{second_outbound.work_order_number}: "
            "5 unidades"
        )

        print()
        print("Devolucao:")
        print(
            "- Referencia utilizada: "
            f"{customer_return.reference_number}"
        )
        print("- Quantidade devolvida: 3 unidades")
        print(
            "- OutboundItem vinculado: "
            f"{return_allocation.outbound_item_id}"
        )

        print()
        print("Validacoes confirmadas:")
        print(
            "- A devolucao foi vinculada somente "
            "a segunda saida."
        )
        print(
            "- A primeira saida nao foi utilizada."
        )
        print(
            "- A devolucao parcial foi aceita."
        )
        print(
            "- A devolucao superior ao saldo "
            "pendente foi bloqueada."
        )
        print(
            "- A tentativa invalida nao criou "
            "um novo item."
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.rollback()
        session.close()


if __name__ == "__main__":
    main()