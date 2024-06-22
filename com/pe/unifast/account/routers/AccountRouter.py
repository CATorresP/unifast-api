from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from com.pe.unifast.account.schemas.AccountSchemas.AccountResponseDto import AccountResponseDto
from com.pe.unifast.account.schemas.AccountSchemas.AccountDto import AccountDto
from com.pe.unifast.account.schemas.AccountSchemas.AccountCreate import AccountCreate


from com.pe.unifast.account.domain.services.AccountService import AccountService
from com.pe.unifast.security.domain.services.AuthService import AuthService
from config.oauth2 import oauth2_scheme

account_router = APIRouter()
account_router.prefix = "/account"


@account_router.get("/account",response_model=AccountResponseDto)
async def get_account_by_id(db: Annotated[Session, Depends(get_db_session)],token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    accountService = AccountService(db)
    
    token_data  = authService.get_token_data(token)

    account_response_dto = accountService.get_account(token_data.accountID)
    return account_response_dto

@account_router.get("/accounts",response_model=list[AccountResponseDto])
async def get_all_accounts(db: Annotated[Session, Depends(get_db_session)], token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    accountService = AccountService(db)
    
    token_data  = authService.get_token_data(token)
    account_response_dto = accountService.get_all_accounts()
    return account_response_dto

@account_router.put("/account",response_model=AccountResponseDto)
async def update_account_by_id(accountDto: AccountDto, db: Annotated[Session, Depends(get_db_session)], token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    accountService = AccountService(db)
    token_data  = authService.get_token_data(token)
    account_response_dto = accountService.update_account(token_data.accountID, accountDto)
    return account_response_dto

@account_router.delete("/account")
async def delete_account_by_id(db: Annotated[Session, Depends(get_db_session)], token: Annotated[str, Depends(oauth2_scheme)]):
    authService = AuthService(db)
    accountService = AccountService(db)
    token_data  = authService.get_token_data(token)
    accountService.delete_account(token_data.accountID)
    return

@account_router.post("/account",response_model=AccountResponseDto)
async def create_account(db: Annotated[Session, Depends(get_db_session)], accountDto: AccountCreate):

    accountService = AccountService(db)
    account_response_dto = accountService.create_account(accountDto)
    return account_response_dto
