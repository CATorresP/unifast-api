from pydantic import BaseModel
from datetime import datetime

class DepartmentResponseDTO(BaseModel):
    deparmentID: int
    name: str
    class Config:
        from_attributes = True
        #orm_mode = True