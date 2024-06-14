from config.database import Base
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship, ForeignKey

class Product(Base):
    __tablename__ = 'Product'
    productID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    brandID: Mapped[int] = mapped_column(ForeignKey("Brand.brandID"))
    supplierID: Mapped[int] = mapped_column(ForeignKey("Supplier.supplierID"))
    name: Mapped[str] = mapped_column(String(30))
    referenceImgPath: Mapped[str] = mapped_column(String(256))
    rating: Mapped[int] = mapped_column(Integer)
    creationDatetime: Mapped[DateTime] = mapped_column(DateTime)
    productStatus: Mapped[str] = mapped_column(String(10))
    
    brand: Mapped["Brand"] = relationship("Brand", back_populates="products")
    supplier: Mapped["Supplier"] = relationship("Supplier", back_populates="products")