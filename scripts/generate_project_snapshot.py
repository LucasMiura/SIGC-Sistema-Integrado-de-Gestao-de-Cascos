from __future__ import annotations

import os
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIRECTORY = PROJECT_ROOT / "snapshots"

TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

OUTPUT_FILE = (
    OUTPUT_DIRECTORY
    / f"sigc_project_snapshot_{TIMESTAMP}.md"
)


IGNORED_DIRECTORIES = {
    ".git",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    ".vscode",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "node_modules",
    "snapshots",
}


IGNORED_FILES = {
    ".coverage",
    ".env",
    ".env.local",
    ".env.production",
    ".env.test",
    "coverage.xml",
}


IGNORED_SUFFIXES = {
    ".db",
    ".db-journal",
    ".exe",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".log",
    ".pdf",
    ".png",
    ".pyc",
    ".pyo",
    ".sqlite",
    ".sqlite3",
    ".svg",
    ".webp",
    ".zip",
}


ALLOWED_FILES_WITHOUT_SUFFIX = {
    "Dockerfile",
    "LICENSE",
    "Makefile",
    "Procfile",
}


ALLOWED_SUFFIXES = {
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".jsx",
    ".json",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}


MAX_FILE_SIZE_BYTES = 500_000


PREFERRED_DATABASE_PATHS = (
    PROJECT_ROOT
    / "data"
    / "sigc_dev.db",
    PROJECT_ROOT
    / "data"
    / "sigc_prod.db",
    PROJECT_ROOT
    / "sigc.db",
    PROJECT_ROOT
    / "database.db",
    PROJECT_ROOT
    / "app.db",
    PROJECT_ROOT
    / "sqlite.db",
    PROJECT_ROOT
    / "sigc.sqlite",
    PROJECT_ROOT
    / "database.sqlite",
    PROJECT_ROOT
    / "app.sqlite",
)


def should_ignore_path(path: Path) -> bool:
    """Verifica se um arquivo ou diretório deve ser ignorado."""

    relative_parts = path.relative_to(PROJECT_ROOT).parts

    if any(
        part in IGNORED_DIRECTORIES
        for part in relative_parts
    ):
        return True

    if path.name in IGNORED_FILES:
        return True

    if path.suffix.lower() in IGNORED_SUFFIXES:
        return True

    return False


def should_include_file(path: Path) -> bool:
    """Verifica se o arquivo deve aparecer no snapshot."""

    if not path.is_file():
        return False

    if should_ignore_path(path):
        return False

    if path.stat().st_size > MAX_FILE_SIZE_BYTES:
        return False

    if path.name in ALLOWED_FILES_WITHOUT_SUFFIX:
        return True

    return path.suffix.lower() in ALLOWED_SUFFIXES


def get_project_files() -> list[Path]:
    """Retorna os arquivos textuais relevantes do projeto."""

    files = [
        path
        for path in PROJECT_ROOT.rglob("*")
        if should_include_file(path)
    ]

    return sorted(
        files,
        key=lambda item: str(
            item.relative_to(PROJECT_ROOT)
        ).lower(),
    )


def build_directory_tree(files: Iterable[Path]) -> str:
    """Monta uma árvore simples dos arquivos incluídos."""

    lines: list[str] = []

    for path in files:
        relative_path = path.relative_to(PROJECT_ROOT)
        depth = len(relative_path.parts) - 1
        indentation = "    " * depth

        lines.append(
            f"{indentation}- {relative_path.name}"
        )

    return "\n".join(lines)


def read_text_file(path: Path) -> str:
    """Lê um arquivo textual usando codificações comuns."""

    encodings = (
        "utf-8",
        "utf-8-sig",
        "latin-1",
    )

    for encoding in encodings:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue

    return (
        "[Arquivo não pôde ser decodificado "
        "como texto.]"
    )


def detect_language(path: Path) -> str:
    """Retorna a linguagem para o bloco Markdown."""

    language_by_suffix = {
        ".cfg": "ini",
        ".css": "css",
        ".csv": "csv",
        ".html": "html",
        ".ini": "ini",
        ".js": "javascript",
        ".json": "json",
        ".md": "markdown",
        ".ps1": "powershell",
        ".py": "python",
        ".sql": "sql",
        ".toml": "toml",
        ".txt": "text",
        ".yaml": "yaml",
        ".yml": "yaml",
    }

    if path.name == "Dockerfile":
        return "dockerfile"

    if path.name == "Makefile":
        return "makefile"

    return language_by_suffix.get(
        path.suffix.lower(),
        "text",
    )


def run_command(command: list[str]) -> str:
    """Executa um comando e retorna sua saída."""

    try:
        result = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError:
        return (
            f"Comando não encontrado: "
            f"{' '.join(command)}"
        )
    except Exception as error:
        return (
            "Erro ao executar o comando "
            f"{' '.join(command)}: {error}"
        )

    output_parts: list[str] = []

    if result.stdout.strip():
        output_parts.append(result.stdout.strip())

    if result.stderr.strip():
        output_parts.append(
            "STDERR:\n"
            f"{result.stderr.strip()}"
        )

    if not output_parts:
        output_parts.append(
            f"Comando finalizado com código "
            f"{result.returncode}, sem saída."
        )

    return "\n\n".join(output_parts)


def find_sqlite_database() -> Path | None:
    """
    Procura um banco SQLite do projeto.

    A busca não inclui ambientes virtuais, snapshots,
    caches ou diretórios ignorados.
    """

    for candidate in PREFERRED_DATABASE_PATHS:
        if (
            candidate.exists()
            and candidate.is_file()
        ):
            return candidate

    candidates: list[Path] = []

    for suffix in ("*.db", "*.sqlite", "*.sqlite3"):
        for path in PROJECT_ROOT.rglob(suffix):
            if should_ignore_path(path):
                continue

            if path.is_file():
                candidates.append(path)

    if not candidates:
        return None

    return sorted(
        candidates,
        key=lambda item: str(item).lower(),
    )[0]


def quote_sqlite_identifier(identifier: str) -> str:
    """Escapa identificadores usados em consultas SQLite."""

    return '"' + identifier.replace('"', '""') + '"'


def get_database_snapshot(
    database_path: Path,
) -> str:
    """
    Coleta somente metadados e contagens do SQLite.

    Os registros completos não são exportados.
    """

    lines: list[str] = []

    relative_database_path = database_path.relative_to(
        PROJECT_ROOT
    )

    lines.append(
        f"Banco detectado: `{relative_database_path}`"
    )
    lines.append("")

    try:
        connection = sqlite3.connect(database_path)
        connection.row_factory = sqlite3.Row
    except sqlite3.Error as error:
        return (
            "Não foi possível abrir o banco SQLite: "
            f"{error}"
        )

    try:
        cursor = connection.cursor()

        tables = cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name
            """
        ).fetchall()

        if not tables:
            lines.append(
                "Nenhuma tabela encontrada no banco."
            )
            return "\n".join(lines)

        for table_row in tables:
            table_name = str(table_row["name"])
            quoted_table = quote_sqlite_identifier(
                table_name
            )

            lines.append(f"## Tabela `{table_name}`")
            lines.append("")

            try:
                total = cursor.execute(
                    f"SELECT COUNT(*) FROM {quoted_table}"
                ).fetchone()[0]

                lines.append(
                    f"Quantidade de registros: `{total}`"
                )
                lines.append("")
            except sqlite3.Error as error:
                lines.append(
                    "Não foi possível contar os registros: "
                    f"`{error}`"
                )
                lines.append("")

            lines.append("### Colunas")
            lines.append("")
            lines.append(
                "```text"
            )

            columns = cursor.execute(
                f"PRAGMA table_info({quoted_table})"
            ).fetchall()

            for column in columns:
                lines.append(
                    " | ".join(
                        [
                            f"cid={column['cid']}",
                            f"name={column['name']}",
                            f"type={column['type']}",
                            f"notnull={column['notnull']}",
                            f"default={column['dflt_value']}",
                            f"pk={column['pk']}",
                        ]
                    )
                )

            lines.append("```")
            lines.append("")

            lines.append("### Índices")
            lines.append("")
            lines.append("```text")

            indexes = cursor.execute(
                f"PRAGMA index_list({quoted_table})"
            ).fetchall()

            if not indexes:
                lines.append("Nenhum índice encontrado.")
            else:
                for index in indexes:
                    lines.append(str(tuple(index)))

                    index_name = str(index["name"])
                    quoted_index = quote_sqlite_identifier(
                        index_name
                    )

                    index_columns = cursor.execute(
                        f"PRAGMA index_info({quoted_index})"
                    ).fetchall()

                    for index_column in index_columns:
                        lines.append(
                            "    "
                            f"{tuple(index_column)}"
                        )

            lines.append("```")
            lines.append("")

            lines.append("### Chaves estrangeiras")
            lines.append("")
            lines.append("```text")

            foreign_keys = cursor.execute(
                f"PRAGMA foreign_key_list({quoted_table})"
            ).fetchall()

            if not foreign_keys:
                lines.append(
                    "Nenhuma chave estrangeira encontrada."
                )
            else:
                for foreign_key in foreign_keys:
                    lines.append(str(tuple(foreign_key)))

            lines.append("```")
            lines.append("")

        if any(
            str(table["name"]) == "parts"
            for table in tables
        ):
            lines.append(
                "## Diagnóstico específico de `parts`"
            )
            lines.append("")

            duplicate_codes = cursor.execute(
                """
                SELECT
                    part_code,
                    COUNT(*) AS total
                FROM parts
                GROUP BY part_code
                HAVING COUNT(*) > 1
                ORDER BY part_code
                """
            ).fetchall()

            lines.append("### Códigos duplicados")
            lines.append("")
            lines.append("```text")

            if not duplicate_codes:
                lines.append(
                    "Nenhum part_code duplicado."
                )
            else:
                for row in duplicate_codes:
                    lines.append(
                        f"{row['part_code']} | "
                        f"total={row['total']}"
                    )

            lines.append("```")
            lines.append("")

            sample_parts = cursor.execute(
                """
                SELECT
                    id,
                    part_code,
                    name,
                    description,
                    is_active,
                    created_at,
                    updated_at
                FROM parts
                ORDER BY id
                LIMIT 30
                """
            ).fetchall()

            lines.append(
                "### Peças existentes"
            )
            lines.append("")
            lines.append(
                "A amostra abaixo ajuda a identificar "
                "a origem e o significado dos 26 registros."
            )
            lines.append("")
            lines.append("```text")

            if not sample_parts:
                lines.append(
                    "Nenhuma peça cadastrada."
                )
            else:
                for row in sample_parts:
                    lines.append(
                        " | ".join(
                            [
                                f"id={row['id']}",
                                f"part_code={row['part_code']}",
                                f"name={row['name']}",
                                (
                                    "description="
                                    f"{row['description']}"
                                ),
                                (
                                    "is_active="
                                    f"{row['is_active']}"
                                ),
                                (
                                    "created_at="
                                    f"{row['created_at']}"
                                ),
                                (
                                    "updated_at="
                                    f"{row['updated_at']}"
                                ),
                            ]
                        )
                    )

            lines.append("```")
            lines.append("")

    except sqlite3.Error as error:
        lines.append(
            "Erro durante a leitura do SQLite: "
            f"`{error}`"
        )
    finally:
        connection.close()

    return "\n".join(lines)


def generate_snapshot() -> Path:
    """Gera o snapshot completo em Markdown."""

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    project_files = get_project_files()

    sections: list[str] = [
        "# Snapshot do projeto SIGC",
        "",
        f"Gerado em: `{datetime.now().isoformat()}`",
        "",
        f"Diretório do projeto: `{PROJECT_ROOT}`",
        "",
        "## Avisos",
        "",
        "- O conteúdo de `.env` não foi incluído.",
        "- Bancos SQLite completos não foram incluídos.",
        "- Foram incluídos apenas metadados e amostras "
        "necessárias para análise.",
        "- `.venv`, `.git`, caches e arquivos binários "
        "foram ignorados.",
        "",
        "## Árvore de arquivos",
        "",
        "```text",
        build_directory_tree(project_files),
        "```",
        "",
        "## Estado do Git",
        "",
        "```text",
        run_command(
            ["git", "status", "--short", "--branch"]
        ),
        "```",
        "",
        "## Últimos commits",
        "",
        "```text",
        run_command(
            [
                "git",
                "log",
                "--oneline",
                "--decorate",
                "-15",
            ]
        ),
        "```",
        "",
        "## Alembic current",
        "",
        "```text",
        run_command(
            [
                os.fspath(
                    PROJECT_ROOT
                    / ".venv"
                    / "Scripts"
                    / "python.exe"
                ),
                "-m",
                "alembic",
                "current",
            ]
        ),
        "```",
        "",
        "## Alembic heads",
        "",
        "```text",
        run_command(
            [
                os.fspath(
                    PROJECT_ROOT
                    / ".venv"
                    / "Scripts"
                    / "python.exe"
                ),
                "-m",
                "alembic",
                "heads",
            ]
        ),
        "```",
        "",
        "## Alembic history",
        "",
        "```text",
        run_command(
            [
                os.fspath(
                    PROJECT_ROOT
                    / ".venv"
                    / "Scripts"
                    / "python.exe"
                ),
                "-m",
                "alembic",
                "history",
                "--verbose",
            ]
        ),
        "```",
        "",
    ]

    database_path = find_sqlite_database()

    sections.extend(
        [
            "# Banco de dados",
            "",
        ]
    )

    if database_path is None:
        sections.extend(
            [
                "Nenhum arquivo SQLite foi encontrado "
                "automaticamente.",
                "",
            ]
        )
    else:
        sections.extend(
            [
                get_database_snapshot(database_path),
                "",
            ]
        )

    sections.extend(
        [
            "# Conteúdo dos arquivos",
            "",
        ]
    )

    for path in project_files:
        relative_path = path.relative_to(PROJECT_ROOT)
        language = detect_language(path)
        content = read_text_file(path)

        sections.extend(
            [
                f"## `{relative_path}`",
                "",
                f"```{language}",
                content.rstrip(),
                "```",
                "",
            ]
        )

    OUTPUT_FILE.write_text(
        "\n".join(sections),
        encoding="utf-8",
    )

    return OUTPUT_FILE


def main() -> None:
    """Ponto de entrada do script."""

    try:
        snapshot_path = generate_snapshot()
    except Exception as error:
        print(
            "Não foi possível gerar o snapshot."
        )
        print(
            f"Erro: {type(error).__name__}: {error}"
        )
        raise SystemExit(1) from error

    print("Snapshot gerado com sucesso:")
    print(snapshot_path)


if __name__ == "__main__":
    main()