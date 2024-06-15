from config.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class ProductCategories(Base):
    __tablename__ = 'ProductCategories'
    productID: Mapped[int] = mapped_column(ForeignKey("Product.productID"), primary_key=True)
    productCategoryID: Mapped[int] = mapped_column(ForeignKey("ProductCategory.productCategoryID"), primary_key=True)

    product: Mapped["Product"] = relationship("Product", back_populates="productCategories")
    productCategory: Mapped["ProductCategory"] = relationship("ProductCategory", back_populates="productCategories")