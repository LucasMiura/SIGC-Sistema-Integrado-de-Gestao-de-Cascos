from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.engine import engine_from_config

from src.database.connection import Base, engine

from src.models.part import Part
from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.models.role import Role
from src.models.supplier import Supplier
from src.models.supplier_contact import SupplierContact
from src.models.user import User
from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.customer_return import CustomerReturn
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import CustomerReturnItem
from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem
from src.models.core_movement import CoreMovement
from src.models.audit_log import AuditLog

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executa as migrações em modo offline."""

    context.configure(
        url=str(engine.url),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Executa as migrações utilizando uma conexão existente."""

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações em modo online."""

    with engine.connect() as connection:
        do_run_migrations(connection)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()