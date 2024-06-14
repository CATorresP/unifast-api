from pydantic import BaseModel
from datetime import datetime

class SupplierResponseDTO(BaseModel):
    supplierID: int
    companyName: str
    contactEmail: str
    contactPhone: str
    rating: int
    profileImgPath: str
    deliveryMeanTime: int
    depsitAuthToken: str
    registerDatetime: datetime
    class Config:
        from_attributes = True
        #orm_mode = True
