from config.database import Base
from sqlalchemy import String, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'Order'
    orderID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    accountID: Mapped[int] = mapped_column(Integer, ForeignKey("Account.accountID"))
    addressID: Mapped[int] = mapped_column(Integer, ForeignKey("AddressDetail.addressID"))
    deliveryID: Mapped[int] = mapped_column(Integer, ForeignKey("Delivery.deliveryID"))
    indications : Mapped[str] = mapped_column(String(256))
    realizationDatetime: Mapped[str] = mapped_column(String(30))
    orderStatus: Mapped[str] = mapped_column(String(10))

    
    account: Mapped["Account"] = relationship("Account", back_populates="order")
    addressDetail: Mapped["AddressDetail"] = relationship("AddressDetail", back_populates="order")
    delivery: Mapped["Delivery"] = relationship("Delivery", back_populates="order")

    orderItem: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order")
    
