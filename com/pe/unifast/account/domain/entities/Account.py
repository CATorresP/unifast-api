from config.database import Base
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import MONEY
from com.pe.unifast.account.domain.entities.Credit import Credit


class Account(Base):
    __tablename__ = 'Account'

    accountID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    creditID: Mapped[int] = mapped_column(ForeignKey("Credit.creditID"))
    name: Mapped[str] = mapped_column(String(35))
    email: Mapped[str] = mapped_column(String(64))
    phoneNumber: Mapped[str] = mapped_column(String(9))
    profileImgPath: Mapped[str] = mapped_column(String(256))
    accountType: Mapped[str] = mapped_column(String(20))
    dni: Mapped[str] = mapped_column(String(8))
    hashedPin: Mapped[str] = mapped_column(String(600))
    debitCardAuthToken: Mapped[str] = mapped_column(String(600))
    dailyTransferLimit: Mapped[MONEY] = mapped_column(MONEY)
    dailyReceptionLimit: Mapped[MONEY] = mapped_column(MONEY)
    registerDatetime: Mapped[DateTime] = mapped_column(DateTime)
    accountStatus: Mapped[str] = mapped_column(String(10))

    credit: Mapped[Credit] = relationship(back_populates="account")
    # transaction: Mapped["Transaction"] = relationship(back_populates='account')
    # transactionSubject: Mapped["Transaction"] = relationship(back_populates='account')

