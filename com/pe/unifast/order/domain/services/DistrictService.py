from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.DistrictRepository import DistrictRepository
from ...schemas.DistrictDTO import DistrictDTO 
from ...schemas.DistrictResponseDTO import DistrictResponseDTO 
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = DistrictRepository(db)
        self.mapper = Mapper()