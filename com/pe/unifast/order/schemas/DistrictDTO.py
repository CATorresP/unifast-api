from pydantic import BaseModel
from datetime import datetime

class DistrictDTO(BaseModel):
    districtID: int
    name: str