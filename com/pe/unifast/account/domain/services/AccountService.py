from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.AccountRepository import AccountRepository
from ...schemas.AccountDto import AccountDto
from ...schemas.AccountResponseDto import AccountResponseDto
from ....shared.mapper.Mapper import Mapper
from ....shared.exception.AccountNotFoundResponse import AccountNotFoundResponse

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = AccountRepository(db)
        self.mapper = Mapper()

    
    def create_account(self, dto: AccountDto) -> AccountResponseDto:
        account = self.repository.create_account(dto)
        return self.mapper.entity_to_response_dto(account, AccountResponseDto)
     
    def get_account(self, id: int) -> AccountResponseDto:
        account = self.repository.find_by_id(id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return self.mapper.entity_to_response_dto(account, AccountResponseDto)
    
    def get_all_accounts(self) -> list[AccountResponseDto]:
        accounts = self.repository.get_all()
        if not accounts:
            raise HTTPException(status_code=404, detail="Account not found")
        return self.mapper.list_entity_to_list_response_dto(accounts, AccountResponseDto)
    
    def update_account(self, id: int, dto: AccountDto) -> AccountResponseDto:
        account = self.repository.update_account_by_id(id, dto)
        if not account:
            raise HTTPException(status_code=404, detail="")
        return self.mapper.entity_to_response_dto(account, AccountResponseDto)
    
    def delete_account(self, id: int):

        if not self.repository.find_by_id(id):
            return AccountNotFoundResponse(message="Account not found")

        self.repository.delete_account_by_id(id)
        return AccountNotFoundResponse(message="Account not found")
    
    def get_account_by_phone_number(self, phone_number: str) -> AccountResponseDto:
        account = self.repository.find_by_phone_number(phone_number)
        return self.mapper.entity_to_response_dto(account, AccountResponseDto)
    
    def get_account_by_email(self, email: str) -> AccountResponseDto:
        account = self.repository.find_by_email(email)
        return self.mapper.entity_to_response_dto(account, AccountResponseDto)
    

