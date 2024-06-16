from pydantic import BaseModel
from datetime import datetime




class AccountResponseDto(BaseModel):
    accountID: int
    creditID: int
    name: str
    email: str
    phoneNumber: str
    profileImgPath: str
    accountType: str
    dni: str
    hashedPin: str
    debitCardAuthToken: str
    dailyTransferLimit: float
    dailyReceptionLimit: float
    registerDatetime: datetime
    accountStatus: str

    class Config:
        #orm_mode = True
        from_attributes = True
