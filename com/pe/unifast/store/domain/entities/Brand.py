from config.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Brand(Base):
    __tablename__ = 'Brand'
    brandID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    def __repr__(self):
        return f"<Brand(brandID={self.brandID}, name={self.name})>"

#class Brand(Base):