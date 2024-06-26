from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.SaleRepository import SaleRepository
from ...schemas.SaleDTO import SaleDTO 
from ...schemas.SaleResponseDTO import SaleResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class SaleService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = SaleRepository(db)
        self.mapper = Mapper()