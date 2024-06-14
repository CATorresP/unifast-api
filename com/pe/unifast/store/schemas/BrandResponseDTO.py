from pydantic import BaseModel

class BrandResponseDTO(BaseModel):
    brandID: int
    name: str
    class Config:
        #orm_mode = True
        from_attributes = True