from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from ..repositories.AccountRepository import AccountRepository
from ...schemas.AccountSchemas.AccountDto import AccountDto
from ...schemas.AccountSchemas.AccountResponseDto import AccountResponseDto
from ...schemas.AccountSchemas.AccountCreate import AccountCreate
from ..entities.Account import Account
from ..entities.Credit import Credit
from ....shared.mapper.Mapper import Mapper
from ....shared.exception.AccountNotFoundResponse import AccountNotFoundResponse
from ....security.domain.services.AuthService import AuthService
from ...domain.repositories.CreditRepository import CreditRepository

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session
from uuid import uuid4


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = AccountRepository(db)
        self.credit_repository = CreditRepository(db)
        self.security = AuthService(db)

    
    def create_account(self, dto: AccountCreate) -> AccountResponseDto:

        hashedPin=self.security.HashManager.get_password_hash(dto.pin)

        entity=Account()
        entity.name = dto.name
        entity.email = dto.email
        entity.phoneNumber = dto.phoneNumber
        entity.dni = dto.dni
        entity.hashedPin = hashedPin


        credit = Credit()
        credit=self.credit_repository.create_credit()
        entity.creditID = credit.creditID
        entity.debitCardAuthToken = uuid4()

        account = self.repository.create_account(entity)
        response  = AccountResponseDto(**account.__dict__)
        return response
     
    def get_account(self, id: int) -> AccountResponseDto:
        account = self.repository.find_by_id(id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return AccountResponseDto(**account.__dict__)
    
    def get_all_accounts(self) -> list[AccountResponseDto]:
        accounts = self.repository.get_all()
        if not accounts:
            raise HTTPException(status_code=404, detail="Account not found")
        return [AccountResponseDto(**account.__dict__) for account in accounts]
    
    def update_account(self, id: int, dto: AccountDto) -> AccountResponseDto:
        account = self.repository.update_account_by_id(id, dto)
        if not account:
            raise HTTPException(status_code=404, detail="")
        return AccountResponseDto(**account.__dict__)
    
    def delete_account(self, id: int):

        if not self.repository.find_by_id(id):
            return AccountNotFoundResponse(message="Account not found")

        self.repository.delete_account_by_id(id)
        return 
    
    def get_account_by_phone_number(self, phone_number: str) -> Optional[AccountResponseDto]:

        account = self.repository.find_by_phone_number(phone_number)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        return AccountResponseDto(**account.__dict__)
    
    def get_account_by_email(self, email: str) -> AccountResponseDto:
        account = self.repository.find_by_email(email)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return AccountResponseDto(**account.__dict__)
    

