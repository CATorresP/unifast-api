from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.District import District


class DistrictRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, district_id: int):
        stmt = select(District).filter(District.districtID == district_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(District)).scalars().all()
    
    def update_district_by_id(self, district_id:int, district:District):
        stmt = update(District).where(District.districtID == district_id).values(district)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(district_id)
    
    def delete_district_by_id(self, district_id:int):
        stmt = delete(District).where(District.districtID == district_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_district(self, district:District):
        stmt = insert(District).values(district)
        self.db.execute(stmt)
        self.db.commit()
        return district
    
    