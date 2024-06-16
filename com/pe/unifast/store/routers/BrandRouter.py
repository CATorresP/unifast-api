from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.BrandDTO import BrandDTO
from ..schemas.BrandResponseDTO import BrandResponseDTO
from ..domain.services.BrandService import BrandService



brandRouter = APIRouter()
brandRouter.prefix = "/brand"

@brandRouter.get("/{brand_id}")
def get_brand_by_id(brand_id:int, db: Annotated[Session, Depends(get_db_session)])->BrandResponseDTO:
    service = BrandService(db)
    brand = service.get_brand_by_id(brand_id)
    return brand

@brandRouter.get("/")
def get_all_brand(db: Annotated[Session, Depends(get_db_session)])->list[BrandResponseDTO]:
    service = BrandService(db)
    brands = service.get_all_brand()
    return brands

@brandRouter.put("/{brand_id}")
def update_brand_by_id(brand_id:int, brand_dto:BrandDTO, db: Annotated[Session, Depends(get_db_session)])->BrandResponseDTO:
    service = BrandService(db)
    brand = service.update_brand_by_id(brand_id, brand_dto)
    return brand

@brandRouter.delete("/{brand_id}")
def delete_brand_by_id(brand_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = BrandService(db)
    service.delete_brand_by_id(brand_id)
    return

@brandRouter.post("/")
def create_brand(brand_dto:BrandDTO, db: Annotated[Session, Depends(get_db_session)])->BrandResponseDTO:
    service = BrandService(db)
    brand = service.create_brand(brand_dto)
    return brand

