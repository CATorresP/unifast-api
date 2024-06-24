from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session
from ...security.domain.services.AuthService import AuthService
from config.oauth2 import oauth2_scheme

from ..schemas.CreditSchemas.CreditDto import CreditDto
from ..schemas.CreditSchemas.CreditResponseDto import CreditResponseDto
from ..domain.services.CreditService import CreditService

creditRouter = APIRouter()
creditRouter.prefix = "/credit"

@creditRouter.get("/credit/{creditID}",response_model=CreditResponseDto)
async def get_credit_by_id(db: Annotated[Session, Depends(get_db_session)], creditID: int, token: Annotated[str, Depends(oauth2_scheme)]): 
    authService = AuthService(db)
    creditService = CreditService(db)
    
    token_data  = authService.get_token_data(token)
    credit_response_dto = creditService.get_credit_by_id(creditID)
    return credit_response_dto

@creditRouter.get("/credit",response_model=list[CreditResponseDto])
async def get_all_credit(db: Annotated[Session, Depends(get_db_session)], token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    creditService = CreditService(db)
    
    token_data  = authService.get_token_data(token) 
    credit_response_dto = creditService.get_all_credit()
    return credit_response_dto

@creditRouter.put("/credit/{creditID}",response_model=CreditResponseDto)
async def update_credit_request_by_id(db: Annotated[Session, Depends(get_db_session)], creditID: int, creditDTO: CreditDto, token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    creditService = CreditService(db)
    
    token_data  = authService.get_token_data(token) 
    credit_request_response_dto = creditService.update_credit_by_id(creditID, creditDTO)
    return credit_request_response_dto

@creditRouter.delete("/credit/{creditID}")
async def delete_credit_request_by_id(db: Annotated[Session, Depends(get_db_session)], creditID: int, token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    creditService = CreditService(db)
    
    token_data  = authService.get_token_data(token) 
    creditService.delete_credit_by_id(creditID)
    return

@creditRouter.post("/credit",response_model=CreditResponseDto)
async def create_credit_request(db: Annotated[Session, Depends(get_db_session)], creditRequestDTO: CreditDto, token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    creditService = CreditService(db)
    
    token_data  = authService.get_token_data(token) 
    credit_request_response_dto = creditService.create_credit(creditRequestDTO)
    return credit_request_response_dto
