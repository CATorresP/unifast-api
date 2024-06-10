from pydantic import BaseModel
from datetime import datetime

from com.pe.unifast.account.schemas import CreditDto


class AccountDto(BaseModel):
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
    #credit: CreditDto
