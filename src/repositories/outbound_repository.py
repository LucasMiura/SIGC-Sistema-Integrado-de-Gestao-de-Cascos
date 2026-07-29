from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound import Outbound


class OutboundRepository:
    """Responsável pela persistência das saídas."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        outbound_id: int,
    ) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.id == outbound_id
        )

        return self.session.scalar(
            statement
        )

    def get_by_work_order_number(
        self,
        work_order_number: str,
    ) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.work_order_number
            == work_order_number
        )

        return self.session.scalar(
            statement
        )

    def get_by_sales_invoice_number(
        self,
        sales_invoice_number: str,
    ) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.sales_invoice_number
            == sales_invoice_number
        )

        return self.session.scalar(
            statement
        )

    def list_all(
        self,
    ) -> list[Outbound]:
        statement = select(Outbound).order_by(
            Outbound.created_at.desc(),
            Outbound.id.desc(),
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_status(
        self,
        status: str,
    ) -> list[Outbound]:
        statement = (
            select(Outbound)
            .where(
                Outbound.status == status
            )
            .order_by(
                Outbound.created_at.desc(),
                Outbound.id.desc(),
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_destination_type(
        self,
        destination_type: str,
    ) -> list[Outbound]:
        statement = (
            select(Outbound)
            .where(
                Outbound.destination_type
                == destination_type
            )
            .order_by(
                Outbound.created_at.desc(),
                Outbound.id.desc(),
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        outbound: Outbound,
    ) -> Outbound:
        self.session.add(
            outbound
        )

        self.session.flush()

        return outbound

    def save(
        self,
        outbound: Outbound,
    ) -> Outbound:
        self.session.add(
            outbound
        )

        self.session.flush()

        return outbound