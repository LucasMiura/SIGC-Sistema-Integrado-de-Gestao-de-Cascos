import json
from unittest.mock import Mock

import pytest

from src.models.audit_log import AuditLog
from src.repositories.audit_log_repository import (
    AuditLogRepository,
)
from src.services.audit_service import (
    AuditService,
)


@pytest.fixture
def repository() -> Mock:
    """
    Cria um repository de auditoria
    simulado.
    """

    return Mock(
        spec=AuditLogRepository,
    )


@pytest.fixture
def service(
    repository: Mock,
) -> AuditService:
    """
    Cria o serviço de auditoria
    com repository simulado.
    """

    return AuditService(
        repository
    )


def create_audit_log(
    *,
    audit_log_id: int = 1,
    user_id: int = 10,
    action: str = "CREATE",
    module: str = "PURCHASE",
    entity_type: str = "Purchase",
    entity_id: int = 20,
    description: str | None = (
        "Compra cadastrada."
    ),
    old_values: str | None = None,
    new_values: str | None = None,
    justification: str | None = None,
) -> AuditLog:
    """
    Cria um registro de auditoria
    para uso nos testes.
    """

    return AuditLog(
        id=audit_log_id,
        user_id=user_id,
        action=action,
        module=module,
        entity_type=entity_type,
        entity_id=entity_id,
        description=description,
        old_values=old_values,
        new_values=new_values,
        justification=justification,
        created_at="2026-08-10T14:30:00",
    )


def test_should_register_audit_log(
    service: AuditService,
    repository: Mock,
) -> None:
    repository.add.side_effect = (
        lambda audit_log: audit_log
    )

    result = service.register(
        user_id=10,
        action="CREATE",
        module="PURCHASE",
        entity_type="Purchase",
        entity_id=20,
        description="Compra cadastrada.",
        new_values={
            "invoice_number": "NF-12345",
            "status": "RECEIVED",
        },
    )

    assert result.user_id == 10
    assert result.action == "CREATE"
    assert result.module == "PURCHASE"
    assert result.entity_type == "Purchase"
    assert result.entity_id == 20

    assert result.description == (
        "Compra cadastrada."
    )

    assert result.old_values is None

    assert json.loads(
        result.new_values
    ) == {
        "invoice_number": "NF-12345",
        "status": "RECEIVED",
    }

    assert result.justification is None

    repository.add.assert_called_once_with(
        result
    )


def test_should_normalize_audit_texts(
    service: AuditService,
    repository: Mock,
) -> None:
    repository.add.side_effect = (
        lambda audit_log: audit_log
    )

    result = service.register(
        user_id=10,
        action="  UPDATE  ",
        module="  PURCHASE  ",
        entity_type="  Purchase  ",
        entity_id=20,
        description=(
            "  Compra alterada.  "
        ),
        justification=(
            "  Correção necessária.  "
        ),
    )

    assert result.action == "UPDATE"
    assert result.module == "PURCHASE"
    assert result.entity_type == "Purchase"

    assert result.description == (
        "Compra alterada."
    )

    assert result.justification == (
        "Correção necessária."
    )


def test_should_convert_blank_optional_text_to_none(
    service: AuditService,
    repository: Mock,
) -> None:
    repository.add.side_effect = (
        lambda audit_log: audit_log
    )

    result = service.register(
        user_id=10,
        action="CREATE",
        module="PURCHASE",
        entity_type="Purchase",
        entity_id=20,
        description="   ",
        justification="   ",
    )

    assert result.description is None
    assert result.justification is None


def test_should_serialize_old_and_new_values(
    service: AuditService,
    repository: Mock,
) -> None:
    repository.add.side_effect = (
        lambda audit_log: audit_log
    )

    result = service.register(
        user_id=10,
        action="UPDATE",
        module="PURCHASE",
        entity_type="Purchase",
        entity_id=20,
        old_values={
            "status": "PENDING",
            "notes": None,
        },
        new_values={
            "status": "RECEIVED",
            "notes": "Recebida.",
        },
        justification=(
            "Nota fiscal recebida."
        ),
    )

    assert json.loads(
        result.old_values
    ) == {
        "status": "PENDING",
        "notes": None,
    }

    assert json.loads(
        result.new_values
    ) == {
        "status": "RECEIVED",
        "notes": "Recebida.",
    }


@pytest.mark.parametrize(
    "user_id",
    [
        0,
        -1,
        True,
    ],
)
def test_should_reject_invalid_user_id(
    service: AuditService,
    repository: Mock,
    user_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário "
            "da auditoria deve ser maior que zero."
        ),
    ):
        service.register(
            user_id=user_id,
            action="CREATE",
            module="PURCHASE",
            entity_type="Purchase",
            entity_id=20,
        )

    repository.add.assert_not_called()


@pytest.mark.parametrize(
    "entity_id",
    [
        0,
        -1,
        True,
    ],
)
def test_should_reject_invalid_entity_id(
    service: AuditService,
    repository: Mock,
    entity_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da entidade "
            "auditada deve ser maior que zero."
        ),
    ):
        service.register(
            user_id=10,
            action="CREATE",
            module="PURCHASE",
            entity_type="Purchase",
            entity_id=entity_id,
        )

    repository.add.assert_not_called()


@pytest.mark.parametrize(
    (
        "field",
        "value",
        "message",
    ),
    [
        (
            "action",
            "",
            "A ação da auditoria é obrigatória.",
        ),
        (
            "action",
            "   ",
            "A ação da auditoria é obrigatória.",
        ),
        (
            "module",
            "",
            "O módulo da auditoria é obrigatório.",
        ),
        (
            "module",
            "   ",
            "O módulo da auditoria é obrigatório.",
        ),
        (
            "entity_type",
            "",
            (
                "O tipo da entidade auditada "
                "é obrigatório."
            ),
        ),
        (
            "entity_type",
            "   ",
            (
                "O tipo da entidade auditada "
                "é obrigatório."
            ),
        ),
    ],
)
def test_should_reject_required_blank_text(
    service: AuditService,
    repository: Mock,
    field: str,
    value: str,
    message: str,
) -> None:
    data = {
        "user_id": 10,
        "action": "CREATE",
        "module": "PURCHASE",
        "entity_type": "Purchase",
        "entity_id": 20,
    }

    data[field] = value

    with pytest.raises(
        ValueError,
        match=message,
    ):
        service.register(
            **data
        )

    repository.add.assert_not_called()


def test_should_get_audit_log_by_id(
    service: AuditService,
    repository: Mock,
) -> None:
    audit_log = create_audit_log()

    repository.get_by_id.return_value = (
        audit_log
    )

    result = service.get_by_id(
        1
    )

    assert result == audit_log

    repository.get_by_id.assert_called_once_with(
        1
    )


def test_should_raise_when_audit_log_is_not_found(
    service: AuditService,
    repository: Mock,
) -> None:
    repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match=(
            "Registro de auditoria não encontrado."
        ),
    ):
        service.get_by_id(
            999
        )

    repository.get_by_id.assert_called_once_with(
        999
    )


def test_should_list_audit_logs_by_user(
    service: AuditService,
    repository: Mock,
) -> None:
    audit_logs = [
        create_audit_log(
            audit_log_id=1,
        ),
        create_audit_log(
            audit_log_id=2,
        ),
    ]

    repository.list_by_user.return_value = (
        audit_logs
    )

    result = service.list_by_user(
        10
    )

    assert result == audit_logs

    repository.list_by_user.assert_called_once_with(
        10
    )


def test_should_list_audit_logs_by_entity(
    service: AuditService,
    repository: Mock,
) -> None:
    audit_logs = [
        create_audit_log()
    ]

    repository.list_by_entity.return_value = (
        audit_logs
    )

    result = service.list_by_entity(
        entity_type=" Purchase ",
        entity_id=20,
    )

    assert result == audit_logs

    repository.list_by_entity.assert_called_once_with(
        "Purchase",
        20,
    )


def test_should_list_audit_logs_by_module(
    service: AuditService,
    repository: Mock,
) -> None:
    audit_logs = [
        create_audit_log()
    ]

    repository.list_by_module.return_value = (
        audit_logs
    )

    result = service.list_by_module(
        " PURCHASE "
    )

    assert result == audit_logs

    repository.list_by_module.assert_called_once_with(
        "PURCHASE"
    )


@pytest.mark.parametrize(
    "audit_log_id",
    [
        0,
        -1,
        True,
    ],
)
def test_should_reject_invalid_audit_log_id(
    service: AuditService,
    repository: Mock,
    audit_log_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da auditoria "
            "deve ser maior que zero."
        ),
    ):
        service.get_by_id(
            audit_log_id
        )

    repository.get_by_id.assert_not_called()