from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.CreditRepository import CreditRepository
from ...schemas.CreditSchemas.CreditDto import CreditDto
from ...schemas.CreditSchemas.CreditResponseDto import CreditResponseDto


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class CreditService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = CreditRepository(db)

    def get_credit_by_id(self, credit_id: int):
        credit = self.repository.find_by_id(credit_id)
        if credit is None:
            raise HTTPException(status_code=404, detail="Credit not found")
        return CreditResponseDto(**credit.__dict__)
    
    def get_all_credit(self):
        credits = self.repository.get_all()
        return [CreditResponseDto(**credit.__dict__) for credit in credits]
    
    def update_credit_by_id(self, credit_id:int, credit_dto:CreditDto):
        credit = self.repository.find_by_id(credit_id)
        if credit is None:
            raise HTTPException(status_code=404, detail="Credit not found")
       
        credit = self.repository.update_credit_by_id(credit_id, credit_dto)
        return CreditResponseDto(**credit.__dict__)
    
    def delete_credit_by_id(self, credit_id:int):
        credit = self.repository.get_credit_by_id(credit_id)
        if credit is None:
            raise HTTPException(status_code=404, detail="Credit not found")
        self.repository.delete_credit_by_id(credit_id)
        return 
    
    def create_credit(self):
        credit = self.repository.create_credit()
        return CreditResponseDto(**credit.__dict__)
    
