from sqlalchemy import inspect

from src.database.connection import engine


def main() -> None:
    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print("Tabelas encontradas:")
    for table in tables:
        print(f"- {table}")

    tables_to_check = [
        "roles",
        "users",
        "parts",
        "suppliers",
        "supplier_contacts",
    ]

    for table in tables_to_check:
        print(f"\nColunas de {table}:")
        for column in inspector.get_columns(table):
            print(f"- {column['name']}")

    print("\nChaves estrangeiras:")
    for table in tables_to_check:
        foreign_keys = inspector.get_foreign_keys(table)

        for foreign_key in foreign_keys:
            print(
                f"- {table}.{foreign_key['constrained_columns']} "
                f"-> {foreign_key['referred_table']}."
                f"{foreign_key['referred_columns']}"
            )


if __name__ == "__main__":
    main()