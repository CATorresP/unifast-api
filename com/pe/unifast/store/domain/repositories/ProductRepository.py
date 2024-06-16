from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.store.domain.entities.Product import Product


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, product_id: int):
        stmt = select(Product).filter(Product.productID == product_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Product)).scalars().all()
    
    def update_product_by_id(self, product_id:int, product:Product):
        stmt = update(Product).where(Product.productID == product_id).values(product)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(product_id)
    
    def delete_product_by_id(self, product_id:int):
        stmt = delete(Product).where(Product.productID == product_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_product(self, product:Product):
        stmt = insert(Product).values(product)
        self.db.execute(stmt)
        self.db.commit()
        return product
    