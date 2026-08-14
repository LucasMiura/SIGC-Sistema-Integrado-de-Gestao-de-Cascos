from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from src.api.dependencies.audit import (
    get_audit_service,
)

from src.api.routes.part_route import (
    get_part_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.part_service import PartService
from src.api.dependencies.auth import (
    get_current_user,
)
from src.services.audit_service import (
    AuditService,
)
from src.api.dependencies.authorization import (
    ROLE_BUYER,
)


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock do serviço de peças.
    """

    return Mock(spec=PartService)


@pytest.fixture
def session_mock() -> Mock:
    """
    Cria um mock da sessão SQLAlchemy.
    """

    session = Mock()

    session.commit.return_value = None
    session.rollback.return_value = None
    session.refresh.return_value = None

    return session

@pytest.fixture
def audit_service() -> Mock:
    """
    Cria um mock do serviço de auditoria.
    """

    return Mock(
        spec=AuditService,
    )

@pytest.fixture
def client(
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP simulando
    um Comprador autenticado.
    """

    buyer_user = SimpleNamespace(
        id=2,
        username="comprador",
        role_id=2,
        is_active=1,
    )

    buyer_role = SimpleNamespace(
        id=2,
        name=ROLE_BUYER,
    )

    def override_part_service() -> Mock:
        return service_mock

    def override_audit_service() -> Mock:
        return audit_service

    def override_session() -> Generator[
        Mock,
        None,
        None,
    ]:
        yield session_mock

    def override_get_current_user():
        return buyer_user

    session_mock.scalar.return_value = (
        buyer_role
    )

    app.dependency_overrides[
        get_part_service
    ] = override_part_service

    app.dependency_overrides[
        get_audit_service
    ] = override_audit_service

    app.dependency_overrides[
        get_session
    ] = override_session

    app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    with TestClient(
        app,
        raise_server_exceptions=False,
    ) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_part(
    *,
    part_id: int = 10,
    supplier_id: int = 1,
    part_code: str = "ABC123",
    name: str = "Compressor de ar",
    description: str | None = (
        "Compressor com obrigação de devolução de casco"
    ),
    return_deadline_days: int = 90,
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados pelo schema.
    """

    return SimpleNamespace(
        id=part_id,
        supplier_id=supplier_id,
        part_code=part_code,
        name=name,
        description=description,
        return_deadline_days=return_deadline_days,
        is_active=is_active,
        created_at="2026-07-28T10:00:00",
        updated_at="2026-07-28T10:00:00",
    )


def expected_part_json(
    *,
    part_id: int = 10,
    supplier_id: int = 1,
    part_code: str = "ABC123",
    name: str = "Compressor de ar",
    description: str | None = (
        "Compressor com obrigação de devolução de casco"
    ),
    return_deadline_days: int = 90,
    is_active: int = 1,
) -> dict[str, object]:
    """
    Retorna o JSON esperado nas respostas da API.
    """

    return {
        "id": part_id,
        "supplier_id": supplier_id,
        "part_code": part_code,
        "name": name,
        "description": description,
        "return_deadline_days": return_deadline_days,
        "is_active": is_active,
        "created_at": "2026-07-28T10:00:00",
        "updated_at": "2026-07-28T10:00:00",
    }


def test_should_create_part_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    part = create_part()

    service_mock.create.return_value = part

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": (
                "Compressor com obrigação de devolução "
                "de casco"
            ),
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 201

    assert response.json() == expected_part_json()

    service_mock.create.assert_called_once_with(
        supplier_id=1,
        part_code="ABC123",
        name="Compressor de ar",
        description=(
            "Compressor com obrigação de devolução "
            "de casco"
        ),
        return_deadline_days=90,
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="CREATE",
        module="PART",
        entity_type="Part",
        entity_id=10,
        description="Peça cadastrada.",
        new_values={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": (
                "Compressor com obrigação "
                "de devolução de casco"
            ),
            "return_deadline_days": 90,
            "is_active": 1,
        },
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(part)
    session_mock.rollback.assert_not_called()


def test_should_create_part_without_description(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    part = create_part(
        description=None,
    )

    service_mock.create.return_value = part

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 201

    assert response.json() == expected_part_json(
        description=None,
    )

    service_mock.create.assert_called_once_with(
        supplier_id=1,
        part_code="ABC123",
        name="Compressor de ar",
        description=None,
        return_deadline_days=90,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(part)
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.post(
        "/parts",
        json={
            "supplier_id": 999,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": None,
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.create.assert_called_once_with(
        supplier_id=999,
        part_code="ABC123",
        name="Compressor de ar",
        description=None,
        return_deadline_days=90,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_supplier_is_inactive_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "O fornecedor informado está inativo."
    )

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": None,
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor informado está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_409_when_part_code_already_exists_for_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    error_message = (
        "Já existe uma peça com este código "
        "para o fornecedor informado."
    )

    service_mock.create.side_effect = ValueError(
        error_message
    )

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": None,
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": error_message,
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_required_create_field_is_missing(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_non_positive_supplier_id_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 0,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_return_deadline_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 0,
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_reject_extra_create_request_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 90,
            "manufacturer": "Fabricante não permitido",
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()

def test_should_list_all_parts(
client: TestClient,
service_mock: Mock,
) -> None:
    first_part = create_part()

    second_part = create_part(
        part_id=11,
        supplier_id=2,
        part_code="XYZ789",
        name="Alternador",
        description="Alternador remanufaturado",
        return_deadline_days=120,
    )

    service_mock.list_all.return_value = [
        first_part,
        second_part,
    ]

    response = client.get(
        "/parts",
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_part_json(),
        expected_part_json(
            part_id=11,
            supplier_id=2,
            part_code="XYZ789",
            name="Alternador",
            description="Alternador remanufaturado",
            return_deadline_days=120,
        ),
    ]

    service_mock.list_all.assert_called_once_with()
    service_mock.list_by_supplier.assert_not_called()


def test_should_return_empty_list_when_there_are_no_parts(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.list_all.return_value = []

    response = client.get(
        "/parts",
    )

    assert response.status_code == 200
    assert response.json() == []

    service_mock.list_all.assert_called_once_with()
    service_mock.list_by_supplier.assert_not_called()


def test_should_list_parts_filtered_by_supplier(
    client: TestClient,
    service_mock: Mock,
) -> None:
    first_part = create_part()

    second_part = create_part(
        part_id=11,
        part_code="DEF456",
        name="Motor de partida",
        description=None,
        return_deadline_days=120,
    )

    service_mock.list_by_supplier.return_value = [
        first_part,
        second_part,
    ]

    response = client.get(
        "/parts",
        params={
            "supplier_id": 1,
        },
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_part_json(),
        expected_part_json(
            part_id=11,
            part_code="DEF456",
            name="Motor de partida",
            description=None,
            return_deadline_days=120,
        ),
    ]

    service_mock.list_by_supplier.assert_called_once_with(
        1
    )

    service_mock.list_all.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_list(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.list_by_supplier.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get(
        "/parts",
        params={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.list_by_supplier.assert_called_once_with(
        999
    )

    service_mock.list_all.assert_not_called()


def test_should_return_422_for_non_positive_supplier_filter(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/parts",
        params={
            "supplier_id": 0,
        },
    )

    assert response.status_code == 422

    service_mock.list_all.assert_not_called()
    service_mock.list_by_supplier.assert_not_called()


def test_should_return_part_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    part = create_part()

    service_mock.get_required.return_value = part

    response = client.get(
        "/parts/10",
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json()

    service_mock.get_required.assert_called_once_with(
        10
    )


def test_should_return_404_when_part_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.get(
        "/parts/999",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.get_required.assert_called_once_with(
        999
    )


def test_should_return_422_for_non_positive_part_id_on_get(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/parts/0",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()


def test_should_return_422_for_invalid_text_part_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/parts/invalid-id",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()

def test_should_update_part_name(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    original_part = create_part()

    updated_part = create_part(
        name="Compressor de ar atualizado",
    )

    service_mock.get_required.return_value = (
        original_part
    )

    service_mock.update.return_value = (
        updated_part
    )

    response = client.put(
        "/parts/10",
        json={
            "name": "Compressor de ar atualizado",
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        name="Compressor de ar atualizado",
    )

    service_mock.get_required.assert_called_once_with(
        10
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        name="Compressor de ar atualizado",
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="UPDATE",
        module="PART",
        entity_type="Part",
        entity_id=10,
        description="Peça atualizada.",
        old_values={
            "name": "Compressor de ar",
        },
        new_values={
            "name": "Compressor de ar atualizado",
        },
    )

    session_mock.commit.assert_called_once_with()

    session_mock.refresh.assert_called_once_with(
        updated_part
    )

    session_mock.rollback.assert_not_called()


def test_should_update_part_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        supplier_id=2,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        supplier_id=2,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_part_code(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        part_code="XYZ789",
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "part_code": "XYZ789",
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        part_code="XYZ789",
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        part_code="XYZ789",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_return_deadline_days(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        return_deadline_days=120,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "return_deadline_days": 120,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        return_deadline_days=120,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        return_deadline_days=120,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_multiple_part_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        supplier_id=2,
        part_code="NOVO123",
        name="Motor de partida",
        description="Descrição atualizada",
        return_deadline_days=180,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
            "part_code": "NOVO123",
            "name": "Motor de partida",
            "description": "Descrição atualizada",
            "return_deadline_days": 180,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        supplier_id=2,
        part_code="NOVO123",
        name="Motor de partida",
        description="Descrição atualizada",
        return_deadline_days=180,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
        part_code="NOVO123",
        name="Motor de partida",
        description="Descrição atualizada",
        return_deadline_days=180,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_clear_part_description(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        description=None,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "description": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        description=None,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        description=None,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_accept_empty_update_body(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    part = create_part()

    service_mock.update.return_value = part

    response = client.put(
        "/parts/10",
        json={},
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json()

    service_mock.update.assert_called_once_with(
        part_id=10,
    )

    service_mock.get_required.assert_not_called()

    audit_service.register.assert_not_called()

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(part)
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_part_is_not_found_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.put(
        "/parts/999",
        json={
            "name": "Novo nome",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.update.assert_called_once_with(
        part_id=999,
        name="Novo nome",
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=999,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_new_supplier_is_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "O fornecedor informado está inativo."
    )

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor informado está inativo.",
    }

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_409_when_updated_combination_already_exists(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    error_message = (
        "Já existe uma peça com este código "
        "para o fornecedor informado."
    )

    service_mock.update.side_effect = ValueError(
        error_message
    )

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
            "part_code": "ABC123",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": error_message,
    }

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
        part_code="ABC123",
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_non_positive_part_id_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/0",
        json={
            "name": "Novo nome",
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_supplier_id_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 0,
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_deadline_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "return_deadline_days": 0,
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_deadline_above_maximum_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "return_deadline_days": 3651,
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_empty_part_code_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "part_code": "",
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_reject_extra_update_request_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "name": "Motor de partida",
            "manufacturer": "Campo não permitido",
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()

def test_should_activate_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    part = create_part(
        is_active=1,
    )

    service_mock.activate.return_value = part

    response = client.patch(
        "/parts/10/activate",
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        is_active=1,
    )

    service_mock.activate.assert_called_once_with(
        10,
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="ACTIVATE",
        module="PART",
        entity_type="Part",
        entity_id=10,
        description="Peça ativada.",
        old_values={
            "is_active": 0,
        },
        new_values={
            "is_active": 1,
        },
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        part,
    )
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_activate_unknown_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.activate.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.patch(
        "/parts/999/activate",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.activate.assert_called_once_with(
        999,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_part_is_already_active(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.activate.side_effect = ValueError(
        "A peça já está ativa."
    )

    response = client.patch(
        "/parts/10/activate",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "A peça já está ativa.",
    }

    service_mock.activate.assert_called_once_with(
        10,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_activate_invalid_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.patch(
        "/parts/0/activate",
    )

    assert response.status_code == 422

    service_mock.activate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_deactivate_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    part = create_part(
        is_active=0,
    )

    service_mock.deactivate.return_value = part

    response = client.patch(
        "/parts/10/deactivate",
        json={
            "justification": (
                "Peça descontinuada pelo fornecedor."
            ),
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        is_active=0,
    )

    service_mock.deactivate.assert_called_once_with(
        10,
    )

    audit_service.register.assert_called_once_with(
        user_id=2,
        action="DEACTIVATE",
        module="PART",
        entity_type="Part",
        entity_id=10,
        description="Peça desativada.",
        old_values={
            "is_active": 1,
        },
        new_values={
            "is_active": 0,
        },
        justification=(
            "Peça descontinuada pelo fornecedor."
        ),
    )

    session_mock.commit.assert_called_once_with()

    session_mock.refresh.assert_called_once_with(
        part,
    )

    session_mock.rollback.assert_not_called()


def test_should_return_404_when_deactivate_unknown_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.patch(
        "/parts/999/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.deactivate.assert_called_once_with(
        999,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_part_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "A peça já está inativa."
    )

    response = client.patch(
        "/parts/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "A peça já está inativa.",
    }

    service_mock.deactivate.assert_called_once_with(
        10,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_deactivate_invalid_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.patch(
        "/parts/0/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 422

    service_mock.deactivate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()

@pytest.mark.parametrize(
    "payload",
    [
        {},
        {
            "justification": "",
        },
        {
            "justification": "   ",
        },
    ],
)
def test_should_return_422_when_deactivate_justification_is_invalid(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    payload: dict[str, object],
) -> None:
    response = client.patch(
        "/parts/10/deactivate",
        json=payload,
    )

    assert response.status_code == 422

    service_mock.deactivate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()

def test_should_return_422_when_deactivate_has_extra_field(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.patch(
        "/parts/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
            "unexpected_field": "value",
        },
    )

    assert response.status_code == 422

    service_mock.deactivate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_rollback_when_audit_fails_on_deactivate(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
    audit_service: Mock,
) -> None:
    part = create_part(
        is_active=0,
    )

    service_mock.deactivate.return_value = part

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.patch(
        "/parts/10/deactivate",
        json={
            "justification": (
                "Desativação de teste."
            ),
        },
    )

    assert response.status_code == 500

    service_mock.deactivate.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once()

    session_mock.rollback.assert_called_once_with()

    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_401_without_authentication(
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    def override_service() -> Mock:
        return service_mock

    def override_session():
        yield session_mock

    app.dependency_overrides[
        get_part_service
    ] = override_service

    app.dependency_overrides[
        get_session
    ] = override_session

    try:
        with TestClient(app) as test_client:
            response = test_client.get(
                "/parts"
            )

        assert response.status_code == 401

        service_mock.list_all.assert_not_called()

    finally:
        app.dependency_overrides.clear()


def test_should_return_403_when_seller_accesses_parts(
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    seller_user = SimpleNamespace(
        id=3,
        username="vendedor",
        role_id=3,
        is_active=1,
    )

    seller_role = SimpleNamespace(
        id=3,
        name="Vendedor",
    )

    def override_service() -> Mock:
        return service_mock

    def override_session():
        yield session_mock

    def override_get_current_user():
        return seller_user

    session_mock.scalar.return_value = (
        seller_role
    )

    app.dependency_overrides[
        get_part_service
    ] = override_service

    app.dependency_overrides[
        get_session
    ] = override_session

    app.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    try:
        with TestClient(app) as test_client:
            response = test_client.get(
                "/parts"
            )

        assert response.status_code == 403

        assert response.json() == {
            "detail": (
                "O usuário autenticado não possui "
                "permissão para realizar esta "
                "operação."
            ),
        }

        service_mock.list_all.assert_not_called()

    finally:
        app.dependency_overrides.clear()