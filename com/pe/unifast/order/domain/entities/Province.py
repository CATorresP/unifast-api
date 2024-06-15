from config.database import Base
from sqlalchemy import String, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class Province(Base):
    __tablename__ = 'Province'
    provinceID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    departmentID: Mapped[int] = mapped_column(Integer, ForeignKey("Department.departmentID"))
    name: Mapped[String] = mapped_column(String(30))

    department: Mapped["Department"] = relationship("Department", back_populates="provinces")
    districts: Mapped[list["District"]] = relationship("District", back_populates="province")