from config.database import Base
from sqlalchemy import Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import MONEY

class OrderItem(Base):
    __tablename__ = 'OrderItem'
    orderID: Mapped[Integer] = mapped_column("orderID",ForeignKey("Order.orderID"),primary_key=True )
    productID: Mapped[Integer] = mapped_column("productID",ForeignKey("Product.productID"),primary_key=True)
    productUnits: Mapped[Integer] = mapped_column("productUnits",Integer)
    price : Mapped[MONEY] = mapped_column("price",MONEY)

    order: Mapped["Order"] = relationship("Order", back_populates="orderItem")
    product: Mapped["Product"] = relationship("Product", back_populates="orderItem")