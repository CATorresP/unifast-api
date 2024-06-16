from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.AddressDetailRepository import AddressDetailRepository
from ...schemas.AddressDetailDTO import AddressDetailDTO 
from ...schemas.AddressDetailResponseDTO import AddressDetailResponseDTO 
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class AddressDetailService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = AddressDetailRepository(db)
        self.mapper = Mapper()
    
    def get_address_detail_by_id(self, address_detail_id: int):
        address_detail = self.repository.find_by_id(address_detail_id)
        if address_detail is None:
            raise HTTPException(status_code=404, detail="Address Detail not found")
        return self.mapper.entity_to_response_dto(address_detail)
    
    def get_all_address_detail(self):
        address_details = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(address_details)
    
    def update_address_detail_by_id(self, address_detail_id:int, address_detail_dto:AddressDetailDTO):
        address_detail = self.repository.find_by_id(address_detail_id)
        if address_detail is None:
            raise HTTPException(status_code=404, detail="Address Detail not found")
        address_detail = self.mapper.dto_to_entity(address_detail_dto)
        address_detail = self.repository.update_address_detail_by_id(address_detail_id, address_detail)
        return self.mapper.entity_to_response_dto(address_detail)
    
    def delete_address_detail_by_id(self, address_detail_id:int):
        address_detail = self.repository.find_by_id(address_detail_id)
        if address_detail is None:
            raise HTTPException(status_code=404, detail="Address Detail not found")
        self.repository.delete_address_detail_by_id(address_detail_id)
        return
    
    def create_address_detail(self, address_detail_dto:AddressDetailDTO):
        address_detail = self.mapper.dto_to_entity(address_detail_dto)
        address_detail = self.repository.create_address_detail(address_detail)
        return self.mapper.entity_to_response_dto(address_detail)
    
