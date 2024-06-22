from config.database import Base
from sqlalchemy import String, DateTime ,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import MONEY
from datetime import datetime

class Account(Base):
    __tablename__ = 'Account'

    accountID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creditID: Mapped[int] = mapped_column(ForeignKey("Credit.creditID"))
    name: Mapped[str] = mapped_column(String(35))
    email: Mapped[str] = mapped_column(String(64))
    phoneNumber: Mapped[str] = mapped_column(String(9))
    profileImgPath: Mapped[str] = mapped_column(String(256),default="")
    accountType: Mapped[str] = mapped_column(String(20),default="Personal")
    dni: Mapped[str] = mapped_column(String(8))
    hashedPin: Mapped[str] = mapped_column(String(600))
    debitCardAuthToken: Mapped[str] = mapped_column(String(600))
    dailyTransferLimit: Mapped[MONEY] = mapped_column(MONEY,default=5000.00)
    dailyReceptionLimit: Mapped[MONEY] = mapped_column(MONEY,default=5000.00)
    registerDatetime: Mapped[DateTime] = mapped_column(DateTime,default=datetime.now())
    accountStatus: Mapped[str] = mapped_column(String(10),default="Active")

    credit: Mapped["Credit"] = relationship(back_populates="account")
    
    transaction: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="account",foreign_keys="[Transaction.accountID]")
    
    transactionSubject: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="subjectAccount",foreign_keys="[Transaction.subjectAccountID]")
    orders : Mapped[list["Order"]] = relationship("Order", back_populates="account")