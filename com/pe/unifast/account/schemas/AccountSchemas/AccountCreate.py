from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    email: str
    phoneNumber: str
    dni: str
    pin: str
    
    class Config:
        #orm_mode = True
        from_attributes = True
    