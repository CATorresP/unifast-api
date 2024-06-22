from pydantic import BaseModel
from datetime import datetime
from xml.etree.ElementTree import XML

class TransactionDto(BaseModel):
    subjectAccountPhoneNumber: str
    amount: float
    transactionType: str
    message: str
    
    class Config:
        from_attributes = True