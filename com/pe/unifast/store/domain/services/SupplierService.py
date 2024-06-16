from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.SupplierRepository import SupplierRepository
from ...schemas.SupplierDTO import SupplierDTO 
from ...schemas.SupplierResponseDTO import SupplierResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class SupplierService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = SupplierRepository(db)
        self.mapper = Mapper()