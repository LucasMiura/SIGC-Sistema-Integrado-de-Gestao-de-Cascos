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

    def get_purchase_tracking_by_invoice(
        self,
        *,
        supplier_id: int,
        invoice_number: str,
        invoice_series: str | None = None,
    ) -> PurchaseTrackingDTO:
        """
        Retorna o acompanhamento consolidado
        a partir da Nota Fiscal de compra.
        """

        if supplier_id <= 0:
            raise ValueError(
                "O identificador do fornecedor "
                "deve ser maior que zero."
            )

        normalized_invoice_number = (
            invoice_number.strip()
        )

        if not normalized_invoice_number:
            raise ValueError(
                "O número da Nota Fiscal "
                "é obrigatório."
            )

        normalized_invoice_series = None

        if invoice_series is not None:
            normalized_invoice_series = (
                invoice_series.strip()
                or None
            )

        tracking = self.query.get_by_invoice(
            supplier_id=supplier_id,
            invoice_number=(
                normalized_invoice_number
            ),
            invoice_series=(
                normalized_invoice_series
            ),
        )

        if tracking is None:
            raise ValueError(
                "Compra não encontrada."
            )

        return tracking