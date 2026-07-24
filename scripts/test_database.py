from sqlalchemy import inspect

from src.database.connection import engine


def main() -> None:
    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print("Tabelas encontradas:")
    for table in tables:
        print(f"- {table}")

    print("\nColunas de roles:")
    for column in inspector.get_columns("roles"):
        print(f"- {column['name']}")

    print("\nColunas de users:")
    for column in inspector.get_columns("users"):
        print(f"- {column['name']}")

    print("\nChaves estrangeiras de users:")
    for foreign_key in inspector.get_foreign_keys("users"):
        print(
            f"- {foreign_key['constrained_columns']} "
            f"-> {foreign_key['referred_table']}."
            f"{foreign_key['referred_columns']}"
        )


if __name__ == "__main__":
    main()