from src.database.connection import SessionLocal
from src.queries.purchase_tracking_query import PurchaseTrackingQuery
from src.repositories.purchase_repository import PurchaseRepository
from src.services.purchase_tracking_service import PurchaseTrackingService


def main() -> None:
    session = SessionLocal()

    try:
        purchases = PurchaseRepository(session).list_all()

        if not purchases:
            print(
                "Nenhuma compra cadastrada. Execute primeiro "
                "scripts/test_purchase_service.py."
            )
            return

        query = PurchaseTrackingQuery(session)
        service = PurchaseTrackingService(query)

        tracking = service.get_purchase_tracking(
            purchases[0].id
        )

        print("Acompanhamento da compra")
        print(f"Compra: {tracking.purchase_id}")
        print(
            "Nota Fiscal: "
            f"{tracking.invoice_number}"
            f"/{tracking.invoice_series or '-'}"
        )
        print(f"Fornecedor: {tracking.supplier_name}")
        print(f"Data de emissão: {tracking.issue_date}")
        print(f"Status da compra: {tracking.purchase_status}")

        for item in tracking.items:
            assert item.quantity_outbound >= 0
            assert item.quantity_returned_by_customer >= 0
            assert item.quantity_returned_to_supplier >= 0
            assert (
                item.quantity_returned_by_customer
                <= item.quantity_outbound
            )
            assert (
                item.quantity_returned_to_supplier
                <= item.quantity_returned_by_customer
            )

            print("-")
            print(
                f"Item {item.purchase_item_id}: "
                f"{item.part_code} - {item.part_name}"
            )
            print(f"Comprada: {item.quantity_purchased}")
            print(f"Saída: {item.quantity_outbound}")
            print(
                "Devolvida pelo cliente: "
                f"{item.quantity_returned_by_customer}"
            )
            print(
                "Pendente com cliente: "
                f"{item.quantity_pending_customer_return}"
            )
            print(
                "Disponível para fornecedor: "
                f"{item.quantity_available_for_supplier_return}"
            )
            print(
                "Remetida ao fornecedor: "
                f"{item.quantity_returned_to_supplier}"
            )
            print(
                "Pendente de encerramento: "
                f"{item.quantity_pending_supplier_return}"
            )
            print(f"Status: {item.lifecycle_status}")

        print("Teste concluído com sucesso.")

    finally:
        session.close()


if __name__ == "__main__":
    main()
