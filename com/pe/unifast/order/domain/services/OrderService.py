from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.OrderRepository import OrderRepository
from ...schemas.OrderDTO import OrderDTO
from ...schemas.OrderResponseDTO import OrderResponseDTO
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AccountService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = OrderRepository(db)
        self.mapper = Mapper()