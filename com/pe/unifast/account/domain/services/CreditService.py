from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.CreditRepository import CreditRepository
from ...schemas.CreditDto import CreditDto
from ...schemas.CreditResponseDto import CreditResponseDto
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class CreditService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = CreditRepository(db)
        self.mapper = Mapper()
