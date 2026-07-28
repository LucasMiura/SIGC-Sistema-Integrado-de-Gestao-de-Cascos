"""
Data Transfer Objects (DTOs).

Responsável por transportar dados entre as camadas da aplicação,
sem expor diretamente os Models do SQLAlchemy.
"""

from src.dtos.purchase_tracking_dto import PurchaseTrackingDTO

__all__ = [
    "PurchaseTrackingDTO",
]