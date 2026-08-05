from datetime import date
from sqlalchemy import Float, Date, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseDb
from typing import Optional


class Invoice(BaseDb):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    purchase_date: Mapped[date] = mapped_column(
        Date, nullable=False, server_default=func.now()
    )
    fk_user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )

    def __repr__(self):
        return f"<Invoice(id={self.id}, total_amount='{self.total_amount}', purchase_date='{self.purchase_date}')>"
