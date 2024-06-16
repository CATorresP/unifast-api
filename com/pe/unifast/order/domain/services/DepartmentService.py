from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.DeparmentRepository import DepartmentRepository
from ...schemas.DepartmentDTO import DepartmentDTO 
from ...schemas.DepartmentReponseDTO import DepartmentResponseDTO 
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = DepartmentRepository(db)
        self.mapper = Mapper()