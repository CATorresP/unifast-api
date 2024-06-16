from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.store.domain.entities.Sale import Sale


class SaleRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, sale_id: int):
        stmt = select(Sale).filter(Sale.saleID == sale_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Sale)).scalars().all()
    
    def update_sale_by_id(self, sale_id:int, sale:Sale):
        stmt = update(Sale).where(Sale.saleID == sale_id).values(sale)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(sale_id)
    
    def delete_sale_by_id(self, sale_id:int):
        stmt = delete(Sale).where(Sale.saleID == sale_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_sale(self, sale:Sale):
        stmt = insert(Sale).values(sale)
        self.db.execute(stmt)
        self.db.commit()
        return sale
    
    