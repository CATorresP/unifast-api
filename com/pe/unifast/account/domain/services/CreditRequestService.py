from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.CreditRequestRepository import CreditRequestRepository
from ...schemas.CreditRequestDto import CreditRequestDTO
from ...schemas.CreditRequestResponseDto import CreditRequesResponseDTO
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class CreditRequestService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = CreditRequestRepository(db)
        self.mapper = Mapper()
    
    def get_credit_request_by_id(self, credit_request_id: int):
        credit_request = self.repository.get_credit_request_by_id(credit_request_id)
        if credit_request is None:
            raise HTTPException(status_code=404, detail="Credit Request not found")
        return self.mapper.entity_to_response_dto(credit_request)
    
    def get_all_credit_request(self):
        credit_requests = self.repository.get_all_credit_request()
        return self.mapper.entity_to_response_dto(credit_requests)
    
    def update_credit_request_by_id(self, credit_request_id:int, credit_request_dto:CreditRequestDTO):
        credit_request = self.repository.get_credit_request_by_id(credit_request_id)
        if credit_request is None:
            raise HTTPException(status_code=404, detail="Credit Request not found")
        credit_request = self.mapper.dto_to_entity(credit_request_dto)
        credit_request = self.repository.update_credit_request_by_id(credit_request_id, credit_request)
        return self.mapper.entity_to_response_dto(credit_request)
    
    def delete_credit_request_by_id(self, credit_request_id:int):
        credit_request = self.repository.get_credit_request_by_id(credit_request_id)
        if credit_request is None:
            raise HTTPException(status_code=404, detail="Credit Request not found")
        self.repository.delete_credit_request_by_id(credit_request_id)
        return
    
    def create_credit_request(self, credit_request_dto:CreditRequestDTO):
        credit_request = self.mapper.dto_to_entity(credit_request_dto)
        credit_request = self.repository.create_credit_request(credit_request)
        return self.mapper.entity_to_response_dto(credit_request)