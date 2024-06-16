from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.ProductCategoryRepository import ProductCategoryRepository
from ...schemas.ProductCategoryDTO import ProductCategoryDTO 
from ...schemas.ProductCategoryResponseDTO import ProductCategoryResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class ProductCategoryService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = ProductCategoryRepository(db)
        self.mapper = Mapper()