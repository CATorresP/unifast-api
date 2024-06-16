from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.CreditRequestResponseDto import CreditRequesResponseDTO
from ..schemas.CreditRequestDto import CreditRequestDTO
from ..domain.services.CreditRequestService import CreditRequestService



creditRequestRouter = APIRouter()
creditRequestRouter.prefix = "/creditRequest"

@creditRequestRouter.get("/creditRequest/{creditRequestId}",response_model=CreditRequesResponseDTO)
async def get_credit_request_by_id(db: Annotated[Session, Depends(get_db_session)], creditRequestId: int):
    creditRequestService = CreditRequestService(db)
    credit_request_response_dto = creditRequestService.get_credit_request_by_id(creditRequestId)
    return credit_request_response_dto

@creditRequestRouter.get("/creditRequests",response_model=list[CreditRequesResponseDTO])
async def get_all_credit_request(db: Annotated[Session, Depends(get_db_session)]):
    creditRequestService = CreditRequestService(db)
    credit_request_response_dto = creditRequestService.get_all_credit_request()
    return credit_request_response_dto

@creditRequestRouter.put("/creditRequest/{creditRequestId}",response_model=CreditRequesResponseDTO)
async def update_credit_request_by_id(db: Annotated[Session, Depends(get_db_session)], creditRequestId: int, creditRequestDTO: CreditRequestDTO):
    creditRequestService = CreditRequestService(db)
    credit_request_response_dto = creditRequestService.update_credit_request_by_id(creditRequestId, creditRequestDTO)
    return credit_request_response_dto

@creditRequestRouter.delete("/creditRequest/{creditRequestId}")
async def delete_credit_request_by_id(db: Annotated[Session, Depends(get_db_session)], creditRequestId: int):
    creditRequestService = CreditRequestService(db)
    creditRequestService.delete_credit_request_by_id(creditRequestId)
    return

@creditRequestRouter.post("/creditRequest",response_model=CreditRequesResponseDTO)
async def create_credit_request(db: Annotated[Session, Depends(get_db_session)], creditRequestDTO: CreditRequestDTO):
    creditRequestService = CreditRequestService(db)
    credit_request_response_dto = creditRequestService.create_credit_request(creditRequestDTO)
    return credit_request_response_dto