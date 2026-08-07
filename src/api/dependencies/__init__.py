"""Dependências compartilhadas da API."""

from src.api.dependencies.auth import (
    CurrentUserDependency,
    get_current_user,
)
from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
    AdminOrSellerUserDependency,
    AdminUserDependency,
    OperationalUserDependency,
    ROLE_ADMIN,
    ROLE_BUYER,
    ROLE_SELLER,
    require_roles,
)


__all__ = [
    "AdminOrBuyerUserDependency",
    "AdminOrSellerUserDependency",
    "AdminUserDependency",
    "CurrentUserDependency",
    "OperationalUserDependency",
    "ROLE_ADMIN",
    "ROLE_BUYER",
    "ROLE_SELLER",
    "get_current_user",
    "require_roles",
]