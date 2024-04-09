from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from src.databases.payments import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String, nullable=True, default='Тенге')
