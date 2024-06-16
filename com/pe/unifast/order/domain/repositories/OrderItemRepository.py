from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.OrderItem import OrderItem


class OrderItemRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, order_item_id: int):
        stmt = select(OrderItem).filter(OrderItem.productID == order_item_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def find_by_order_id(self, order_id: int):
        stmt = select(OrderItem).filter(OrderItem.orderID == order_id)
        return self.db.execute(stmt).scalars().all()


    def get_all(self):
        return self.db.execute(select(OrderItem)).scalars().all()
    
    def update_order_item_by_id(self, order_item_id:int, order_item:OrderItem):
        stmt = update(OrderItem).where(OrderItem.orderID == order_item_id).values(order_item)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(order_item_id)
    
    def delete_order_item_by_id(self, order_item_id:int):
        stmt = delete(OrderItem).where(OrderItem.orderID == order_item_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_order_item(self, order_item:OrderItem):
        stmt = insert(OrderItem).values(order_item)
        self.db.execute(stmt)
        self.db.commit()
        return order_item
    
    
    