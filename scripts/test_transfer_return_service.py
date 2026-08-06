import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(PROJECT_ROOT),
    )

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
from src.repositories.outbound_transfer_allocation_repository import (
    OutboundTransferAllocationRepository,
)
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.repositories.transfer_return_item_repository import (
    TransferReturnItemRepository,
)
from src.repositories.transfer_return_repository import (
    TransferReturnRepository,
)
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.services.outbound_service import (
    OutboundService,
)
from src.services.transfer_return_service import (
    TransferReturnService,
)
from src.services.transfer_service import (
    TransferService,
)


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(
            session
        )

        part_repository = PartRepository(
            session
        )

        purchase_item_repository = (
            PurchaseItemRepository(
                session
            )
        )

        transfer_repository = TransferRepository(
            session
        )

        transfer_item_repository = (
            TransferItemRepository(
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

        outbound_transfer_allocation_repository = (
            OutboundTransferAllocationRepository(
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

        transfer_return_repository = (
            TransferReturnRepository(
                session
            )
        )

        transfer_return_item_repository = (
            TransferReturnItemRepository(
                session
            )
        )

        transfer_service = TransferService(
            transfer_repository=(
                transfer_repository
            ),
            transfer_item_repository=(
                transfer_item_repository
            ),
            part_repository=part_repository,
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
            outbound_transfer_allocation_repository=(
                outbound_transfer_allocation_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            transfer_item_repository=(
                transfer_item_repository
            ),
            part_repository=part_repository,
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
                outbound_repository=(
                    outbound_repository
                ),
                outbound_item_repository=(
                    outbound_item_repository
                ),
                part_repository=part_repository,
            )
        )

        transfer_return_service = (
            TransferReturnService(
                transfer_return_repository=(
                    transfer_return_repository
                ),
                transfer_return_item_repository=(
                    transfer_return_item_repository
                ),
                transfer_repository=(
                    transfer_repository
                ),
                transfer_item_repository=(
                    transfer_item_repository
                ),
                outbound_transfer_allocation_repository=(
                    outbound_transfer_allocation_repository
                ),
                customer_return_allocation_repository=(
                    customer_return_allocation_repository
                ),
            )
        )

        suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        supplier = Supplier(
            name=(
                "Filial Fornecedora Teste "
                f"{suffix}"
            ),
            document=(
                f"FILIAL-TRANSFER-RETURN-{suffix}"
            ),
            address=(
                "Endereço temporário utilizado no "
                "teste de devolução entre filiais."
            ),
            notes=(
                "Cadastro temporário criado pelo "
                "script de teste."
            ),
            is_active=1,
        )

        supplier = supplier_repository.add(
            supplier
        )

        part = Part(
            supplier_id=supplier.id,
            part_code=(
                f"TEST-TRANSFER-RETURN-{suffix}"
            ),
            name=(
                "Peça Teste Devolução entre Filiais"
            ),
            description=(
                "Peça criada exclusivamente para "
                "validar o ciclo de transferência, "
                "saída e devolução."
            ),
            return_deadline_days=90,
            is_active=1,
        )

        part = part_repository.add(
            part
        )

        transfer = transfer_service.create_transfer(
            origin_branch_id=2,
            destination_branch_id=1,
            invoice_number=(
                f"NF-TRANSFER-IN-{suffix}"
            ),
            issue_date="2026-08-05",
            created_by=1,
            status="ACTIVE",
        )

        transfer_item = transfer_service.add_item(
            transfer_id=transfer.id,
            part_id=part.id,
            quantity=8,
            return_deadline_days=45,
        )

        assert transfer_item.quantity == 8

        assert (
            transfer_item.quantity_available
            == 8
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number=(
                f"OS-TRANSFER-RETURN-{suffix}"
            ),
            created_by=1,
            status="ACTIVE",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part.id,
            quantity=8,
        )

        assert (
            transfer_item.quantity_available
            == 0
        )

        outbound_transfer_allocations = (
            outbound_transfer_allocation_repository
            .list_by_outbound_item(
                outbound_item.id
            )
        )

        assert len(
            outbound_transfer_allocations
        ) == 1

        outbound_transfer_allocation = (
            outbound_transfer_allocations[0]
        )

        assert (
            outbound_transfer_allocation
            .transfer_item_id
            == transfer_item.id
        )

        assert (
            outbound_transfer_allocation
            .quantity_allocated
            == 8
        )

        outbound_purchase_allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(
                outbound_item.id
            )
        )

        assert (
            outbound_purchase_allocations
            == []
        ), (
            "A saída deveria utilizar exclusivamente "
            "o estoque da transferência."
        )

        customer_return = (
            customer_return_service
            .create_customer_return(
                return_type="WORK_ORDER",
                reference_number=(
                    outbound.work_order_number
                ),
                customer_name=(
                    "Cliente Teste Transferência"
                ),
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Devolução parcial de cascos "
                    "originados de transferência."
                ),
            )
        )

        customer_return_item = (
            customer_return_service.add_item(
                customer_return_id=(
                    customer_return.id
                ),
                part_id=part.id,
                quantity=6,
            )
        )

        assert customer_return_item.quantity == 6

        customer_return_allocations = (
            customer_return_allocation_repository
            .list_by_return_item(
                customer_return_item.id
            )
        )

        assert len(
            customer_return_allocations
        ) == 1

        assert (
            customer_return_allocations[0]
            .outbound_item_id
            == outbound_item.id
        )

        assert (
            customer_return_allocations[0]
            .quantity_allocated
            == 6
        )

        available_before_return = (
            transfer_return_service
            .get_available_quantity(
                transfer_item.id
            )
        )

        assert available_before_return == 6, (
            "A quantidade disponível antes da "
            "devolução à filial deveria ser 6, "
            f"mas foi {available_before_return}."
        )

        transfer_return = (
            transfer_return_service
            .create_transfer_return(
                transfer_id=transfer.id,
                dispatch_invoice_number=(
                    f"NF-TRANSFER-RETURN-1-{suffix}"
                ),
                dispatch_invoice_series="1",
                issue_date="2026-08-05",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Primeira devolução parcial "
                    "para a filial de origem."
                ),
            )
        )

        transfer_return_item = (
            transfer_return_service.add_item(
                transfer_return_id=(
                    transfer_return.id
                ),
                transfer_item_id=(
                    transfer_item.id
                ),
                quantity=4,
            )
        )

        assert transfer_return_item.quantity == 4

        available_after_first_return = (
            transfer_return_service
            .get_available_quantity(
                transfer_item.id
            )
        )

        assert available_after_first_return == 2, (
            "A quantidade disponível após a primeira "
            "devolução deveria ser 2, "
            f"mas foi {available_after_first_return}."
        )

        try:
            transfer_return_service.add_item(
                transfer_return_id=(
                    transfer_return.id
                ),
                transfer_item_id=(
                    transfer_item.id
                ),
                quantity=1,
            )

        except ValueError as error:
            assert str(error) == (
                "Este item de transferência já foi "
                "adicionado à devolução."
            )

            print()
            print(
                "Bloqueio de item duplicado "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu adicionar o mesmo "
                "TransferItem duas vezes na devolução."
            )

        second_transfer_return = (
            transfer_return_service
            .create_transfer_return(
                transfer_id=transfer.id,
                dispatch_invoice_number=(
                    f"NF-TRANSFER-RETURN-2-{suffix}"
                ),
                dispatch_invoice_series="1",
                issue_date="2026-08-05",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Segunda devolução parcial "
                    "para a filial de origem."
                ),
            )
        )

        try:
            transfer_return_service.add_item(
                transfer_return_id=(
                    second_transfer_return.id
                ),
                transfer_item_id=(
                    transfer_item.id
                ),
                quantity=3,
            )

        except ValueError as error:
            assert str(error) == (
                "A quantidade devolvida é maior que a "
                "quantidade disponível para devolução "
                "à filial. Quantidade máxima permitida: "
                "2."
            )

            print()
            print(
                "Bloqueio de quantidade superior "
                "ao saldo realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu devolver uma "
                "quantidade superior ao saldo."
            )

        second_transfer_return_item = (
            transfer_return_service.add_item(
                transfer_return_id=(
                    second_transfer_return.id
                ),
                transfer_item_id=(
                    transfer_item.id
                ),
                quantity=2,
            )
        )

        assert (
            second_transfer_return_item.quantity
            == 2
        )

        final_available_quantity = (
            transfer_return_service
            .get_available_quantity(
                transfer_item.id
            )
        )

        assert final_available_quantity == 0

        third_transfer_return = (
            transfer_return_service
            .create_transfer_return(
                transfer_id=transfer.id,
                dispatch_invoice_number=(
                    f"NF-TRANSFER-RETURN-3-{suffix}"
                ),
                dispatch_invoice_series="1",
                issue_date="2026-08-05",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Remessa criada para validar "
                    "o bloqueio de saldo zerado."
                ),
            )
        )

        try:
            transfer_return_service.add_item(
                transfer_return_id=(
                    third_transfer_return.id
                ),
                transfer_item_id=(
                    transfer_item.id
                ),
                quantity=1,
            )

        except ValueError as error:
            assert str(error) == (
                "Não existe quantidade disponível para "
                "devolução à filial neste item de "
                "transferência."
            )

            print()
            print(
                "Bloqueio de saldo zerado "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu devolver um casco "
                "sem saldo disponível."
            )

        listed_returns = (
            transfer_return_service
            .list_by_transfer(
                transfer.id
            )
        )

        assert len(listed_returns) == 3

        first_return_items = (
            transfer_return_service.list_items(
                transfer_return.id
            )
        )

        second_return_items = (
            transfer_return_service.list_items(
                second_transfer_return.id
            )
        )

        assert len(first_return_items) == 1
        assert len(second_return_items) == 1

        print()
        print(
            "Teste de devolução entre filiais "
            "concluído com sucesso!"
        )

        print()
        print("Transferência recebida:")
        print(f"- ID: {transfer.id}")
        print(
            "- Nota Fiscal: "
            f"{transfer.invoice_number}"
        )
        print(
            "- Filial de origem: "
            f"{transfer.origin_branch_id}"
        )
        print(
            "- Filial de destino: "
            f"{transfer.destination_branch_id}"
        )

        print()
        print("Item recebido:")
        print(f"- TransferItem: {transfer_item.id}")
        print(f"- Peça: {part.part_code}")
        print("- Quantidade recebida: 8")
        print(
            "- Prazo específico: "
            f"{transfer_item.return_deadline_days} dias"
        )

        print()
        print("Saída:")
        print(f"- Outbound: {outbound.id}")
        print(f"- OutboundItem: {outbound_item.id}")
        print("- Quantidade retirada: 8")
        print(
            "- Origem utilizada: "
            f"TransferItem {transfer_item.id}"
        )

        print()
        print("Devolução do cliente:")
        print(
            f"- CustomerReturn: "
            f"{customer_return.id}"
        )
        print(
            f"- CustomerReturnItem: "
            f"{customer_return_item.id}"
        )
        print("- Quantidade devolvida: 6")

        print()
        print("Devoluções à filial de origem:")
        print(
            "- Primeira remessa: "
            f"{transfer_return_item.quantity}"
        )
        print(
            "- Segunda remessa: "
            f"{second_transfer_return_item.quantity}"
        )
        print(
            "- Total devolvido à filial: "
            f"{(
                transfer_return_item.quantity
                + second_transfer_return_item.quantity
            )}"
        )

        print()
        print("Saldos:")
        print(
            "- Disponível antes da primeira remessa: "
            f"{available_before_return}"
        )
        print(
            "- Disponível após a primeira remessa: "
            f"{available_after_first_return}"
        )
        print(
            "- Disponível após a segunda remessa: "
            f"{final_available_quantity}"
        )

        print()
        print("Validações confirmadas:")
        print(
            "- A saída utilizou o estoque da "
            "transferência."
        )
        print(
            "- A devolução do cliente preservou "
            "a origem transferida."
        )
        print(
            "- A devolução parcial à filial "
            "foi permitida."
        )
        print(
            "- O mesmo item não pôde ser repetido "
            "na mesma remessa."
        )
        print(
            "- Quantidades acima do saldo foram "
            "bloqueadas."
        )
        print(
            "- O saldo foi reduzido conforme as "
            "devoluções à filial."
        )
        print(
            "- O saldo final foi encerrado em zero."
        )
        print(
            "- A responsabilidade da filial atual "
            "foi encerrada."
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.rollback()
        session.close()


if __name__ == "__main__":
    main()