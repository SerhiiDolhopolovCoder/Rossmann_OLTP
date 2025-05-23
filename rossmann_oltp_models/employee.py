from datetime import date

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp_models import SyncBase


class Employee(SyncBase):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("shops.shop_id"), nullable=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[date]
    hire_date: Mapped[date]
    phone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(320))
    role: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(100))
    salary: Mapped[float]

    
    shop = relationship('Shop', back_populates="employees")