from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.OrderItemDTO import OrderItemDTO
from ..schemas.OrderItemDTOResponse import OrderItemResponseDTO
from ..domain.services.OrderItemService import OrderItemService


orderItemRouter = APIRouter()
orderItemRouter.prefix = "/orderItem"

@orderItemRouter.get("/{order_item_id}")
def get_order_item_by_id(order_item_id:int, db: Annotated[Session, Depends(get_db_session)])->OrderItemResponseDTO:
    service = OrderItemService(db)
    order_item = service.get_order_item_by_id(order_item_id)
    return order_item

@orderItemRouter.get("/")
def get_all_order_item(db: Annotated[Session, Depends(get_db_session)])->list[OrderItemResponseDTO]:
    service = OrderItemService(db)
    order_items = service.get_all_order_item()
    return order_items

@orderItemRouter.put("/{order_item_id}")
def update_order_item_by_id(order_item_id:int, order_item_dto:OrderItemDTO, db: Annotated[Session, Depends(get_db_session)])->OrderItemResponseDTO:
    service = OrderItemService(db)
    order_item = service.update_order_item_by_id(order_item_id, order_item_dto)
    return order_item

@orderItemRouter.delete("/{order_item_id}")
def delete_order_item_by_id(order_item_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = OrderItemService(db)
    service.delete_order_item_by_id(order_item_id)
    return

@orderItemRouter.post("/")
def create_order_item(order_item_dto:OrderItemDTO, db: Annotated[Session, Depends(get_db_session)])->OrderItemResponseDTO:
    service = OrderItemService(db)
    order_item = service.create_order_item(order_item_dto)
    return order_item

