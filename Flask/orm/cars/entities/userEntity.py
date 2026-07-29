from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List 
from database import BaseDb

class User(BaseDb):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    address: Mapped[List["Address"]] = relationship("Address", back_populates="user")
    cars: Mapped[List["Car"]] = relationship("Car", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', user_name='{self.user_name}')>"