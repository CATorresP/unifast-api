from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.LoanInstallmentResponseDto import LoanInstallmentResponseDto
from ..schemas.LoantInstallmentDto import  LoanInstallmentDto
from ..domain.services.LoanInstallmentService import LoanInstallmentService


loanInstallmentRouter = APIRouter()
loanInstallmentRouter.prefix = "/loanInstallment"

@loanInstallmentRouter.get("/loanInstallment/{loanInstallmentId}",response_model=LoanInstallmentResponseDto)
async def get_loan_installment_by_id(db: Annotated[Session, Depends(get_db_session)], loanInstallmentId: int):
    loanInstallmentService = LoanInstallmentService(db)
    loan_installment_response_dto = loanInstallmentService.get_loan_installment_by_id(loanInstallmentId)
    return loan_installment_response_dto

@loanInstallmentRouter.get("/loanInstallments",response_model=list[LoanInstallmentResponseDto])
async def get_all_loan_installment(db: Annotated[Session, Depends(get_db_session)]):
    loanInstallmentService = LoanInstallmentService(db)
    loan_installment_response_dto = loanInstallmentService.get_all_loan_installment()
    return loan_installment_response_dto

@loanInstallmentRouter.put("/loanInstallment/{loanInstallmentId}",response_model=LoanInstallmentResponseDto)
async def update_loan_installment_by_id(db: Annotated[Session, Depends(get_db_session)], loanInstallmentId: int, loanInstallmentDto: LoanInstallmentDto):
    loanInstallmentService = LoanInstallmentService(db)
    loan_installment_response_dto = loanInstallmentService.update_loan_installment_by_id(loanInstallmentId, loanInstallmentDto)
    return loan_installment_response_dto

@loanInstallmentRouter.delete("/loanInstallment/{loanInstallmentId}")
async def delete_loan_installment_by_id(db: Annotated[Session, Depends(get_db_session)], loanInstallmentId: int):
    loanInstallmentService = LoanInstallmentService(db)
    loanInstallmentService.delete_loan_installment_by_id(loanInstallmentId)
    return

@loanInstallmentRouter.post("/loanInstallment",response_model=LoanInstallmentResponseDto)
async def create_loan_installment(db: Annotated[Session, Depends(get_db_session)], loanInstallmentDto: LoanInstallmentDto):
    loanInstallmentService = LoanInstallmentService(db)
    loan_installment_response_dto = loanInstallmentService.create_loan_installment(loanInstallmentDto)
    return loan_installment_response_dto