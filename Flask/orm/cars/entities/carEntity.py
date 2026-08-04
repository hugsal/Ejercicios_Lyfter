from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseDb
from typing import Optional


class Car(BaseDb):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    fk_user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    user: Mapped[Optional["User"]] = relationship("User", back_populates="cars")

    def __repr__(self):
        return f"<Car(id={self.id}, brand='{self.brand}', model='{self.model}', year={self.year}, fk_user_id={self.fk_user_id})>"
