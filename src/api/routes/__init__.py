"""
Rotas HTTP da aplicação.
"""

from src.api.routes.purchase_tracking_route import (
    router as purchase_tracking_router,
)

__all__ = [
    "purchase_tracking_router",
]