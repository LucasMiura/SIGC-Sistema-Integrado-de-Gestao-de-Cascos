from __future__ import annotations

import argparse
from getpass import getpass
import sys

from sqlalchemy import select

from src.api.dependencies.authorization import (
    ROLE_ADMIN,
)
from src.database.connection import (
    SessionLocal,
)
from src.models.user import User
from src.repositories.audit_log_repository import (
    AuditLogRepository,
)
from src.repositories.role_repository import (
    RoleRepository,
)
from src.repositories.user_repository import (
    UserRepository,
)
from src.services.audit_service import (
    AuditService,
)
from src.services.user_service import (
    UserService,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Cria o primeiro Administrador "
            "Master do SIGC."
        )
    )

    parser.add_argument(
        "--full-name",
        required=True,
        help="Nome completo.",
    )

    parser.add_argument(
        "--username",
        required=True,
        help="Nome de usuário.",
    )

    parser.add_argument(
        "--email",
        required=True,
        help="E-mail.",
    )

    return parser


def main() -> int:
    args = (
        build_parser()
        .parse_args()
    )

    session = SessionLocal()

    try:
        role_repository = (
            RoleRepository(
                session
            )
        )

        admin_role = (
            role_repository
            .get_by_name(
                ROLE_ADMIN
            )
        )

        if admin_role is None:
            raise RuntimeError(
                "O perfil Administrador Master "
                "não existe. Execute primeiro "
                "as migrations do banco."
            )

        existing_admin = (
            session.scalar(
                select(User)
                .where(
                    User.role_id
                    == admin_role.id
                )
                .limit(1)
            )
        )

        if existing_admin is not None:
            raise RuntimeError(
                "Já existe um Administrador "
                "Master cadastrado."
            )

        password = getpass(
            "Senha do Administrador Master: "
        )

        password_confirmation = getpass(
            "Confirme a senha: "
        )

        if password != password_confirmation:
            raise ValueError(
                "As senhas informadas "
                "não coincidem."
            )

        user_repository = (
            UserRepository(
                session
            )
        )

        user_service = UserService(
            repository=user_repository,
            role_repository=(
                role_repository
            ),
        )

        user = user_service.create(
            full_name=args.full_name,
            username=args.username,
            email=args.email,
            password=password,
            role_id=admin_role.id,
        )

        audit_repository = (
            AuditLogRepository(
                session
            )
        )

        audit_service = AuditService(
            audit_repository
        )

        audit_service.register(
            user_id=user.id,
            action="BOOTSTRAP",
            module="USER",
            entity_type="User",
            entity_id=user.id,
            description=(
                "Administrador Master inicial "
                "criado durante a configuração "
                "do SIGC."
            ),
            new_values={
                "full_name": (
                    user.full_name
                ),
                "username": (
                    user.username
                ),
                "email": user.email,
                "role_id": (
                    user.role_id
                ),
                "is_active": (
                    user.is_active
                ),
            },
        )

        session.commit()

        print()
        print(
            "Administrador Master "
            "criado com sucesso."
        )

        print(
            f"ID: {user.id}"
        )

        print(
            f"Usuário: {user.username}"
        )

        return 0

    except Exception as error:
        session.rollback()

        print(
            "ERRO: não foi possível "
            "criar o Administrador Master.",
            file=sys.stderr,
        )

        print(
            str(error),
            file=sys.stderr,
        )

        return 1

    finally:
        session.close()


if __name__ == "__main__":
    raise SystemExit(
        main()
    )