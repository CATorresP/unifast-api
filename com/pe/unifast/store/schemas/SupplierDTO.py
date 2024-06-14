from pydantic import BaseModel
from datetime import datetime

class SupplierDTO(BaseModel):
    supplierID: int
    companyName: str
    contactEmail: str
    contactPhone: str
    rating: int
    deliveryMeanTime: int
    depsitAuthToken: str
    registerDatetime: datetime
    #credit: CreditDto