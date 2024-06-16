from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.ProductRepository import ProductRepository
from ...schemas.ProductDTO import ProductDTO 
from ...schemas.ProductResponseDTO import ProductResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class ProductService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = ProductRepository(db)
        self.mapper = Mapper()