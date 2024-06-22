from pydantic import BaseModel
from datetime import datetime

class CreditRequestDTO(BaseModel):
    creditID: int
    creditRequestID: int
    requestDate: datetime
    paymentType : str
    requestStatus: str
    
    class Config:
        from_attributes = True
    



