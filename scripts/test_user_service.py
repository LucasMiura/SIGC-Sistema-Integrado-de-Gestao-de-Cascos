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
from src.repositories.role_repository import (
    RoleRepository,
)
from src.repositories.user_repository import (
    UserRepository,
)
from src.security.password import (
    verify_password,
)
from src.services.role_service import (
    RoleService,
)
from src.services.user_service import (
    UserService,
)


def main() -> None:
    session = SessionLocal()

    try:
        role_repository = RoleRepository(
            session
        )

        user_repository = UserRepository(
            session
        )

        role_service = RoleService(
            role_repository
        )

        user_service = UserService(
            repository=user_repository,
            role_repository=role_repository,
        )

        suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        role_name = (
            f"Perfil Teste Usuário {suffix}"
        )

        username = (
            f"usuario.teste.{suffix}"
        )

        email = (
            f"usuario.teste.{suffix}"
            "@example.com"
        )

        initial_password = (
            "SenhaInicial123"
        )

        changed_password = (
            "SenhaAlterada123"
        )

        reset_password = (
            "SenhaRedefinida123"
        )

        role = role_service.create(
            name=role_name,
            description=(
                "Perfil temporário criado para "
                "validar o módulo de usuários."
            ),
        )

        assert role.id is not None
        assert role.name == role_name

        user = user_service.create(
            full_name=(
                "Usuário Temporário de Teste"
            ),
            username=username,
            email=email,
            password=initial_password,
            role_id=role.id,
        )

        assert user.id is not None

        assert user.full_name == (
            "Usuário Temporário de Teste"
        )

        assert user.username == username
        assert user.email == email
        assert user.role_id == role.id
        assert user.is_active == 1

        assert (
            user.password_hash
            != initial_password
        ), (
            "A senha foi armazenada em texto puro."
        )

        assert verify_password(
            initial_password,
            user.password_hash,
        ), (
            "O hash armazenado não corresponde "
            "à senha inicial."
        )

        stored_initial_hash = (
            user.password_hash
        )

        found_by_id = (
            user_service.get_required(
                user.id
            )
        )

        found_by_username = (
            user_service.get_by_username(
                f" {username} "
            )
        )

        found_by_email = (
            user_service.get_by_email(
                f" {email.upper()} "
            )
        )

        assert found_by_id.id == user.id
        assert found_by_username.id == user.id
        assert found_by_email.id == user.id

        updated_user = user_service.update(
            user.id,
            full_name=(
                "Usuário Temporário Atualizado"
            ),
            username=(
                f"{username}.atualizado"
            ),
            email=(
                f"atualizado.{email}"
            ),
        )

        assert updated_user.full_name == (
            "Usuário Temporário Atualizado"
        )

        assert updated_user.username == (
            f"{username}.atualizado"
        )

        assert updated_user.email == (
            f"atualizado.{email}"
        )

        assert (
            updated_user.password_hash
            == stored_initial_hash
        ), (
            "A atualização cadastral alterou "
            "indevidamente a senha."
        )

        deactivated_user = (
            user_service.deactivate(
                user.id
            )
        )

        assert deactivated_user.is_active == 0

        try:
            user_service.deactivate(
                user.id
            )

        except ValueError as error:
            assert str(error) == (
                "O usuário já está inativo."
            )

            print()
            print(
                "Bloqueio de desativação duplicada "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu desativar "
                "novamente um usuário inativo."
            )

        activated_user = (
            user_service.activate(
                user.id
            )
        )

        assert activated_user.is_active == 1

        try:
            user_service.activate(
                user.id
            )

        except ValueError as error:
            assert str(error) == (
                "O usuário já está ativo."
            )

            print()
            print(
                "Bloqueio de ativação duplicada "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu ativar "
                "novamente um usuário ativo."
            )

        previous_hash = (
            activated_user.password_hash
        )

        changed_user = (
            user_service.change_password(
                user_id=user.id,
                current_password=(
                    initial_password
                ),
                new_password=(
                    changed_password
                ),
            )
        )

        assert (
            changed_user.password_hash
            != previous_hash
        )

        assert verify_password(
            changed_password,
            changed_user.password_hash,
        )

        assert not verify_password(
            initial_password,
            changed_user.password_hash,
        )

        try:
            user_service.change_password(
                user_id=user.id,
                current_password=(
                    initial_password
                ),
                new_password=(
                    "OutraSenha123"
                ),
            )

        except ValueError as error:
            assert str(error) == (
                "A senha atual está incorreta."
            )

            print()
            print(
                "Bloqueio de senha atual incorreta "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema aceitou uma senha atual "
                "incorreta."
            )

        hash_after_change = (
            changed_user.password_hash
        )

        reset_user = (
            user_service.reset_password(
                user_id=user.id,
                new_password=reset_password,
            )
        )

        assert (
            reset_user.password_hash
            != hash_after_change
        )

        assert verify_password(
            reset_password,
            reset_user.password_hash,
        )

        assert not verify_password(
            changed_password,
            reset_user.password_hash,
        )

        try:
            user_service.reset_password(
                user_id=user.id,
                new_password=reset_password,
            )

        except ValueError as error:
            assert str(error) == (
                "A nova senha deve ser diferente "
                "da senha atual."
            )

            print()
            print(
                "Bloqueio de reutilização da senha "
                "realizado com sucesso!"
            )
            print(f"Mensagem: {error}")

        else:
            raise AssertionError(
                "O sistema permitiu redefinir "
                "a mesma senha atual."
            )

        listed_users = (
            user_service.list_all()
        )

        assert any(
            listed_user.id == user.id
            for listed_user in listed_users
        )

        listed_roles = (
            role_service.list_all()
        )

        assert any(
            listed_role.id == role.id
            for listed_role in listed_roles
        )

        print()
        print(
            "Teste do módulo de usuários "
            "concluído com sucesso!"
        )

        print()
        print("Perfil:")
        print(f"- ID: {role.id}")
        print(f"- Nome: {role.name}")

        print()
        print("Usuário:")
        print(f"- ID: {user.id}")
        print(
            "- Nome: "
            f"{updated_user.full_name}"
        )
        print(
            "- Username: "
            f"{updated_user.username}"
        )
        print(
            "- E-mail: "
            f"{updated_user.email}"
        )
        print(
            "- Perfil: "
            f"{updated_user.role_id}"
        )
        print(
            "- Status final: "
            f"{updated_user.is_active}"
        )

        print()
        print("Segurança:")
        print(
            "- A senha inicial não foi "
            "armazenada em texto puro."
        )
        print(
            "- A senha inicial foi validada "
            "contra o hash."
        )
        print(
            "- A alteração cadastral não "
            "alterou a senha."
        )
        print(
            "- A senha atual incorreta foi "
            "bloqueada."
        )
        print(
            "- A alteração da própria senha "
            "foi concluída."
        )
        print(
            "- A redefinição administrativa "
            "foi concluída."
        )
        print(
            "- A reutilização da senha atual "
            "foi bloqueada."
        )

        print()
        print("Status:")
        print(
            "- A desativação foi concluída."
        )
        print(
            "- A desativação duplicada foi "
            "bloqueada."
        )
        print(
            "- A reativação foi concluída."
        )
        print(
            "- A ativação duplicada foi "
            "bloqueada."
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.rollback()
        session.close()


if __name__ == "__main__":
    main()