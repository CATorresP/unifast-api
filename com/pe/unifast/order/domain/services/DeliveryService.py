from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.DeliveryRepository import DeliveryRepository
from ...schemas.DeliveryDTO import DeliveryDTO 
from ...schemas.DeliveryResponseDTO import DeliveryResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class DeliveryService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = DeliveryRepository(db)
        self.mapper = Mapper()

    def get_delivery_by_id(self, delivery_id: int):
        delivery = self.repository.find_by_id(delivery_id)
        if delivery is None:
            raise HTTPException(status_code=404, detail="Delivery not found")
        return self.mapper.entity_to_response_dto(delivery)
    
    def get_all_delivery(self):
        deliveries = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(deliveries)
    
    def update_delivery_by_id(self, delivery_id:int, delivery_dto:DeliveryDTO):
        delivery = self.repository.find_by_id(delivery_id)
        if delivery is None:
            raise HTTPException(status_code=404, detail="Delivery not found")
        delivery = self.mapper.dto_to_entity(delivery_dto)
        delivery = self.repository.update_delivery_by_id(delivery_id, delivery)
        return self.mapper.entity_to_response_dto(delivery)
    
    def delete_delivery_by_id(self, delivery_id:int):

        delivery = self.repository.find_by_id(delivery_id)
        if delivery is None:
            raise HTTPException(status_code=404, detail="Delivery not found")
        self.repository.delete_delivery_by_id(delivery_id)
        return
    
    def create_delivery(self, delivery_dto:DeliveryDTO):
        delivery = self.mapper.dto_to_entity(delivery_dto)
        delivery = self.repository.create_delivery(delivery)
        return self.mapper.entity_to_response_dto(delivery)