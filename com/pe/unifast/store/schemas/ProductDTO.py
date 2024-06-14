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