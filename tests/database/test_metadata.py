import src.models  # noqa: F401

from src.database.connection import Base


EXPECTED_TABLES = {
    "audit_logs",
    "core_movements",
    "customer_return_allocations",
    "customer_return_items",
    "customer_returns",
    "outbound_items",
    "outbound_purchase_allocations",
    "outbound_transfer_allocations",
    "outbounds",
    "parts",
    "purchase_items",
    "purchases",
    "roles",
    "supplier_contacts",
    "supplier_return_items",
    "supplier_returns",
    "suppliers",
    "transfer_items",
    "transfer_return_items",
    "transfer_returns",
    "transfers",
    "users",
}


def test_should_load_all_expected_tables_into_metadata() -> None:
    assert (
        EXPECTED_TABLES
        <= set(
            Base.metadata.tables
        )
    )