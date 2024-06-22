from pydantic import BaseModel
from datetime import datetime
from xml.etree.ElementTree import XML


class TransactionResponseDto(BaseModel):
    transactionID: int
    accountID: int
    subjectAccountID: int | None
    subjectSupplierID: int | None
    realizationDatetime: datetime
    amount: float
    transactionType: str
    message: str | None
    eBill: str
    eBillSign: str
    class Config:
        from_attributes = True
        #orm_mode = True
    