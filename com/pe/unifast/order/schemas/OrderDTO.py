from pydantic import BaseModel
from datetime import datetime

class OrderDTO(BaseModel):
    orderID: int
    accountID: int
    addressID: int
    deliveryID: int
    indications: str
    relizationDatetime: datetime
    orderStatus: str
