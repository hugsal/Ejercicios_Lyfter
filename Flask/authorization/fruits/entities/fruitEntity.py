from datetime import date
from sqlalchemy import String, Float, Date, func
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseDb


class Fruit(BaseDb):
    __tablename__ = "fruits"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    admission_date: Mapped[date] = mapped_column(
        Date, nullable=False, server_default=func.now()
    )
    quantity: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Fruit(id={self.id}, name='{self.name}', price='{self.price}', admission_date='{self.admission_date}, quantity={self.quantity}')>"
