from config.database import Base
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import MONEY

class LoanInstallment(Base):
    __tablename__ = 'LoanInstallment'
    installmentID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creditLoanID: Mapped[int] = mapped_column(ForeignKey("CreditRequest.creditRequestID"))
    interest: Mapped[MONEY] = mapped_column(MONEY)
    amount: Mapped[MONEY] = mapped_column(MONEY)
    limitDate: Mapped[DateTime] = mapped_column(DateTime)
    installmentStatus: Mapped[str] = mapped_column(String(10))

    creditRequest: Mapped["CreditRequest"] = relationship("CreditRequest", back_populates="installments")


