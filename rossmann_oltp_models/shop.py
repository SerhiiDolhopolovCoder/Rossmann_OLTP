from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rossmann_oltp_models import Base


class Shop(Base):
    __tablename__ = "shops"

    shop_id: Mapped[int] = mapped_column(primary_key=True)
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey("cities.city_id"))
    address: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(100))
    
    employees = relationship("Employee", back_populates="shop")
    products = relationship("ShopProduct", back_populates="shop")
    terminals = relationship("Terminal", back_populates="shop")
    city = relationship("City", back_populates="shops")