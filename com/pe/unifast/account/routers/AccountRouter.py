from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from com.pe.unifast.account.schemas.AccountResponseDto import AccountResponseDto
from com.pe.unifast.account.schemas.AccountDto import AccountDto
from com.pe.unifast.account.domain.services.AccountService import AccountService
from config.oauth2 import oauth2_scheme

account_router = APIRouter()
account_router.prefix = "/account"



@account_router.get("/account/{accountId}",response_model=AccountResponseDto)
async def get_account_by_id(accountId:int, db: Annotated[Session, Depends(get_db_session)]):
    accountService = AccountService(db)
    account_response_dto = accountService.get_account(accountId)
    return account_response_dto

@account_router.get("/accounts",response_model=list[AccountResponseDto])
async def get_all_accounts(db: Annotated[Session, Depends(get_db_session)]):
    accountService = AccountService(db)
    account_response_dto = accountService.get_all_accounts()
    return account_response_dto