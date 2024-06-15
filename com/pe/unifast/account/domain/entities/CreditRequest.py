from config.database import Base
from sqlalchemy import ForeignKey, String, DateTime, Boolean, Integer
from sqlalchemy.dialects.mssql import MONEY, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CreditRequest(Base):
    __tablename__ = 'CreditRequest'
    creditRequestID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creditID : Mapped[int] = mapped_column(ForeignKey("Credit.creditID"))
    requestDate: Mapped[DateTime] = mapped_column(DATETIME)
    paymentType: Mapped[str] = mapped_column(String(10))
    requestStatus: Mapped[str] = mapped_column(String(10))

    installments: Mapped[list["LoanInstallment"]] = relationship("LoanInstallment", back_populates="creditRequest")
    credit: Mapped["Credit"] = relationship("Credit", back_populates="creditRequests")

    