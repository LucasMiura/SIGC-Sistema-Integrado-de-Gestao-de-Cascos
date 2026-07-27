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
from src.services.customer_return_service import (
    CustomerReturnService,
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

        customer_return_repository = (
            CustomerReturnRepository(session)
        )
        customer_return_item_repository = (
            CustomerReturnItemRepository(session)
        )
        customer_return_allocation_repository = (
            CustomerReturnAllocationRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor de Teste Devolucao",
                document="00.000.000/0001-02",
                address="Endereco de Teste",
                notes=(
                    "Registro criado para teste "
                    "de devolucao de cliente."
                ),
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
            part_code=(
                f"TEST-RETURN-{test_suffix}"
            ),
            name="Peca de Teste Devolucao",
            description=(
                "Peca criada exclusivamente para "
                "teste de devolucao de cliente."
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
                    f"NF-RETURN-001-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-24",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Primeira compra criada para "
                    "teste de devolucao."
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
                    f"NF-RETURN-002-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-25",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Segunda compra criada para "
                    "teste de devolucao."
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
                f"OS-RETURN-{test_suffix}"
            ),
            created_by=1,
            status="COMPLETED",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part_entity.id,
            quantity=8,
        )

        outbound_allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(
                outbound_item.id
            )
        )

        customer_return_service = (
            CustomerReturnService(
                customer_return_repository=(
                    customer_return_repository
                ),
                customer_return_item_repository=(
                    customer_return_item_repository
                ),
                customer_return_allocation_repository=(
                    customer_return_allocation_repository
                ),
                outbound_item_repository=(
                    outbound_item_repository
                ),
                part_repository=part_repository,
            )
        )

        customer_return = (
            customer_return_service
            .create_customer_return(
                return_type="CUSTOMER",
                reference_number=(
                    f"DEV-RETURN-{test_suffix}"
                ),
                customer_name=(
                    "Cliente de Teste"
                ),
                created_by=1,
                status="COMPLETED",
                notes=(
                    "Devolucao criada para teste "
                    "de rastreabilidade."
                ),
            )
        )

        customer_return_item = (
            customer_return_service.add_item(
                customer_return_id=(
                    customer_return.id
                ),
                part_id=part_entity.id,
                quantity=6,
            )
        )

        return_allocations = (
            customer_return_allocation_repository
            .list_by_return_item(
                customer_return_item.id
            )
        )

        session.commit()

        print(
            "Devolucao de cliente criada "
            "com sucesso!"
        )

        print(
            f"ID da devolucao: "
            f"{customer_return.id}"
        )

        print(
            f"ID do item devolvido: "
            f"{customer_return_item.id}"
        )

        print(
            f"Quantidade devolvida: "
            f"{customer_return_item.quantity}"
        )

        print()
        print(
            "Alocacoes da saida:"
        )

        for allocation in outbound_allocations:
            print(
                f"- PurchaseItem "
                f"{allocation.purchase_item_id}: "
                f"{allocation.quantity_allocated} "
                "unidade(s)"
            )

        print()
        print(
            "Alocacoes da devolucao:"
        )

        for allocation in return_allocations:
            print(
                f"- OutboundItem "
                f"{allocation.outbound_item_id}: "
                f"{allocation.quantity_allocated} "
                "unidade(s)"
            )

        print()
        print(
            "Resultado esperado:"
        )

        print(
            "- Saida de 8 unidades criada."
        )

        print(
            "- Devolucao de 6 unidades criada."
        )

        print(
            "- As 6 unidades foram vinculadas "
            "ao OutboundItem da saida."
        )

        print()
        print(
            "Quantidade disponivel das compras "
            "apos a saida:"
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