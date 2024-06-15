from pydantic import BaseModel
from datetime import datetime

class OrderResponseDTO(BaseModel):
    orderID: int
    accountID: int
    addressID: int
    deliveryID: int
    indications: str
    relizationDatetime: datetime
    orderStatus: str
    class Config:
        from_attributes = True
        #orm_mode = True
