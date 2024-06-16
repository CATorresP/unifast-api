from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.SaleDTO import SaleDTO
from ..schemas.SaleResponseDTO import SaleResponseDTO
from ..domain.services.SaleService import SaleService


saleRouter = APIRouter()
saleRouter.prefix = "/sale"

@saleRouter.get("/{sale_id}")
def get_sale_by_id(sale_id:int, db: Annotated[Session, Depends(get_db_session)])->SaleResponseDTO:
    service = SaleService(db)
    sale = service.get_sale_by_id(sale_id)
    return sale

@saleRouter.get("/")
def get_all_sale(db: Annotated[Session, Depends(get_db_session)])->list[SaleResponseDTO]:
    service = SaleService(db)
    sales = service.get_all_sale()
    return sales

@saleRouter.put("/{sale_id}")
def update_sale_by_id(sale_id:int, sale_dto:SaleDTO, db: Annotated[Session, Depends(get_db_session)])->SaleResponseDTO:
    service = SaleService(db)
    sale = service.update_sale_by_id(sale_id, sale_dto)
    return sale

@saleRouter.delete("/{sale_id}")
def delete_sale_by_id(sale_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = SaleService(db)
    service.delete_sale_by_id(sale_id)
    return

@saleRouter.post("/")
def create_sale(sale_dto:SaleDTO, db: Annotated[Session, Depends(get_db_session)])->SaleResponseDTO:
    service = SaleService(db)
    sale = service.create_sale(sale_dto)
    return sale