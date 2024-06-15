from sqlalchemy import Boolean
from config.database import Base
from sqlalchemy.dialects.mssql import MONEY
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Credit(Base):
    __tablename__ = 'Credit'

    creditID: Mapped[int] = mapped_column(primary_key=True)
    ownedCredit: Mapped[MONEY] = mapped_column(MONEY)
    preApprovedRequest: Mapped[bool] = mapped_column(Boolean)
    prevInstallmentOverdue: Mapped[bool] = mapped_column(Boolean)
    creditEligibility: Mapped[bool] = mapped_column(Boolean)

    creditRequests: Mapped[list["CreditRequest"]] = relationship( back_populates="credit")
    account: Mapped["Account"] = relationship(back_populates="credit")

