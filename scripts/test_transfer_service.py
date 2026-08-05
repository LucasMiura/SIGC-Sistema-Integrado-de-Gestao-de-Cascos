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
from src.repositories.part_repository import (
    PartRepository,
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

        transfer_repository = TransferRepository(
            session
        )

        transfer_item_repository = (
            TransferItemRepository(
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

        suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        supplier = Supplier(
            name=(
                "Filial Fornecedora Teste "
                f"{suffix}"
            ),
            document=f"FILIAL-{suffix}",
            address=(
                "Endereço criado para o teste "
                "manual de transferência."
            ),
            notes=(
                "Cadastro temporário utilizado como "
                "referência da peça transferida."
            ),
            is_active=1,
        )

        supplier = supplier_repository.add(
            supplier
        )

        part = Part(
            supplier_id=supplier.id,
            part_code=(
                f"TEST-TRANSFER-{suffix}"
            ),
            name="Peça Teste Transferência",
            description=(
                "Peça criada exclusivamente para "
                "validar o módulo de transferências."
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
                f"NF-TRANSFER-{suffix}"
            ),
            issue_date="2026-08-05",
            created_by=1,
            status="ACTIVE",
        )

        assert transfer.origin_branch_id == 2
        assert transfer.destination_branch_id == 1

        assert transfer.invoice_number == (
            f"NF-TRANSFER-{suffix}"
        )

        assert transfer.status == "ACTIVE"

        transfer_item = transfer_service.add_item(
            transfer_id=transfer.id,
            part_id=part.id,
            quantity=10,
            return_deadline_days=45,
        )

        assert transfer_item.transfer_id == (
            transfer.id
        )

        assert transfer_item.part_id == part.id
        assert transfer_item.quantity == 10

        assert (
            transfer_item.quantity_available
            == 10
        )

        assert (
            transfer_item.return_deadline_days
            == 45
        )

        initial_available_quantity = (
            transfer_service.get_available_quantity(
                transfer_item.id
            )
        )

        assert initial_available_quantity == 10

        reduced_item = (
            transfer_service.reduce_available_quantity(
                transfer_item_id=transfer_item.id,
                quantity=4,
            )
        )

        assert reduced_item.quantity_available == 6

        reduced_available_quantity = (
            transfer_service.get_available_quantity(
                transfer_item.id
            )
        )

        assert reduced_available_quantity == 6

        try:
            transfer_service.reduce_available_quantity(
                transfer_item_id=transfer_item.id,
                quantity=7,
            )
        except ValueError as error:
            assert str(error) == (
                "A quantidade informada é superior "
                "ao saldo disponível do item de "
                "transferência."
            )

            print()
            print(
                "Bloqueio de saldo insuficiente "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu reduzir uma "
                "quantidade superior ao saldo."
            )

        try:
            transfer_service.add_item(
                transfer_id=transfer.id,
                part_id=part.id,
                quantity=1,
                return_deadline_days=45,
            )
        except ValueError as error:
            assert str(error) == (
                "Esta peça já foi adicionada "
                "à transferência."
            )

            print()
            print(
                "Bloqueio de item duplicado "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu adicionar a mesma "
                "peça duas vezes à transferência."
            )

        try:
            transfer_service.cancel_transfer(
                transfer.id
            )
        except ValueError as error:
            assert str(error) == (
                "Não é possível cancelar uma "
                "transferência que possui movimentações."
            )

            print()
            print(
                "Bloqueio de cancelamento com "
                "movimentação realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu cancelar uma "
                "transferência com movimentação."
            )

        restored_item = (
            transfer_service.restore_available_quantity(
                transfer_item_id=transfer_item.id,
                quantity=4,
            )
        )

        assert restored_item.quantity_available == 10

        restored_available_quantity = (
            transfer_service.get_available_quantity(
                transfer_item.id
            )
        )

        assert restored_available_quantity == 10

        try:
            transfer_service.restore_available_quantity(
                transfer_item_id=transfer_item.id,
                quantity=1,
            )
        except ValueError as error:
            assert str(error) == (
                "A quantidade restaurada não pode "
                "ultrapassar a quantidade originalmente "
                "recebida."
            )

            print()
            print(
                "Bloqueio de restauração excessiva "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu restaurar saldo "
                "acima da quantidade recebida."
            )

        cancelled_transfer = (
            transfer_service.cancel_transfer(
                transfer.id
            )
        )

        assert cancelled_transfer.status == (
            "CANCELLED"
        )

        try:
            transfer_service.cancel_transfer(
                transfer.id
            )
        except ValueError as error:
            assert str(error) == (
                "A transferência já está cancelada."
            )

            print()
            print(
                "Bloqueio de cancelamento duplicado "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu cancelar novamente "
                "uma transferência cancelada."
            )

        try:
            transfer_service.create_transfer(
                origin_branch_id=2,
                destination_branch_id=1,
                invoice_number=(
                    f"NF-TRANSFER-{suffix}"
                ),
                issue_date="2026-08-05",
                created_by=1,
            )
        except ValueError as error:
            assert str(error) == (
                "Já existe uma transferência cadastrada "
                "com esse número de Nota Fiscal."
            )

            print()
            print(
                "Bloqueio de Nota Fiscal duplicada "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu cadastrar duas "
                "transferências com a mesma NF."
            )

        try:
            transfer_service.create_transfer(
                origin_branch_id=1,
                destination_branch_id=1,
                invoice_number=(
                    f"NF-SAME-BRANCH-{suffix}"
                ),
                issue_date="2026-08-05",
                created_by=1,
            )
        except ValueError as error:
            assert str(error) == (
                "A filial de origem deve ser diferente "
                "da filial de destino."
            )

            print()
            print(
                "Bloqueio de filiais iguais "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu transferência "
                "entre a mesma filial."
            )

        listed_transfers = (
            transfer_service.list_transfers()
        )

        listed_items = transfer_service.list_items(
            transfer.id
        )

        assert any(
            listed_transfer.id == transfer.id
            for listed_transfer in listed_transfers
        )

        assert len(listed_items) == 1
        assert listed_items[0].id == transfer_item.id

        print()
        print(
            "Teste manual de transferência "
            "concluído com sucesso!"
        )

        print()
        print("Transferência:")
        print(f"- ID: {transfer.id}")
        print(
            "- Filial de origem: "
            f"{transfer.origin_branch_id}"
        )
        print(
            "- Filial de destino: "
            f"{transfer.destination_branch_id}"
        )
        print(
            "- Nota Fiscal: "
            f"{transfer.invoice_number}"
        )
        print(
            f"- Status final: {transfer.status}"
        )

        print()
        print("Item transferido:")
        print(f"- ID: {transfer_item.id}")
        print(f"- Peça: {part.part_code}")
        print("- Quantidade recebida: 10")
        print(
            "- Quantidade disponível inicial: "
            f"{initial_available_quantity}"
        )
        print(
            "- Quantidade após movimentação: "
            f"{reduced_available_quantity}"
        )
        print(
            "- Quantidade após restauração: "
            f"{restored_available_quantity}"
        )
        print("- Prazo específico: 45 dias")

        print()
        print("Validações confirmadas:")
        print(
            "- A transferência criou estoque "
            "próprio para a peça."
        )
        print(
            "- A movimentação reduziu o saldo."
        )
        print(
            "- A restauração recuperou o saldo."
        )
        print(
            "- Quantidades acima do saldo foram "
            "bloqueadas."
        )
        print(
            "- Itens duplicados foram bloqueados."
        )
        print(
            "- O cancelamento com movimentação "
            "foi bloqueado."
        )
        print(
            "- O cancelamento sem movimentação "
            "foi permitido."
        )
        print(
            "- Notas Fiscais duplicadas foram "
            "bloqueadas."
        )
        print(
            "- Transferências entre a mesma filial "
            "foram bloqueadas."
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.rollback()
        session.close()


if __name__ == "__main__":
    main()