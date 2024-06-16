from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.AddressDetail import AddressDetail


class AddressDetailRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, address_detail_id: int):
        stmt = select(AddressDetail).filter(AddressDetail.addressID == address_detail_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(AddressDetail)).scalars().all()
    
    def update_address_detail_by_id(self, address_detail_id:int, address_detail:AddressDetail):
        stmt = update(AddressDetail).where(AddressDetail.addressID == address_detail_id).values(address_detail)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(address_detail_id)
    
    def delete_address_detail_by_id(self, address_detail_id:int):
        stmt = delete(AddressDetail).where(AddressDetail.addressID == address_detail_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_address_detail(self, address_detail:AddressDetail):
        stmt = insert(AddressDetail).values(address_detail)
        self.db.execute(stmt)
        self.db.commit()
        return address_detail
