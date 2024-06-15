from config.database import Base
from sqlalchemy import String, Integer,ForeignKey,DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import MONEY

class Delivery(Base):
    __tablename__ = 'Delivery'
    deliveryID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    limitDate: Mapped[DateTime] = mapped_column(DateTime)
    deliveryDate: Mapped[DateTime] = mapped_column(DateTime)
    cost : Mapped[MONEY] = mapped_column(MONEY)

    order: Mapped[list["Order"]] = relationship("Order", back_populates="delivery")