from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.ProductCategoryDTO import ProductCategoryDTO
from ..schemas.ProductCategoryResponseDTO import ProductCategoryResponseDTO
from ..domain.services.ProductCategoryService import ProductCategoryService



productCategoryRouter = APIRouter()
productCategoryRouter.prefix = "/productCategory"

@productCategoryRouter.get("/{product_category_id}")
def get_product_category_by_id(product_category_id:int, db: Annotated[Session, Depends(get_db_session)])->ProductCategoryResponseDTO:
    service = ProductCategoryService(db)
    product_category = service.get_product_category_by_id(product_category_id)
    return product_category

@productCategoryRouter.get("/")
def get_all_product_category(db: Annotated[Session, Depends(get_db_session)])->list[ProductCategoryResponseDTO]:
    service = ProductCategoryService(db)
    product_categories = service.get_all_product_category()
    return product_categories

@productCategoryRouter.put("/{product_category_id}")
def update_product_category_by_id(product_category_id:int, product_category_dto:ProductCategoryDTO, db: Annotated[Session, Depends(get_db_session)])->ProductCategoryResponseDTO:
    service = ProductCategoryService(db)
    product_category = service.update_product_category_by_id(product_category_id, product_category_dto)
    return product_category

@productCategoryRouter.delete("/{product_category_id}")
def delete_product_category_by_id(product_category_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = ProductCategoryService(db)
    service.delete_product_category_by_id(product_category_id)
    return

@productCategoryRouter.post("/")
def create_product_category(product_category_dto:ProductCategoryDTO, db: Annotated[Session, Depends(get_db_session)])->ProductCategoryResponseDTO:
    service = ProductCategoryService(db)
    product_category = service.create_product_category(product_category_dto)
    return product_category