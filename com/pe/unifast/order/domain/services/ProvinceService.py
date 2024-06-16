from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.ProvinceRepository import ProvinceRepository
from ...schemas.ProvinceDTO import ProvinceDTO
from ...schemas.ProvinceResponseDTO import ProvinceResponseDTO
from ....shared.mapper.Mapper import Mapper

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class ProvinceService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = ProvinceRepository(db)
        self.mapper = Mapper()
    
    def get_province_by_id(self, province_id: int):
        province = self.repository.find_by_id(province_id)
        if province is None:
            raise HTTPException(status_code=404, detail="Province not found")
        return self.mapper.entity_to_response_dto(province)
    
    def get_all_province(self):
        provinces = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(provinces)
    
    def update_province_by_id(self, province_id:int, province_dto:ProvinceDTO):
        province = self.repository.find_by_id(province_id)
        if province is None:
            raise HTTPException(status_code=404, detail="Province not found")
        province = self.mapper.dto_to_entity(province_dto)
        province = self.repository.update_province_by_id(province_id, province)
        return self.mapper.entity_to_response_dto(province)
    
    def delete_province_by_id(self, province_id:int):
        province = self.repository.find_by_id(province_id)
        if province is None:
            raise HTTPException(status_code=404, detail="Province not found")
        self.repository.delete_province_by_id(province_id)
        return
    
    def create_province(self, province_dto:ProvinceDTO):
        province = self.mapper.dto_to_entity(province_dto)
        province = self.repository.create_province(province)
        return self.mapper.entity_to_response_dto(province)
    