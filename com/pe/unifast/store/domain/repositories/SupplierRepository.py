from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.store.domain.entities.Supplier import Supplier


class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, supplier_id: int):
        stmt = select(Supplier).filter(Supplier.supplierID == supplier_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Supplier)).scalars().all()
    
    def update_supplier_by_id(self, supplier_id:int, supplier:Supplier):
        stmt = update(Supplier).where(Supplier.supplierID == supplier_id).values(supplier)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(supplier_id)
    
    def delete_supplier_by_id(self, supplier_id:int):
        stmt = delete(Supplier).where(Supplier.supplierID == supplier_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_supplier(self, supplier:Supplier):
        stmt = insert(Supplier).values(supplier)
        self.db.execute(stmt)
        self.db.commit()
        return supplier
    
    