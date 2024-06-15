from config.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class ProductCategory(Base):
    __tablename__ = 'ProductCategory'
    productCategoryID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    productCategory : Mapped[String] = mapped_column(String(20))

    productCategories: Mapped[list["ProductCategories"]] = relationship("ProductCategories", back_populates="productCategory")