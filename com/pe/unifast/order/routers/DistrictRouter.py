from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.DistrictDTO import DistrictDTO
from ..schemas.DistrictResponseDTO import DistrictResponseDTO
from ..domain.services.DistrictService import DistrictService


districtRouter = APIRouter()
districtRouter.prefix = "/district"

@districtRouter.get("/{district_id}")
def get_district_by_id(district_id:int, db: Annotated[Session, Depends(get_db_session)])->DistrictResponseDTO:
    service = DistrictService(db)
    district = service.get_district_by_id(district_id)
    return district

@districtRouter.get("/")
def get_all_district(db: Annotated[Session, Depends(get_db_session)])->list[DistrictResponseDTO]:
    service = DistrictService(db)
    districts = service.get_all_district()
    return districts

@districtRouter.put("/{district_id}")
def update_district_by_id(district_id:int, district_dto:DistrictDTO, db: Annotated[Session, Depends(get_db_session)])->DistrictResponseDTO:
    service = DistrictService(db)
    district = service.update_district_by_id(district_id, district_dto)
    return district

@districtRouter.delete("/{district_id}")
def delete_district_by_id(district_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = DistrictService(db)
    service.delete_district_by_id(district_id)
    return

@districtRouter.post("/")
def create_district(district_dto:DistrictDTO, db: Annotated[Session, Depends(get_db_session)])->DistrictResponseDTO:
    service = DistrictService(db)
    district = service.create_district(district_dto)
    return district

