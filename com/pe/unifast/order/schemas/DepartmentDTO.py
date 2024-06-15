from pydantic import BaseModel
from datetime import datetime

class DepartmentDTO(BaseModel):
    deparmentID: int
    name: str
