"""Rotas HTTP da aplicação."""

from src.api.routes.part_route import (
    router as part_router,
)
from src.api.routes.purchase_tracking_route import (
    router as purchase_tracking_router,
)
from src.api.routes.supplier_contact_route import (
    router as supplier_contact_router,
)
from src.api.routes.supplier_route import (
    router as supplier_router,
)


__all__ = [
    "part_router",
    "purchase_tracking_router",
    "supplier_contact_router",
    "supplier_router",
]