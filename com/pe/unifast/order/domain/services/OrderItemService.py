from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.OrderItemRepository import OrderItemRepository
from ...schemas.OrderItemDTO import OrderItemDTO
from ...schemas.OrderItemDTOResponse import OrderItemResponseDTO
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class OrderItemService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = OrderItemRepository(db)
        self.mapper = Mapper()
    
    def get_order_item_by_id(self, order_item_id: int):
        order_item = self.repository.find_by_id(order_item_id)
        if order_item is None:
            raise HTTPException(status_code=404, detail="Order Item not found")
        return self.mapper.entity_to_response_dto(order_item)
    
    def get_all_order_item(self):
        order_items = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(order_items)
    
    def update_order_item_by_id(self, order_item_id:int, order_item_dto:OrderItemDTO):
        order_item = self.repository.find_by_id(order_item_id)
        if order_item is None:
            raise HTTPException(status_code=404, detail="Order Item not found")
        order_item = self.mapper.dto_to_entity(order_item_dto)
        order_item = self.repository.update_order_item_by_id(order_item_id, order_item)
        return self.mapper.entity_to_response_dto(order_item)
    
    def delete_order_item_by_id(self, order_item_id:int):
        order_item = self.repository.find_by_id(order_item_id)
        if order_item is None:
            raise HTTPException(status_code=404, detail="Order Item not found")
        self.repository.delete_order_item_by_id(order_item_id)
        return
    
    def create_order_item(self, order_item_dto:OrderItemDTO):
        order_item = self.mapper.dto_to_entity(order_item_dto)
        order_item = self.repository.create_order_item(order_item)
        return self.mapper.entity_to_response_dto(order_item)