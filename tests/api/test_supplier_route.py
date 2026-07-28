from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.supplier_route import (
    get_supplier_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.supplier_service import SupplierService


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock do serviço de fornecedores.
    """

    return Mock(spec=SupplierService)


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
def client(
    service_mock: Mock,
    session_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo o serviço e a sessão reais.
    """

    def override_supplier_service() -> Mock:
        return service_mock

    def override_session() -> Generator[Mock, None, None]:
        yield session_mock

    app.dependency_overrides[
        get_supplier_service
    ] = override_supplier_service

    app.dependency_overrides[
        get_session
    ] = override_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_supplier(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    document: str | None = "12.345.678/0001-90",
    address: str | None = "Registro/SP",
    notes: str | None = "Fornecedor de teste",
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados pelo schema.
    """

    return SimpleNamespace(
        id=supplier_id,
        name=name,
        document=document,
        address=address,
        notes=notes,
        is_active=is_active,
        created_at="2026-07-28T10:00:00",
        updated_at="2026-07-28T10:00:00",
    )


def expected_supplier_json(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    document: str | None = "12.345.678/0001-90",
    address: str | None = "Registro/SP",
    notes: str | None = "Fornecedor de teste",
    is_active: int = 1,
) -> dict[str, object]:
    """
    Retorna o JSON esperado nas respostas.
    """

    return {
        "id": supplier_id,
        "name": name,
        "document": document,
        "address": address,
        "notes": notes,
        "is_active": is_active,
        "created_at": "2026-07-28T10:00:00",
        "updated_at": "2026-07-28T10:00:00",
    }


def test_should_create_supplier_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier()

    service_mock.create.return_value = supplier

    response = client.post(
        "/suppliers",
        json={
            "name": "Fornecedor Teste",
            "document": "12.345.678/0001-90",
            "address": "Registro/SP",
            "notes": "Fornecedor de teste",
        },
    )

    assert response.status_code == 201
    assert response.json() == expected_supplier_json()

    service_mock.create.assert_called_once_with(
        name="Fornecedor Teste",
        document="12.345.678/0001-90",
        address="Registro/SP",
        notes="Fornecedor de teste",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_list_suppliers(
    client: TestClient,
    service_mock: Mock,
) -> None:
    first_supplier = create_supplier()

    second_supplier = create_supplier(
        supplier_id=2,
        name="Segundo Fornecedor",
        document=None,
        address=None,
        notes=None,
        is_active=0,
    )

    service_mock.list_all.return_value = [
        first_supplier,
        second_supplier,
    ]

    response = client.get("/suppliers")

    assert response.status_code == 200

    assert response.json() == [
        expected_supplier_json(),
        expected_supplier_json(
            supplier_id=2,
            name="Segundo Fornecedor",
            document=None,
            address=None,
            notes=None,
            is_active=0,
        ),
    ]

    service_mock.list_all.assert_called_once_with()


def test_should_get_supplier_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    supplier = create_supplier()

    service_mock.get_required.return_value = supplier

    response = client.get("/suppliers/1")

    assert response.status_code == 200
    assert response.json() == expected_supplier_json()

    service_mock.get_required.assert_called_once_with(1)


def test_should_return_404_when_supplier_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get("/suppliers/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.get_required.assert_called_once_with(999)


def test_should_update_only_informed_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier(
        address="Novo endereço",
        notes=None,
    )

    service_mock.update.return_value = supplier

    response = client.put(
        "/suppliers/1",
        json={
            "address": "Novo endereço",
            "notes": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        address="Novo endereço",
        notes=None,
    )

    service_mock.update.assert_called_once_with(
        1,
        address="Novo endereço",
        notes=None,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_return_409_for_duplicate_document(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "Já existe um fornecedor com este documento."
    )

    response = client.post(
        "/suppliers",
        json={
            "name": "Fornecedor Duplicado",
            "document": "12.345.678/0001-90",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe um fornecedor com este documento."
        ),
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_deactivate_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier(
        is_active=0,
    )

    service_mock.deactivate.return_value = supplier

    response = client.patch(
        "/suppliers/1/deactivate",
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        is_active=0,
    )

    service_mock.deactivate.assert_called_once_with(1)

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_activate_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier(
        is_active=1,
    )

    service_mock.activate.return_value = supplier

    response = client.patch(
        "/suppliers/1/activate",
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        is_active=1,
    )

    service_mock.activate.assert_called_once_with(1)

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_return_400_when_supplier_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "O fornecedor já está inativo."
    )

    response = client.patch(
        "/suppliers/1/deactivate",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor já está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()


def test_should_return_422_for_invalid_supplier_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.get(
        "/suppliers/0",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()