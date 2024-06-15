from pydantic import BaseModel
from datetime import datetime

class DistrictResponseDTO(BaseModel):
    districtID: int
    name: str
    class Config:
        from_attributes = True
        #orm_mode = True