from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.Order import Order


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, order_id: int):
        stmt = select(Order).filter(Order.orderID == order_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Order)).scalars().all()
    
    def update_order_by_id(self, order_id:int, order:Order):
        stmt = update(Order).where(Order.orderID == order_id).values(order)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(order_id)
    
    def delete_order_by_id(self, order_id:int):
        stmt = delete(Order).where(Order.orderID == order_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_order(self, order:Order):
        stmt = insert(Order).values(order)
        self.db.execute(stmt)
        self.db.commit()
        return order
    