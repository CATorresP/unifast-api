from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session


from ..schemas.TransactionResponseDto import TransactionResponseDto
from ..schemas.TransactionDto import TransactionDto

transactionRouter = APIRouter()
transactionRouter.prefix = "/transaction"