from pydantic import BaseModel
from datetime import datetime

class DeliveryDTO(BaseModel):
    deliveryID: int
    limitDate: datetime
    deliveryDate: datetime
    cost: float

