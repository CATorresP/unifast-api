from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.ProductDTO import ProductDTO
from ..schemas.ProductResponseDTO import ProductResponseDTO
from ..domain.services.ProductService import ProductService



productRouter = APIRouter()
productRouter.prefix = "/product"

@productRouter.get("/{product_id}")
def get_product_by_id(product_id:int, db: Annotated[Session, Depends(get_db_session)])->ProductResponseDTO:
    service = ProductService(db)
    product = service.get_product_by_id(product_id)
    return product

@productRouter.get("/")
def get_all_product(db: Annotated[Session, Depends(get_db_session)])->list[ProductResponseDTO]:
    service = ProductService(db)
    products = service.get_all_product()
    return products

@productRouter.put("/{product_id}")
def update_product_by_id(product_id:int, product_dto:ProductDTO, db: Annotated[Session, Depends(get_db_session)])->ProductResponseDTO:
    service = ProductService(db)
    product = service.update_product_by_id(product_id, product_dto)
    return product

@productRouter.delete("/{product_id}")
def delete_product_by_id(product_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = ProductService(db)
    service.delete_product_by_id(product_id)
    return

@productRouter.post("/")
def create_product(product_dto:ProductDTO, db: Annotated[Session, Depends(get_db_session)])->ProductResponseDTO:
    service = ProductService(db)
    product = service.create_product(product_dto)
    return product