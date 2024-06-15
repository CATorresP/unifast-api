from config.database import Base
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Department(Base):
    __tablename__ = 'Department'
    departmentID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    provinces: Mapped[list["Province"]] = relationship("Province", back_populates="department")
