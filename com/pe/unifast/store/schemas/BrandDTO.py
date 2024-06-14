from pydantic import BaseModel

class BrandDTO(BaseModel):
    brandID: int
    name: str