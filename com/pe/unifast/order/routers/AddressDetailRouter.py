from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.AddressDetailDTO import AddressDetailDTO
from ..schemas.AddressDetailResponseDTO import AddressDetailResponseDTO
from ..domain.services.AddressDetailService import AddressDetailService



addressDetailRouter = APIRouter()
addressDetailRouter.prefix = "/addressDetail"

@addressDetailRouter.get("/{address_detail_id}")
def get_address_detail_by_id(address_detail_id:int, db: Annotated[Session, Depends(get_db_session)])->AddressDetailResponseDTO:
    service = AddressDetailService(db)
    address_detail = service.get_address_detail_by_id(address_detail_id)
    return address_detail

    
@addressDetailRouter.get("/")
def get_all_address_detail(db: Annotated[Session, Depends(get_db_session)])->list[AddressDetailResponseDTO]:
    service = AddressDetailService(db)
    address_details = service.get_all_address_detail()
    return address_details

    
@addressDetailRouter.put("/{address_detail_id}")
def update_address_detail_by_id(address_detail_id:int, address_detail_dto:AddressDetailDTO, db: Annotated[Session, Depends(get_db_session)])->AddressDetailResponseDTO:
    service = AddressDetailService(db)
    address_detail = service.update_address_detail_by_id(address_detail_id, address_detail_dto)
    return address_detail
  

@addressDetailRouter.delete("/{address_detail_id}")
def delete_address_detail_by_id(address_detail_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = AddressDetailService(db)
    service.delete_address_detail_by_id(address_detail_id)
    return

    
@addressDetailRouter.post("/")
def create_address_detail(address_detail_dto:AddressDetailDTO, db: Annotated[Session, Depends(get_db_session)])->AddressDetailResponseDTO:
    service = AddressDetailService(db)
    address_detail = service.create_address_detail(address_detail_dto)
    return address_detail

