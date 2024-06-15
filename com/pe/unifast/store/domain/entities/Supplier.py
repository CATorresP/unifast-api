from config.database import Base
from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime

class Supplier(Base):
    __tablename__ = 'Supplier'
    supplierID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    companyName: Mapped[String] = mapped_column(String(30))
    contactEmail: Mapped[String] = mapped_column(String(30))
    contactPhone: Mapped[String] = mapped_column(String(30))
    rating : Mapped[int] = mapped_column(Integer)
    profileImgPath: Mapped[String] = mapped_column(String(256))
    deliveryMeantime: Mapped[int] = mapped_column(Integer)
    depsitAuthToken: Mapped[String] = mapped_column(String(600))
    registerDatetime: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    
    products: Mapped[list["Product"]] = relationship("Product", back_populates="supplier")
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="supplier")
    #class Supplier(Base):