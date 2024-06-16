from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.DeliveryDTO import DeliveryDTO
from ..schemas.DeliveryResponseDTO import DeliveryResponseDTO
from ..domain.services.DeliveryService import DeliveryService



deliveryRouter = APIRouter()
deliveryRouter.prefix = "/delivery"

@deliveryRouter.get("/{delivery_id}")
def get_delivery_by_id(delivery_id:int, db: Annotated[Session, Depends(get_db_session)])->DeliveryResponseDTO:
    service = DeliveryService(db)
    delivery = service.get_delivery_by_id(delivery_id)
    return delivery

@deliveryRouter.get("/")
def get_all_delivery(db: Annotated[Session, Depends(get_db_session)])->list[DeliveryResponseDTO]:
    service = DeliveryService(db)
    deliveries = service.get_all_delivery()
    return deliveries

@deliveryRouter.put("/{delivery_id}")
def update_delivery_by_id(delivery_id:int, delivery_dto:DeliveryDTO, db: Annotated[Session, Depends(get_db_session)])->DeliveryResponseDTO:
    service = DeliveryService(db)
    delivery = service.update_delivery_by_id(delivery_id, delivery_dto)
    return delivery

@deliveryRouter.delete("/{delivery_id}")
def delete_delivery_by_id(delivery_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = DeliveryService(db)
    service.delete_delivery_by_id(delivery_id)
    return

@deliveryRouter.post("/")
def create_delivery(delivery_dto:DeliveryDTO, db: Annotated[Session, Depends(get_db_session)])->DeliveryResponseDTO:
    service = DeliveryService(db)
    delivery = service.create_delivery(delivery_dto)
    return delivery