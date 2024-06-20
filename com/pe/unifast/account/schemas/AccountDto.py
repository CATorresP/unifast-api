from pydantic import BaseModel
from datetime import datetime

class AccountDto(BaseModel):
    accountID: int
    creditID: int
    name: str
    email: str
    phoneNumber: str
    profileImgPath: str
    accountType: str
    dni: str
    pin: str
    debitCardAuthToken: str
    dailyTransferLimit: float
    dailyReceptionLimit: float
    registerDatetime: datetime
    accountStatus: str
    
