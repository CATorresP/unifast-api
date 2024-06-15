from pydantic import BaseModel

class ProvinceDTO(BaseModel):
    provinceID: int
    departmentID: int
    name: str