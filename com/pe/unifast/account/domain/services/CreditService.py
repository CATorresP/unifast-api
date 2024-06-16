from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.CreditRepository import CreditRepository
from ...schemas.CreditDto import CreditDto
from ...schemas.CreditResponseDto import CreditResponseDto
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class CreditService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = CreditRepository(db)
        self.mapper = Mapper()

    def get_credit_by_id(self, credit_id: int):
        credit = self.repository.get_credit_by_id(credit_id)
        if credit is None:
            raise HTTPException(status_code=404, detail="Credit not found")
        return self.mapper.entity_to_response_dto(credit)
    
    def get_all_credit(self):
        credits = self.repository.get_all_credit()
        return self.mapper.list_entity_to_list_response_dto(credits)
    
    def update_credit_by_id(self, credit_id:int, credit_dto:CreditDto):
        credit = self.repository.get_credit_by_id(credit_id)
        if credit is None:
            raise HTTPException(status_code=404, detail="Credit not found")
        credit = self.mapper.dto_to_entity(credit_dto)
        credit = self.repository.update_credit_by_id(credit_id, credit)
        return self.mapper.entity_to_response_dto(credit)
    
    def delete_credit_by_id(self, credit_id:int):
        credit = self.repository.get_credit_by_id(credit_id)
        if credit is None:
            raise HTTPException(status_code=404, detail="Credit not found")
        self.repository.delete_credit_by_id(credit_id)
        return
    
    def create_credit(self, credit_dto:CreditDto):
        credit = self.mapper.dto_to_entity(credit_dto)
        credit = self.repository.create_credit(credit)
        return self.mapper.entity_to_response_dto(credit)
    
