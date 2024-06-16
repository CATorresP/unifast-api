from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.Delivery import Delivery


class DeliveryRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, delivery_id: int):
        stmt = select(Delivery).filter(Delivery.deliveryID == delivery_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Delivery)).scalars().all()
    
    def update_delivery_by_id(self, delivery_id:int, delivery:Delivery):
        stmt = update(Delivery).where(Delivery.deliveryID == delivery_id).values(delivery)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(delivery_id)
    
    def delete_delivery_by_id(self, delivery_id:int):
        stmt = delete(Delivery).where(Delivery.deliveryID == delivery_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_delivery(self, delivery:Delivery):
        stmt = insert(Delivery).values(delivery)
        self.db.execute(stmt)
        self.db.commit()
        return delivery