"""Rotas HTTP da aplicação."""

from src.api.routes.customer_return_route import (
    router as customer_return_router,
)
from src.api.routes.outbound_route import (
    router as outbound_router,
)
from src.api.routes.part_route import (
    router as part_router,
)
from src.api.routes.purchase_route import (
    router as purchase_router,
)
from src.api.routes.purchase_tracking_route import (
    router as purchase_tracking_router,
)
from src.api.routes.auth_route import (
    router as auth_router,
)
from src.api.routes.role_route import (
    router as role_router,
)
from src.api.routes.supplier_contact_route import (
    router as supplier_contact_router,
)
from src.api.routes.supplier_return_route import (
    router as supplier_return_router,
)
from src.api.routes.supplier_route import (
    router as supplier_router,
)
from src.api.routes.transfer_route import (
    router as transfer_router,
)
from src.api.routes.transfer_return_route import (
    router as transfer_return_router,
)
from src.api.routes.user_route import (
    router as user_router,
)
from src.api.routes.audit_route import (
    router as audit_router,
)


__all__ = [
    "audit_router",
    "customer_return_router",
    "outbound_router",
    "part_router",
    "purchase_router",
    "purchase_tracking_router",
    "auth_router",
    "role_router",
    "supplier_contact_router",
    "supplier_return_router",
    "supplier_router",
    "transfer_router",
    "transfer_return_router",
    "user_router",
]