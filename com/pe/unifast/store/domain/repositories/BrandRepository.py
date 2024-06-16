from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.store.domain.entities.Brand import Brand


class BrandRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, brand_id: int):
        stmt = select(Brand).filter(Brand.brandID == brand_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Brand)).scalars().all()
    
    def update_brand_by_id(self, brand_id:int, brand:Brand):
        stmt = update(Brand).where(Brand.brandID == brand_id).values(brand)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(brand_id)
    
    def delete_brand_by_id(self, brand_id:int):
        stmt = delete(Brand).where(Brand.brandID == brand_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_brand(self, brand:Brand):
        stmt = insert(Brand).values(brand)
        self.db.execute(stmt)
        self.db.commit()
        return brand
    