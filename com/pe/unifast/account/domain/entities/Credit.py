from sqlalchemy import Boolean
from config.database import Base
from sqlalchemy.dialects.mssql import MONEY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Credit(Base):
    __tablename__ = 'Credit'

    creditID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ownedCredit: Mapped[MONEY] = mapped_column(MONEY, default=5000.00)
    preApprovedRequest: Mapped[bool] = mapped_column(Boolean, default=True)
    prevInstallmentOverdue: Mapped[bool] = mapped_column(Boolean, default=True)
    creditEligibility: Mapped[bool] = mapped_column(Boolean,default=True)

    creditRequests: Mapped[list["CreditRequest"]] = relationship("CreditRequest", back_populates="credit")
    account: Mapped["Account"] = relationship("Account",back_populates="credit")

