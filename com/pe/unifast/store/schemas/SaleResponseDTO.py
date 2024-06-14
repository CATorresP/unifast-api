from pydantic import BaseModel
from datetime import datetime

class SaleResponseDTO(BaseModel):
    shopSaleID: int
    productID: int
    discountType: str
    discountValue: float
    price : float
    creationDatetime: str
    saleStatus: str
    class Config:
        from_attributes = True
        #orm_mode = True