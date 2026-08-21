from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseDb


class User(BaseDb):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    role: Mapped[str] = mapped_column(String(50), nullable=False, default="client")
    user_name: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', role='{self.role}', user_name='{self.user_name}')>"
