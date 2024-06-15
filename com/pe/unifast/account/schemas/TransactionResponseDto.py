from pydantic import BaseModel
from datetime import datetime
from xml.etree.ElementTree import XML


class TransactionResponseDto(BaseModel):
    transactionID: int
    accountID: int
    subjectAccountID: int
    subjectSupplierID: int
    realizationDatetime: datetime
    amount: float
    transactionType: str
    message: str
    eBill: XML
    class Config:
        from_attributes = True
        #orm_mode = True
    