from src.dtos.purchase_tracking import PurchaseTrackingDTO
from src.queries.purchase_tracking_query import PurchaseTrackingQuery


class PurchaseTrackingService:
    """Ponto de entrada para o acompanhamento consolidado de compras."""

    def __init__(self, query: PurchaseTrackingQuery):
        self.query = query

    def get_purchase_tracking(
        self,
        purchase_id: int,
    ) -> PurchaseTrackingDTO:
        """Retorna o acompanhamento consolidado de uma compra."""

        if purchase_id <= 0:
            raise ValueError(
                "O identificador da compra deve ser maior que zero."
            )

        tracking = self.query.get_by_purchase_id(purchase_id)

        if tracking is None:
            raise ValueError("Compra não encontrada.")

        return tracking