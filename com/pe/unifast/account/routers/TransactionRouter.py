from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session


from ..schemas.TransactionResponseDto import TransactionResponseDto
from ..schemas.TransactionDto import TransactionDto
from ..domain.services.TransactionService import TransactionService

transactionRouter = APIRouter()
transactionRouter.prefix = "/transaction"

@transactionRouter.get("/transaction/{transactionId}",response_model=TransactionResponseDto)
async def get_transaction_by_id(db: Annotated[Session, Depends(get_db_session)], transactionId: int):
    transactionService = TransactionService(db)
    transaction_response_dto = transactionService.get_transaction_by_id(transactionId)
    return transaction_response_dto

@transactionRouter.get("/transactions",response_model=list[TransactionResponseDto])
async def get_all_transaction(db: Annotated[Session, Depends(get_db_session)]):
    transactionService = TransactionService(db)
    transaction_response_dto = transactionService.get_all_transaction()
    return transaction_response_dto

@transactionRouter.put("/transaction/{transactionId}",response_model=TransactionResponseDto)
async def update_transaction_by_id(db: Annotated[Session, Depends(get_db_session)], transactionId: int, transactionDto: TransactionDto):
    transactionService = TransactionService(db)
    transaction_response_dto = transactionService.update_transaction_by_id(transactionId, transactionDto)
    return transaction_response_dto

@transactionRouter.delete("/transaction/{transactionId}")
async def delete_transaction_by_id(db: Annotated[Session, Depends(get_db_session)], transactionId: int):
    transactionService = TransactionService(db)
    transactionService.delete_transaction_by_id(transactionId)
    return

@transactionRouter.post("/transaction",response_model=TransactionResponseDto)
async def create_transaction(db: Annotated[Session, Depends(get_db_session)], transactionDto: TransactionDto):
    transactionService = TransactionService(db)
    transaction_response_dto = transactionService.create_transaction(transactionDto)
    return transaction_response_dto
