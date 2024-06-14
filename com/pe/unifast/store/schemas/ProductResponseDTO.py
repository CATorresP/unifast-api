from pydantic import BaseModel
from datetime import datetime

class ProductDTO(BaseModel):
    productID: int
    brandID: int
    supplierID: int
    name : str
    refecenImgPath: str
    creationDatetime: datetime
    productStatus: str
    class Config:
        from_attributes = True
        #orm_mode = True