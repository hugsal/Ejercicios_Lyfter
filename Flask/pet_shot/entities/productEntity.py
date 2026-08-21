from datetime import date
from sqlalchemy import String, Float, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseDb
from typing import Optional


class Product(BaseDb):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    admission_date: Mapped[date] = mapped_column(
        Date, nullable=False, default=date.today
    )

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})>"
