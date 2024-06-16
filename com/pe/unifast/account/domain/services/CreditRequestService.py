from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.CreditRequestRepository import CreditRequestRepository
from ...schemas.CreditRequestDto import CreditRequestDTO
from ...schemas.CreditRequestResponseDto import CreditRequesResponseDTO
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class CreditRequestService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = CreditRequestRepository(db)
        self.mapper = Mapper()
