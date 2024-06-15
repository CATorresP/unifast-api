from config.database import Base
from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import MONEY


class Sale(Base):
    __tablename__ = 'Sale'
    shopSaleID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    productID: Mapped[int] = mapped_column(ForeignKey("Product.productID"))
    percentage: Mapped[int] = mapped_column(Integer)
    discountType: Mapped[String] = mapped_column(String(10))
    discountValue: Mapped[MONEY] = mapped_column(MONEY)
    price : Mapped[MONEY] = mapped_column(MONEY)
    creationDatetime: Mapped[DateTime] = mapped_column(DateTime)
    saleStatus: Mapped[String] = mapped_column(String(10))
    
    product: Mapped["Product"] = relationship("Product", back_populates="sales")