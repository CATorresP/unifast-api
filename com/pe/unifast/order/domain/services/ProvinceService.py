from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.ProvinceRepository import ProvinceRepository
from ...schemas.ProvinceDTO import ProvinceDTO
from ...schemas.ProvinceResponseDTO import ProvinceResponseDTO
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = ProvinceRepository(db)
        self.mapper = Mapper()