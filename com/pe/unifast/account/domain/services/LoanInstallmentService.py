from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.LoanInstallmentRepository import LoanInstallmentRepository
from ...schemas.LoantInstallmentDto import LoanInstallmentDto
from ...schemas.LoanInstallmentResponseDto import LoanInstallmentResponseDto
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class LoanInstallmentService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = LoanInstallmentRepository(db)
        self.mapper = Mapper()
