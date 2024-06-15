from pydantic import BaseModel
from datetime import datetime
from xml.etree.ElementTree import XML

class TransactionDto(BaseModel):
    transactionID: int
    accountID: int
    subjectAccountID: int
    subjectSupplierID: int
    realizationDatetime: datetime
    amount: float
    transactionType: str
    message: str
    eBill: XML