from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseDb
from typing import Optional


class FruitsInvoice(BaseDb):
    __tablename__ = "fruits_invoice"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    fk_invoice_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("invoices.id", ondelete="SET NULL"), nullable=True
    )
    fk_fruit_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fruits.id", ondelete="SET NULL"), nullable=True
    )

    def __repr__(self):
        return f"<Fruit(id={self.id}, quantity={self.quantity}, total_amount={total_amount})>"
