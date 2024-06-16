from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.AddressDetailRepository import AddressDetailRepository
from ...schemas.AddressDetailDTO import AddressDetailDTO 
from ...schemas.AddressDetailResponseDTO import AddressDetailResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = AddressDetailRepository(db)
        self.mapper = Mapper()