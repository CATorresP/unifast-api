from config.database import Base
from sqlalchemy import String, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class District(Base):
    __tablename__ = 'District'
    districtID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    provinceID: Mapped[int] = mapped_column(Integer, ForeignKey("Province.provinceID"))
    name: Mapped[str] = mapped_column(String(30))

    province: Mapped["Province"] = relationship("Province", back_populates="districts")
    addresses: Mapped[list["AddressDetail"]] = relationship("AddressDetail", back_populates="district")