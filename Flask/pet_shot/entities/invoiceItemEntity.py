from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseDb
from typing import Optional


class InvoiceItem(BaseDb):
    __tablename__ = "invoice_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    subtotal: Mapped[float] = mapped_column(Float, nullable=False)
    fk_invoice_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("invoices.id", ondelete="CASCADE"), nullable=True, index=True
    )
    fk_product_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("products.id", ondelete="SET NULL"), nullable=True, index=True
    )

    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="items")
    product = relationship("Product")

    def __repr__(self):
        return f"<InvoiceItem(id={self.id}, invoice_id='{self.fk_invoice_id}', product_id={self.fk_product_id}, quantity={self.quantity}, subtotal={self.subtotal})>"
