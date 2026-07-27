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

        supplier_return_repository = (
            SupplierReturnRepository(session)
        )
        supplier_return_item_repository = (
            SupplierReturnItemRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor Teste Remessa",
                document="00.000.000/0001-03",
                address="Endereco de Teste",
                notes=(
                    "Fornecedor criado para teste "
                    "de remessa de cascos."
                ),
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        test_suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        part_entity = Part(
            part_code=(
                f"TEST-SUPPLIER-RETURN-{test_suffix}"
            ),
            name="Peca Teste Remessa Fornecedor",
            description=(
                "Peca criada exclusivamente para teste "
                "de remessa ao fornecedor."
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
            outbound_item_repository=(
                outbound_item_repository
            ),
            part_repository=part_repository,
        )

        supplier_return_service = SupplierReturnService(
            supplier_return_repository=(
                supplier_return_repository
            ),
            supplier_return_item_repository=(
                supplier_return_item_repository
            ),
            supplier_repository=supplier_repository,
            purchase_repository=purchase_repository,
            purchase_item_repository=(
                purchase_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
        )

        purchase = purchase_service.create_purchase(
            supplier_id=supplier_entity.id,
            invoice_number=(
                f"NF-PURCHASE-SR-{test_suffix}"
            ),
            invoice_series="1",
            issue_date="2026-07-27",
            created_by=1,
            status="RECEIVED",
            notes=(
                "Compra criada para teste de "
                "remessa ao fornecedor."
            ),
        )

        purchase_item = purchase_service.add_item(
            purchase_id=purchase.id,
            part_id=part_entity.id,
            quantity_purchased=8,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORKSHOP",
            work_order_number=(
                f"OS-SR-{test_suffix}"
            ),
            created_by=1,
            status="ACTIVE",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part_entity.id,
            quantity=8,
        )

        customer_return = (
            customer_return_service.create_customer_return(
                return_type="WORKSHOP",
                reference_number=(
                    f"OS-SR-{test_suffix}"
                ),
                customer_name="Cliente Teste Remessa",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Devolucao criada para teste de "
                    "remessa ao fornecedor."
                ),
            )
        )

        customer_return_item = (
            customer_return_service.add_item(
                customer_return_id=customer_return.id,
                part_id=part_entity.id,
                quantity=6,
            )
        )

        available_before = (
            supplier_return_service.get_available_quantity(
                purchase_item.id
            )
        )

        assert available_before == 6, (
            "A quantidade disponível antes da remessa "
            f"deveria ser 6, mas foi {available_before}."
        )

        supplier_return = (
            supplier_return_service.create_supplier_return(
                supplier_id=supplier_entity.id,
                dispatch_invoice_number=(
                    f"NF-REMESSA-{test_suffix}"
                ),
                dispatch_invoice_series="1",
                issue_date="2026-07-27",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Remessa parcial criada pelo teste."
                ),
            )
        )

        supplier_return_item = (
            supplier_return_service.add_item(
                supplier_return_id=supplier_return.id,
                purchase_item_id=purchase_item.id,
                quantity=4,
            )
        )

        available_after = (
            supplier_return_service.get_available_quantity(
                purchase_item.id
            )
        )

        assert available_after == 2, (
            "A quantidade disponível após a remessa "
            f"deveria ser 2, mas foi {available_after}."
        )

        excess_blocked = False

        try:
            supplier_return_service.add_item(
                supplier_return_id=supplier_return.id,
                purchase_item_id=purchase_item.id,
                quantity=3,
            )

        except ValueError as error:
            excess_blocked = True

            print(
                "\nBloqueio de excesso realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        assert excess_blocked, (
            "O sistema deveria bloquear uma remessa "
            "superior ao saldo disponível."
        )

        session.commit()

        print(
            "\nRemessa ao fornecedor criada com sucesso!"
        )
        print(
            f"ID da compra: {purchase.id}"
        )
        print(
            f"ID do item da compra: {purchase_item.id}"
        )
        print(
            f"ID da saida: {outbound.id}"
        )
        print(
            f"ID do item da saida: {outbound_item.id}"
        )
        print(
            f"ID da devolucao do cliente: "
            f"{customer_return.id}"
        )
        print(
            f"ID do item devolvido: "
            f"{customer_return_item.id}"
        )
        print(
            f"ID da remessa: {supplier_return.id}"
        )
        print(
            f"ID do item da remessa: "
            f"{supplier_return_item.id}"
        )

        print(
            "\nQuantidades:"
        )
        print(
            "- Quantidade comprada: 8"
        )
        print(
            "- Quantidade retirada: 8"
        )
        print(
            "- Quantidade devolvida pelo cliente: 6"
        )
        print(
            "- Quantidade remetida ao fornecedor: 4"
        )
        print(
            f"- Saldo disponível para nova remessa: "
            f"{available_after}"
        )

        print(
            "\nResultado esperado:"
        )
        print(
            "- A quantidade inicial disponível para "
            "remessa era 6."
        )
        print(
            "- Foram remetidas 4 unidades."
        )
        print(
            "- Restaram 2 unidades disponíveis."
        )
        print(
            "- A tentativa de remeter 3 unidades "
            "foi bloqueada."
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()