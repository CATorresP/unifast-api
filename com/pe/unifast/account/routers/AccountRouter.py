from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from com.pe.unifast.account.domain.repositories.AccountRepository import AccountRepository
from com.pe.unifast.account.schemas.AccountResponseDto import AccountResponseDto
from config.database import logger
from dependencies import get_db_session

account_router = APIRouter()


@account_router.get("/account/")
async def root(db: Annotated[Session, Depends(get_db_session)]):
    account_repository = AccountRepository(db)
    account = account_repository.find_by_id(3)
    logger.info(f"{account.accountID}, {account.phoneNumber}")

    if account is None:
        raise HTTPException(status_code=404, detail="Item not found")
    account_response_dto = AccountResponseDto.from_orm(account)
    return account_response_dto
