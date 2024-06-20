from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.SupplierDTO import SupplierDTO
from ..schemas.SupplierResponseDTO import SupplierResponseDTO
from ..domain.services.SupplierService import SupplierService

from com.pe.unifast.security.domain.services.AuthService import AuthService
from config.oauth2 import oauth2_scheme

supplierRouter = APIRouter()
supplierRouter.prefix = "/sale"

@supplierRouter.get("/{supplier_id}")
def get_supplier_by_id(supplier_id:int, db: Annotated[Session, Depends(get_db_session)],token:Annotated[str,Depends(oauth2_scheme)])->SupplierResponseDTO:
    verify=AuthService(db).TokenManager.decode(token)
    logger.info(verify)
    service = SupplierService(db)
    supplier = service.get_supplier_by_id(supplier_id)
    return supplier

@supplierRouter.get("/")
def get_all_supplier(db: Annotated[Session, Depends(get_db_session)],token:Annotated[str,Depends(oauth2_scheme)])->list[SupplierResponseDTO]:
    verify=AuthService(db).TokenManager.decode(token)
    logger.info(verify)
    service = SupplierService(db)
    suppliers = service.get_all_supplier()
    return suppliers

@supplierRouter.put("/{supplier_id}")
def update_supplier_by_id(supplier_id:int, supplier_dto:SupplierDTO, db: Annotated[Session, Depends(get_db_session)],token:Annotated[str,Depends(oauth2_scheme)])->SupplierResponseDTO:
    verify=AuthService(db).TokenManager.decode(token)
    logger.info(verify)
    service = SupplierService(db)
    supplier = service.update_supplier_by_id(supplier_id, supplier_dto)
    return supplier

@supplierRouter.delete("/{supplier_id}")
def delete_supplier_by_id(supplier_id:int, db: Annotated[Session, Depends(get_db_session)],token:Annotated[str,Depends(oauth2_scheme)])->None:
    verify=AuthService(db).TokenManager.decode(token)
    logger.info(verify)
    service = SupplierService(db)
    service.delete_supplier_by_id(supplier_id)
    return

@supplierRouter.post("/")
def create_supplier(supplier_dto:SupplierDTO, db: Annotated[Session, Depends(get_db_session)],token:Annotated[str,Depends(oauth2_scheme)])->SupplierResponseDTO:
    verify=AuthService(db).TokenManager.decode(token)
    logger.info(verify)
    service = SupplierService(db)
    supplier = service.create_supplier(supplier_dto)
    return supplier


