from pydantic import BaseModel

class ProvinceResponseDTO(BaseModel):
    provinceID: int
    departmentID: int
    name: str
    class Config:
        from_attributes = True
        #orm_mode = True