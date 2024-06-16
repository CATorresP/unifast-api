from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.LoanInstallmentRepository import LoanInstallmentRepository
from ...schemas.LoantInstallmentDto import LoanInstallmentDto
from ...schemas.LoanInstallmentResponseDto import LoanInstallmentResponseDto
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class LoanInstallmentService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = LoanInstallmentRepository(db)
        self.mapper = Mapper()
    
    def get_loan_installment_by_id(self, loan_installment_id: int):
        loan_installment = self.repository.get_loan_installment_by_id(loan_installment_id)
        if loan_installment is None:
            raise HTTPException(status_code=404, detail="Loan Installment not found")
        return self.mapper.entity_to_response_dto(loan_installment)
    
    def get_all_loan_installment(self):
        loan_installments = self.repository.get_all_loan_installment()
        return self.mapper.list_entity_to_list_response_dto(loan_installments)
    
    def update_loan_installment_by_id(self, loan_installment_id:int, loan_installment_dto:LoanInstallmentDto):
        loan_installment = self.repository.get_loan_installment_by_id(loan_installment_id)
        if loan_installment is None:
            raise HTTPException(status_code=404, detail="Loan Installment not found")
        loan_installment = self.mapper.dto_to_entity(loan_installment_dto)
        loan_installment = self.repository.update_loan_installment_by_id(loan_installment_id, loan_installment)
        return self.mapper.entity_to_response_dto(loan_installment)
    
    def delete_loan_installment_by_id(self, loan_installment_id:int):
        loan_installment = self.repository.get_loan_installment_by_id(loan_installment_id)
        if loan_installment is None:
            raise HTTPException(status_code=404, detail="Loan Installment not found")
        self.repository.delete_loan_installment_by_id(loan_installment_id)
        return
    
    def create_loan_installment(self, loan_installment_dto:LoanInstallmentDto):
        loan_installment = self.mapper.dto_to_entity(loan_installment_dto)
        loan_installment = self.repository.create_loan_installment(loan_installment)
        return self.mapper.entity_to_response_dto(loan_installment)
    

