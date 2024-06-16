from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.TransactionRepository import TransactionRepository
from ...schemas.TransactionDto import TransactionDto
from ...schemas.TransactionResponseDto import TransactionResponseDto
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class TransactionService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = TransactionRepository(db)
        self.mapper = Mapper()

    def get_transaction_by_id(self, transaction_id: int):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return self.mapper.entity_to_response_dto(transaction)
    
    def get_all_transaction(self):
        transactions = self.repository.get_all_transaction()
        return self.mapper.list_entity_to_list_dto(transactions)
    
    def update_transaction_by_id(self, transaction_id:int, transaction_dto:TransactionDto):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        transaction = self.mapper.dto_to_entity(transaction_dto)
        transaction = self.repository.update_transaction_by_id(transaction_id, transaction)
        return self.mapper.entity_to_response_dto(transaction)
    
    def delete_transaction_by_id(self, transaction_id:int):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        self.repository.delete_transaction_by_id(transaction_id)
        return

    def create_transaction(self, transaction_dto:TransactionDto):
        transaction = self.mapper.dto_to_entity(transaction_dto)
        transaction = self.repository.create_transaction(transaction)
        return self.mapper.entity_to_response_dto(transaction)
    