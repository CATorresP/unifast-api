from config.database import Base
from sqlalchemy import ForeignKey, String, DateTime, Boolean
from sqlalchemy.dialects.mssql import MONEY, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from com.pe.unifast.account.domain.entities.Account import Account


class Credit(Base):
    __tablename__ = 'Credit'
    creditID: Mapped[int] = mapped_column(primary_key=True)
    ownedCredit: Mapped[MONEY] = mapped_column(MONEY)
    preApprovedRequest: Mapped[bool] = mapped_column(Boolean)
    prevInstallmentOverdue: Mapped[bool] = mapped_column(Boolean)
    creditEligibility: Mapped[bool] = mapped_column(Boolean)

    account: Mapped["Account"] = relationship("Account", back_populates="credit")

