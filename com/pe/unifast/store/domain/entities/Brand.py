from config.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Brand(Base):
    __tablename__ = 'Brand'
    brandID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String(30))

    products: Mapped[list["Product"]] = relationship("Product", back_populates="brand")

#class Brand(Base):