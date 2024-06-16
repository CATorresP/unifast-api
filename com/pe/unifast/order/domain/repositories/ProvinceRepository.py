from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.Province import Province


class ProvinceRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, province_id: int):
        stmt = select(Province).filter(Province.provinceID == province_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Province)).scalars().all()
    
    def update_province_by_id(self, province_id:int, province:Province):
        stmt = update(Province).where(Province.provinceID == province_id).values(province)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(province_id)
    
    def delete_province_by_id(self, province_id:int):
        stmt = delete(Province).where(Province.provinceID == province_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_province(self, province:Province):
        stmt = insert(Province).values(province)
        self.db.execute(stmt)
        self.db.commit()
        return province
    
    