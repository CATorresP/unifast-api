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


class LoanInstallmentService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = TransactionRepository(db)
        self.mapper = Mapper()
