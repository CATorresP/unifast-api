from config.database import Base
from sqlalchemy import String, DateTime, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship



class Product(Base):
    __tablename__ = 'Product'
    productID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    brandID: Mapped[int] = mapped_column(ForeignKey("Brand.brandID"))
    supplierID: Mapped[int] = mapped_column(ForeignKey("Supplier.supplierID"))
    name: Mapped[String] = mapped_column(String(30))
    referenceImgPath: Mapped[int] = mapped_column(String(256))
    rating: Mapped[int] = mapped_column(Integer)
    creationDatetime: Mapped[DateTime] = mapped_column(DateTime)
    productStatus: Mapped[String] = mapped_column(String(10))
    
    brand: Mapped["Brand"] = relationship("Brand", back_populates="products")
    supplier: Mapped["Supplier"] = relationship("Supplier", back_populates="products")
    sales: Mapped[list["Sale"]] = relationship("Sale", back_populates="product")

    productCategories: Mapped[list["ProductCategories"]] = relationship("ProductCategories", back_populates="product")

    orderItem: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="product")
