from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.ProvinceDTO import ProvinceDTO
from ..schemas.ProvinceResponseDTO import ProvinceResponseDTO
from ..domain.services.ProvinceService import ProvinceService

provinceRouter = APIRouter()
provinceRouter.prefix = "/province"

@provinceRouter.get("/{province_id}")
def get_province_by_id(province_id:int, db: Annotated[Session, Depends(get_db_session)])->ProvinceResponseDTO:
    service = ProvinceService(db)
    province = service.get_province_by_id(province_id)
    return province

@provinceRouter.get("/")
def get_all_province(db: Annotated[Session, Depends(get_db_session)])->list[ProvinceResponseDTO]:
    service = ProvinceService(db)
    provinces = service.get_all_province()
    return provinces

@provinceRouter.put("/{province_id}")
def update_province_by_id(province_id:int, province_dto:ProvinceDTO, db: Annotated[Session, Depends(get_db_session)])->ProvinceResponseDTO:
    service = ProvinceService(db)
    province = service.update_province_by_id(province_id, province_dto)
    return province

@provinceRouter.delete("/{province_id}")
def delete_province_by_id(province_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = ProvinceService(db)
    service.delete_province_by_id(province_id)
    return

@provinceRouter.post("/")
def create_province(province_dto:ProvinceDTO, db: Annotated[Session, Depends(get_db_session)])->ProvinceResponseDTO:
    service = ProvinceService(db)
    province = service.create_province(province_dto)
    return province
