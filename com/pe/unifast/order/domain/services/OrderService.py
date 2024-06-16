from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.OrderRepository import OrderRepository
from ...schemas.OrderDTO import OrderDTO
from ...schemas.OrderResponseDTO import OrderResponseDTO
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class OrderService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = OrderRepository(db)
        self.mapper = Mapper()
    
    def get_order_by_id(self, order_id: int):
        order = self.repository.find_by_id(order_id)
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return self.mapper.entity_to_response_dto(order)
    
    def get_all_order(self):
        orders = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(orders)
    
    def update_order_by_id(self, order_id:int, order_dto:OrderDTO):
        order = self.repository.find_by_id(order_id)
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        order = self.mapper.dto_to_entity(order_dto)
        order = self.repository.update_order_by_id(order_id, order)
        return self.mapper.entity_to_response_dto(order)
    
    def delete_order_by_id(self, order_id:int):
        order = self.repository.find_by_id(order_id)
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        self.repository.delete_order_by_id(order_id)
        return
    
    def create_order(self, order_dto:OrderDTO):
        order = self.mapper.dto_to_entity(order_dto)
        order = self.repository.create_order(order)
        return self.mapper.entity_to_response_dto(order)
    
    