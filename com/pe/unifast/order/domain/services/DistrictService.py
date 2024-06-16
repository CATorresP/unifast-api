from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.DistrictRepository import DistrictRepository
from ...schemas.DistrictDTO import DistrictDTO 
from ...schemas.DistrictResponseDTO import DistrictResponseDTO 
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class DistrictService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = DistrictRepository(db)
        self.mapper = Mapper()
    
    def get_district_by_id(self, district_id: int):
        district = self.repository.find_by_id(district_id)
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")
        return self.mapper.entity_to_response_dto(district)
    
    def get_all_district(self):
        districts = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(districts)
    
    def update_district_by_id(self, district_id:int, district_dto:DistrictDTO):
        district = self.repository.find_by_id(district_id)
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")
        district = self.mapper.dto_to_entity(district_dto)
        district = self.repository.update_district_by_id(district_id, district)
        return self.mapper.entity_to_response_dto(district)
    
    def delete_district_by_id(self, district_id:int):
        district = self.repository.find_by_id(district_id)
        if district is None:
            raise HTTPException(status_code=404, detail="District not found")
        self.repository.delete_district_by_id(district_id)
        return
    
    def create_district(self, district_dto:DistrictDTO):
        district = self.mapper.dto_to_entity(district_dto)
        district = self.repository.create_district(district)
        return self.mapper.entity_to_response_dto(district)
    
    