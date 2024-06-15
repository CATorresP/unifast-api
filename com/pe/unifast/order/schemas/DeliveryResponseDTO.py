from pydantic import BaseModel
from datetime import datetime

class DeliveryResponseDTO(BaseModel):
    deliveryID: int
    limitDate: datetime
    deliveryDate: datetime
    cost: float
    class Config:
            from_attributes = True
            #orm_mode = True