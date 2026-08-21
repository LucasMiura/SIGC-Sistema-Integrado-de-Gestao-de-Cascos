from collections.abc import Generator
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.outbound_route import (
    get_outbound_service,
    router,
)
from src.database.connection import (
    get_session,
)
from src.models.outbound import Outbound
from src.services.outbound_service import (
    OutboundService,
)
from src.models.outbound_item import OutboundItem
from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.authorization import (
    ROLE_SELLER,
)
from src.api.dependencies.audit import (
    get_audit_service,
)
from src.services.audit_service import (
    AuditService,
)


def create_outbound(
    outbound_id: int = 10,
    destination_type: str = "WORK_ORDER",
    work_order_number: str | None = "OS-12345",
    sales_invoice_number: str | None = None,
    customer_name: str = "Cliente Teste",
    created_by: int = 1,
    created_at: str = "2026-07-29T10:00:00",
    updated_at: str = "2026-07-29T10:00:00",
    status: str = "ACTIVE",
) -> Outbound:
    outbound = Outbound(
        destination_type=destination_type,
        work_order_number=work_order_number,
        sales_invoice_number=sales_invoice_number,
        customer_name=customer_name,
        created_by=created_by,
        status=status,
    )

    outbound.id = outbound_id
    outbound.created_at = created_at
    outbound.updated_at = updated_at

    return outbound


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=OutboundService,
    )

@pytest.fixture
def audit_service() -> Mock:
    return Mock(
        spec=AuditService,
    )

@pytest.fixture
def app(
    session: Mock,
    service: Mock,
    audit_service: Mock,
) -> Generator[FastAPI, None, None]:
    application = FastAPI()

    seller_user = Mock()
    seller_user.id = 1
    seller_user.username = "vendedor"
    seller_user.role_id = 3
    seller_user.is_active = 1

    seller_role = Mock()
    seller_role.id = 3
    seller_role.name = ROLE_SELLER

    def override_get_current_user():
        return seller_user

    session.scalar.return_value = (
        seller_role
    )

    application.dependency_overrides[
        get_session
    ] = lambda: session

    application.dependency_overrides[
        get_outbound_service
    ] = lambda: service

    application.dependency_overrides[
        get_audit_service
    ] = lambda: audit_service

    application.dependency_overrides[
        get_current_user
    ] = override_get_current_user

    application.include_router(
        router
    )

    yield application

    application.dependency_overrides.clear()


@pytest.fixture
def client(
    app: FastAPI,
) -> Generator[TestClient, None, None]:
    with TestClient(
        app,
        raise_server_exceptions=False,
    ) as test_client:
        yield test_client


def test_should_create_outbound(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    outbound = create_outbound()

    service.create_outbound.return_value = (
        outbound
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "sales_invoice_number": None,
            "customer_name": "Cliente Teste",
            "status": "ACTIVE",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "destination_type": "WORK_ORDER",
        "work_order_number": "OS-12345",
        "sales_invoice_number": None,
        "customer_name": "Cliente Teste",
        "created_by": 1,
        "created_at": "2026-07-29T10:00:00",
        "updated_at": "2026-07-29T10:00:00",
        "status": "ACTIVE",
    }

    service.create_outbound.assert_called_once_with(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
        customer_name="Cliente Teste",
        created_by=1,
        status="ACTIVE",
    )

    audit_service.register.assert_called_once_with(
        user_id=1,
        action="CREATE",
        module="OUTBOUND",
        entity_type="Outbound",
        entity_id=10,
        description="Saída cadastrada.",
        new_values={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "sales_invoice_number": None,
            "customer_name": "Cliente Teste",
            "status": "ACTIVE",
            "created_by": 1,
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound
    )

    session.rollback.assert_not_called()


def test_should_create_outbound_with_sales_invoice(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        customer_name="Cliente Balcão",
    )

    service.create_outbound.return_value = (
        outbound
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-12345",
            "customer_name": "Cliente Balcão",
        },
    )

    assert response.status_code == 201

    assert response.json()[
        "destination_type"
    ] == "SALE"

    assert response.json()[
        "work_order_number"
    ] is None

    assert response.json()[
        "sales_invoice_number"
    ] == "NFV-12345"

    assert response.json()[
        "customer_name"
    ] == "Cliente Balcão"

    service.create_outbound.assert_called_once_with(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        customer_name="Cliente Balcão",
        created_by=1,
        status="ACTIVE",
    )

    audit_service.register.assert_called_once_with(
        user_id=1,
        action="CREATE",
        module="OUTBOUND",
        entity_type="Outbound",
        entity_id=10,
        description="Saída cadastrada.",
        new_values={
            "destination_type": "SALE",
            "work_order_number": None,
            "sales_invoice_number": "NFV-12345",
            "customer_name": "Cliente Balcão",
            "status": "ACTIVE",
            "created_by": 1,
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound
    )


def test_should_use_active_status_by_default_on_create(
    client: TestClient,
    service: Mock,
) -> None:
    service.create_outbound.return_value = (
        create_outbound(
            customer_name="Cliente Teste",
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 201

    service.create_outbound.assert_called_once_with(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
        customer_name="Cliente Teste",
        created_by=1,
        status="ACTIVE",
    )

def test_should_rollback_when_audit_fails_on_create(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    outbound = create_outbound(
        customer_name="Cliente Teste",
    )

    service.create_outbound.return_value = (
        outbound
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 500

    service.create_outbound.assert_called_once_with(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
        customer_name="Cliente Teste",
        created_by=1,
        status="ACTIVE",
    )

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_reference_numbers_are_missing(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        ValueError(
            (
                "A saída deve possuir uma ordem de serviço "
                "ou uma nota fiscal de venda."
            )
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        )
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_work_order_is_duplicated(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        ValueError(
            (
                "Já existe uma saída com esta "
                "ordem de serviço."
            )
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Já existe uma saída com esta "
            "ordem de serviço."
        )
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()


def test_should_return_400_when_sales_invoice_is_duplicated(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        ValueError(
            (
                "Já existe uma saída com esta "
                "nota fiscal de venda."
            )
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Já existe uma saída com esta "
            "nota fiscal de venda."
        )
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "field",
    ),
    [
        (
            {
                "destination_type": "",
                "work_order_number": "OS-12345",
                "customer_name": "Cliente Teste",
            },
            "destination_type",
        ),
        (
            {
                "destination_type": "WORK_ORDER",
                "work_order_number": "OS-12345",
                "customer_name": "Cliente Teste",
                "status": "PENDING",
            },
            "status",
        ),
        (
            {
                "destination_type": "WORK_ORDER",
                "work_order_number": "OS-12345",
                "customer_name": "",
            },
            "customer_name",
        ),
    ],
)
def test_should_return_422_when_create_payload_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, object],
    field: str,
) -> None:
    response = client.post(
        "/outbounds",
        json=payload,
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == field
        for error in response.json()["detail"]
    )

    service.create_outbound.assert_not_called()


def test_should_return_422_when_customer_name_is_missing(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == "customer_name"
        for error in response.json()["detail"]
    )

    service.create_outbound.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "customer_name": "Cliente Teste",
            "unexpected_field": "valor",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1]
        == "unexpected_field"
        for error in response.json()["detail"]
    )

    service.create_outbound.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_create(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "customer_name": "Cliente Teste",
        },
    )

    assert response.status_code == 500

    service.create_outbound.assert_called_once_with(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
        customer_name="Cliente Teste",
        created_by=1,
        status="ACTIVE",
    )

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_all_outbounds(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = [
        create_outbound(
            outbound_id=10,
        ),
        create_outbound(
            outbound_id=11,
            destination_type="SALE",
            work_order_number=None,
            sales_invoice_number="NFV-12345",
        ),
    ]

    response = client.get(
        "/outbounds"
    )

    assert response.status_code == 200

    assert len(response.json()) == 2

    assert response.json()[0]["id"] == 10

    assert response.json()[1]["id"] == 11

    assert response.json()[1][
        "destination_type"
    ] == "SALE"

    service.list_outbounds.assert_called_once_with(
        status=None,
        destination_type=None,
    )


def test_should_return_empty_outbound_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = []

    response = client.get(
        "/outbounds"
    )

    assert response.status_code == 200

    assert response.json() == []

    service.list_outbounds.assert_called_once_with(
        status=None,
        destination_type=None,
    )


def test_should_list_outbounds_filtered_by_status(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = [
        create_outbound(
            status="CANCELLED",
        )
    ]

    response = client.get(
        "/outbounds",
        params={
            "status": "CANCELLED",
        },
    )

    assert response.status_code == 200

    assert response.json()[0][
        "status"
    ] == "CANCELLED"

    service.list_outbounds.assert_called_once_with(
        status="CANCELLED",
        destination_type=None,
    )


def test_should_list_outbounds_filtered_by_destination_type(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = [
        create_outbound(
            destination_type="SALE",
            work_order_number=None,
            sales_invoice_number="NFV-12345",
        )
    ]

    response = client.get(
        "/outbounds",
        params={
            "destination_type": "SALE",
        },
    )

    assert response.status_code == 200

    assert response.json()[0][
        "destination_type"
    ] == "SALE"

    service.list_outbounds.assert_called_once_with(
        status=None,
        destination_type="SALE",
    )


def test_should_return_400_when_multiple_filters_are_sent(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.side_effect = (
        ValueError(
            "Informe apenas um filtro por vez."
        )
    )

    response = client.get(
        "/outbounds",
        params={
            "status": "ACTIVE",
            "destination_type": "WORK_ORDER",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Informe apenas um filtro por vez."
        )
    }

    service.list_outbounds.assert_called_once_with(
        status="ACTIVE",
        destination_type="WORK_ORDER",
    )


def test_should_return_422_when_status_filter_is_invalid(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.get(
        "/outbounds",
        params={
            "status": "PENDING",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == "status"
        for error in response.json()["detail"]
    )

    service.list_outbounds.assert_not_called()


def test_should_return_422_when_destination_type_filter_is_blank(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.get(
        "/outbounds",
        params={
            "destination_type": "",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1]
        == "destination_type"
        for error in response.json()["detail"]
    )

    service.list_outbounds.assert_not_called()


def test_should_get_outbound(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound()
    )

    response = client.get(
        "/outbounds/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "destination_type": "WORK_ORDER",
        "work_order_number": "OS-12345",
        "sales_invoice_number": None,
        "customer_name": "Cliente Teste",
        "created_by": 1,
        "created_at": "2026-07-29T10:00:00",
        "updated_at": "2026-07-29T10:00:00",
        "status": "ACTIVE",
    }

    service.get_outbound.assert_called_once_with(
        10
    )


def test_should_return_404_when_outbound_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_outbound.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.get(
        "/outbounds/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    service.get_outbound.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_outbound_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.get(
        f"/outbounds/{outbound_id}"
    )

    assert response.status_code == 422

    service.get_outbound.assert_not_called()

def test_should_update_outbound(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    existing_outbound = create_outbound()

    service.get_outbound.return_value = (
        existing_outbound
    )

    outbound = create_outbound(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-67890",
    )

    service.update_outbound.return_value = outbound

    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-67890",
        },
    )

    assert response.status_code == 200

    assert response.json()["destination_type"] == "SALE"
    assert response.json()["sales_invoice_number"] == "NFV-67890"

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        destination_type="SALE",
        sales_invoice_number="NFV-67890",
    )

    service.get_outbound.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once_with(
        user_id=1,
        action="UPDATE",
        module="OUTBOUND",
        entity_type="Outbound",
        entity_id=10,
        description="Saída atualizada.",
        old_values={
            "destination_type": "WORK_ORDER",
            "sales_invoice_number": None,
        },
        new_values={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-67890",
        },
    )

    session.commit.assert_called_once_with()
    session.refresh.assert_called_once_with(outbound)
    session.rollback.assert_not_called()


def test_should_update_only_status(
    client: TestClient,
    service: Mock,
) -> None:
    outbound = create_outbound(
        status="ACTIVE",
    )

    service.get_outbound.return_value = (
        create_outbound(
            status="ACTIVE",
        )
    )

    service.update_outbound.return_value = outbound

    response = client.patch(
        "/outbounds/10",
        json={
            "status": "ACTIVE",
        },
    )

    assert response.status_code == 200

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        status="ACTIVE",
    )

def test_should_update_outbound_customer_name(
    client: TestClient,
    service: Mock,
    audit_service: Mock,
) -> None:
    existing = create_outbound(
        customer_name="Cliente Antigo",
    )

    updated = create_outbound(
        customer_name="Cliente Atualizado",
    )

    service.get_outbound.return_value = (
        existing
    )

    service.update_outbound.return_value = (
        updated
    )

    response = client.patch(
        "/outbounds/10",
        json={
            "customer_name":
                "Cliente Atualizado",
        },
    )

    assert response.status_code == 200

    assert response.json()[
        "customer_name"
    ] == "Cliente Atualizado"

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        customer_name="Cliente Atualizado",
    )

    audit_service.register.assert_called_once_with(
        user_id=1,
        action="UPDATE",
        module="OUTBOUND",
        entity_type="Outbound",
        entity_id=10,
        description="Saída atualizada.",
        old_values={
            "customer_name":
                "Cliente Antigo",
        },
        new_values={
            "customer_name":
                "Cliente Atualizado",
        },
    )


def test_should_send_only_modified_fields(
    client: TestClient,
    service: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="INTERNAL_USE",
    )

    service.get_outbound.return_value = (
        create_outbound()
    )

    service.update_outbound.return_value = outbound

    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "INTERNAL_USE",
        },
    )

    assert response.status_code == 200

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        destination_type="INTERNAL_USE",
    )


def test_should_return_404_when_update_outbound_is_not_found(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    service.update_outbound.assert_not_called()

    response = client.patch(
        "/outbounds/999",
        json={
            "destination_type": "SALE",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()


def test_should_return_400_when_update_business_rule_fails(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound()
    )
    
    service.update_outbound.side_effect = ValueError(
        "Já existe uma saída com esta ordem de serviço."
    )

    response = client.patch(
        "/outbounds/10",
        json={
            "work_order_number": "OS-12345",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Já existe uma saída com esta ordem de serviço."
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()


def test_should_return_422_when_update_payload_is_invalid(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.patch(
        "/outbounds/10",
        json={
            "status": "PENDING",
        },
    )

    assert response.status_code == 422

    service.update_outbound.assert_not_called()


def test_should_return_422_when_update_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "SALE",
            "unexpected": True,
        },
    )

    assert response.status_code == 422

    service.update_outbound.assert_not_called()


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_update_id_is_invalid(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.patch(
        f"/outbounds/{outbound_id}",
        json={
            "destination_type": "SALE",
        },
    )

    assert response.status_code == 422

    service.update_outbound.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_update(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound()
    )

    service.update_outbound.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.patch(
        "/outbounds/10",
        json={
            "status": "ACTIVE",
        },
    )

    assert response.status_code == 500

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        status="ACTIVE",
    )

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def create_outbound_item(
    outbound_item_id: int = 50,
    outbound_id: int = 10,
    part_id: int = 40,
    quantity: int = 5,
    created_at: str = "2026-07-29T10:05:00",
) -> OutboundItem:
    outbound_item = OutboundItem(
        outbound_id=outbound_id,
        part_id=part_id,
        quantity=quantity,
    )

    outbound_item.id = outbound_item_id
    outbound_item.created_at = created_at

    return outbound_item


def test_should_cancel_outbound(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    existing_outbound = create_outbound(
        status="ACTIVE",
    )

    cancelled_outbound = create_outbound(
        status="CANCELLED",
    )

    service.get_outbound.return_value = (
        existing_outbound
    )

    service.cancel_outbound.return_value = (
        cancelled_outbound
    )

    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "Saída lançada incorretamente."
            ),
        },
    )

    assert response.status_code == 200

    assert response.json()[
        "status"
    ] == "CANCELLED"

    service.get_outbound.assert_called_once_with(
        10
    )

    service.cancel_outbound.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once_with(
        user_id=1,
        action="CANCEL",
        module="OUTBOUND",
        entity_type="Outbound",
        entity_id=10,
        description="Saída cancelada.",
        old_values={
            "status": "ACTIVE",
        },
        new_values={
            "status": "CANCELLED",
        },
        justification=(
            "Saída lançada incorretamente."
        ),
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        cancelled_outbound
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_cancel_outbound_is_not_found(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.patch(
        "/outbounds/999/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    service.get_outbound.assert_called_once_with(
        999
    )

    service.cancel_outbound.assert_not_called()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_outbound_is_already_cancelled(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound(
            status="ACTIVE",
        )
    )
    service.cancel_outbound.side_effect = (
        ValueError(
            "A saída já está cancelada."
        )
    )

    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "A saída já está cancelada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


def test_should_return_404_when_purchase_item_is_not_found_on_cancel(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound(
            status="ACTIVE",
        )
    )
    message = (
        "Item de compra relacionado "
        "à saída não encontrado."
    )

    service.cancel_outbound.side_effect = (
        ValueError(message)
    )

    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_cancel_id_is_invalid(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.patch(
        f"/outbounds/{outbound_id}/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 422

    service.cancel_outbound.assert_not_called()

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
def test_should_return_422_when_cancel_justification_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, object],
) -> None:
    response = client.patch(
        "/outbounds/10/cancel",
        json=payload,
    )

    assert response.status_code == 422

    service.get_outbound.assert_not_called()
    service.cancel_outbound.assert_not_called()

def test_should_return_422_when_cancel_payload_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
            "unknown_field": "valor",
        },
    )

    assert response.status_code == 422

    service.get_outbound.assert_not_called()
    service.cancel_outbound.assert_not_called()

def test_should_rollback_when_audit_fails_on_cancel(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound(
            status="ACTIVE",
        )
    )

    service.cancel_outbound.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "Saída lançada incorretamente."
            ),
        },
    )

    assert response.status_code == 500

    service.get_outbound.assert_called_once_with(
        10
    )

    service.cancel_outbound.assert_called_once_with(
        10
    )

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_strip_cancel_justification(
    client: TestClient,
    service: Mock,
    audit_service: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound(
            status="ACTIVE",
        )
    )

    service.cancel_outbound.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "  Erro no lançamento.  "
            ),
        },
    )

    assert response.status_code == 200

    assert (
        audit_service.register.call_args.kwargs[
            "justification"
        ]
        == "Erro no lançamento."
    )

def test_should_rollback_when_unexpected_error_occurs_on_cancel(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound(
            status="ACTIVE",
        )
    )
    service.cancel_outbound.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.patch(
        "/outbounds/10/cancel",
        json={
            "justification": (
                "Cancelamento de teste."
            ),
        },
    )

    assert response.status_code == 500

    service.cancel_outbound.assert_called_once_with(
        10
    )

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_add_outbound_item(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    outbound_item = create_outbound_item()

    service.add_item.return_value = (
        outbound_item
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 50,
        "outbound_id": 10,
        "part_id": 40,
        "quantity": 5,
        "created_at": "2026-07-29T10:05:00",
    }

    service.add_item.assert_called_once_with(
        outbound_id=10,
        part_id=40,
        quantity=5,
    )

    audit_service.register.assert_called_once_with(
        user_id=1,
        action="CREATE",
        module="OUTBOUND",
        entity_type="OutboundItem",
        entity_id=50,
        description="Item adicionado à saída.",
        new_values={
            "outbound_id": 10,
            "part_id": 40,
            "quantity": 5,
        },
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound_item
    )

    session.rollback.assert_not_called()

def test_should_rollback_when_audit_fails_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    outbound_item = create_outbound_item()

    service.add_item.return_value = (
        outbound_item
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 500

    service.add_item.assert_called_once_with(
        outbound_id=10,
        part_id=40,
        quantity=5,
    )

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_rollback_when_audit_fails_on_update(
    client: TestClient,
    service: Mock,
    session: Mock,
    audit_service: Mock,
) -> None:
    existing_outbound = create_outbound()

    updated_outbound = create_outbound(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-67890",
    )

    service.get_outbound.return_value = (
        existing_outbound
    )

    service.update_outbound.return_value = (
        updated_outbound
    )

    audit_service.register.side_effect = (
        RuntimeError(
            "Falha ao registrar auditoria."
        )
    )

    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-67890",
        },
    )

    assert response.status_code == 500

    service.get_outbound.assert_called_once_with(
        10
    )

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        destination_type="SALE",
        sales_invoice_number="NFV-67890",
    )

    audit_service.register.assert_called_once()

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_404_when_outbound_is_not_found_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.add_item.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.post(
        "/outbounds/999/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_return_404_when_part_is_not_found_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.add_item.side_effect = (
        ValueError(
            "Peça não encontrada."
        )
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 999,
            "quantity": 5,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        (
            "Não é possível adicionar itens "
            "a uma saída cancelada."
        ),
        "A peça informada está inativa.",
        (
            "A peça informada já foi adicionada "
            "a esta saída."
        ),
        "Estoque insuficiente para a peça informada.",
        "Não há estoque disponível para a peça informada.",
        (
            "Não foi possível completar a alocação "
            "da quantidade solicitada."
        ),
    ],
)
def test_should_return_400_when_add_item_business_rule_fails(
    client: TestClient,
    service: Mock,
    session: Mock,
    message: str,
) -> None:
    service.add_item.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": message
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "field",
    ),
    [
        (
            {
                "part_id": 0,
                "quantity": 5,
            },
            "part_id",
        ),
        (
            {
                "part_id": -1,
                "quantity": 5,
            },
            "part_id",
        ),
        (
            {
                "part_id": 40,
                "quantity": 0,
            },
            "quantity",
        ),
        (
            {
                "part_id": 40,
                "quantity": -1,
            },
            "quantity",
        ),
    ],
)
def test_should_return_422_when_add_item_payload_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, int],
    field: str,
) -> None:
    response = client.post(
        "/outbounds/10/items",
        json=payload,
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == field
        for error in response.json()["detail"]
    )

    service.add_item.assert_not_called()


def test_should_return_422_when_add_item_payload_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
            "unexpected_field": True,
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1]
        == "unexpected_field"
        for error in response.json()["detail"]
    )

    service.add_item.assert_not_called()


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_outbound_id_is_invalid_on_add_item(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.post(
        f"/outbounds/{outbound_id}/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.add_item.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 20,
            "quantity": 2,
        },
    )

    assert response.status_code == 500

    service.add_item.assert_called_once_with(
        outbound_id=10,
        part_id=20,
        quantity=2,
    )

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_outbound_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbound_items.return_value = [
        create_outbound_item(
            outbound_item_id=50,
            part_id=40,
            quantity=5,
        ),
        create_outbound_item(
            outbound_item_id=51,
            part_id=41,
            quantity=3,
        ),
    ]

    response = client.get(
        "/outbounds/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 50,
            "outbound_id": 10,
            "part_id": 40,
            "quantity": 5,
            "created_at": "2026-07-29T10:05:00",
        },
        {
            "id": 51,
            "outbound_id": 10,
            "part_id": 41,
            "quantity": 3,
            "created_at": "2026-07-29T10:05:00",
        },
    ]

    service.list_outbound_items.assert_called_once_with(
        10
    )


def test_should_return_empty_outbound_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbound_items.return_value = []

    response = client.get(
        "/outbounds/10/items"
    )

    assert response.status_code == 200

    assert response.json() == []

    service.list_outbound_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_outbound_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbound_items.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.get(
        "/outbounds/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    service.list_outbound_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_outbound_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.get(
        f"/outbounds/{outbound_id}/items"
    )

    assert response.status_code == 422

    service.list_outbound_items.assert_not_called()