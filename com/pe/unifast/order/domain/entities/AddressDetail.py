from config.database import Base
from sqlalchemy import String, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class AddressDetail(Base):
    __tablename__ = 'AddressDetail'
    addressID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    districtID: Mapped[int] = mapped_column(Integer, ForeignKey("District.districtID"))
    address: Mapped[str] = mapped_column(String(100))
    blockNumber: Mapped[int] = mapped_column(Integer)
    reference : Mapped[str] = mapped_column(String(100))

    district: Mapped["District"] = relationship("District", back_populates="addresses")
    order: Mapped[list["Order"]] = relationship("Order", back_populates="addressDetail")