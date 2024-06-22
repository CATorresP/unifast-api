from pydantic import BaseModel
from datetime import datetime





class AccountResponseDto(BaseModel):
    name: str
    email: str
    phoneNumber: str
    dni: str
    hashedPin: str
    accountID: int
    creditID: int
    profileImgPath: str
    accountType: str
    debitCardAuthToken: str
    dailyTransferLimit: float
    dailyReceptionLimit: float
    registerDatetime: datetime
    accountStatus: str

    class Config:
        #orm_mode = True
        from_attributes = True
