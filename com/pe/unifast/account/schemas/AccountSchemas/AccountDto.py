from pydantic import BaseModel
from .AccountCreate import AccountCreate
from datetime import datetime

class AccountDto(BaseModel):
    name: str
    email: str
    phoneNumber: str
    dni: str
    hashedPin: str


    class Config:
        #orm_mode = True
        from_attributes = True
    
