from pydantic import BaseModel
from datetime import datetime

from com.pe.unifast.account.schemas.CreditResponseDto import CreditResponseDto


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
    # credit: CreditResponseDto

    class Config:
        orm_mode = True
        from_attributes = True
