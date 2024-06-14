#sale schema dto
from pydantic import BaseModel

class SaleDTO(BaseModel):
    shopSaleID: int
    productID: int
    discountType: str
    discountValue: float
    price : float
    creationDatetime: str
    saleStatus: str
