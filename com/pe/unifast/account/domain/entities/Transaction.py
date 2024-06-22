from config.database import Base
from sqlalchemy import String, DateTime, Integer,ForeignKey,LargeBinary
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import MONEY,XML

from datetime import datetime 

class Transaction(Base):
    __tablename__ = 'Transaction'
    transactionID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    accountID: Mapped[int] = mapped_column(ForeignKey("Account.accountID"),nullable=False)
    subjectAccountID: Mapped[int] = mapped_column(ForeignKey("Account.accountID"),nullable=True)
    subjectSupplierID: Mapped[int] = mapped_column(ForeignKey("Supplier.supplierID"),nullable=True)
    realizationDatetime: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    amount: Mapped[MONEY] = mapped_column(MONEY)
    transactionType: Mapped[str] = mapped_column(String(10))
    message: Mapped[str] = mapped_column(String(256))
    eBillSign: Mapped[LargeBinary] = mapped_column(LargeBinary)
    eBill: Mapped[XML] = mapped_column(XML)

    account: Mapped["Account"] = relationship("Account", back_populates="transaction",foreign_keys="[Transaction.accountID]")
    
    subjectAccount : Mapped["Account"] = relationship("Account", back_populates="transactionSubject",foreign_keys="[Transaction.subjectAccountID]")
    
    supplier: Mapped["Supplier"] = relationship("Supplier", back_populates="transactions",)