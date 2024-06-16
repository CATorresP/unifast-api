from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.OrderDTO import OrderDTO
from ..schemas.OrderResponseDTO import OrderResponseDTO
from ..domain.services.OrderService import OrderService

orderRouter = APIRouter()
orderRouter.prefix = "/order"

@orderRouter.get("/{order_id}")
def get_order_by_id(order_id:int, db: Annotated[Session, Depends(get_db_session)])->OrderResponseDTO:
    service = OrderService(db)
    order = service.get_order_by_id(order_id)
    return order

@orderRouter.get("/")
def get_all_order(db: Annotated[Session, Depends(get_db_session)])->list[OrderResponseDTO]:
    service = OrderService(db)
    orders = service.get_all_order()
    return orders

@orderRouter.put("/{order_id}")
def update_order_by_id(order_id:int, order_dto:OrderDTO, db: Annotated[Session, Depends(get_db_session)])->OrderResponseDTO:
    service = OrderService(db)
    order = service.update_order_by_id(order_id, order_dto)
    return order

@orderRouter.delete("/{order_id}")
def delete_order_by_id(order_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = OrderService(db)
    service.delete_order_by_id(order_id)
    return

@orderRouter.post("/")
def create_order(order_dto:OrderDTO, db: Annotated[Session, Depends(get_db_session)])->OrderResponseDTO:
    service = OrderService(db)
    order = service.create_order(order_dto)
    return order
