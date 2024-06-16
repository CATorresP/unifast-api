from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.store.domain.entities.ProductCategory import ProductCategory


class ProductCategoryRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, product_category_id: int):
        stmt = select(ProductCategory).filter(ProductCategory.productCategoryID == product_category_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(ProductCategory)).scalars().all()
    
    def update_product_category_by_id(self, product_category_id:int, product_category:ProductCategory):
        stmt = update(ProductCategory).where(ProductCategory.productCategoryID == product_category_id).values(product_category)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(product_category_id)
    
    def delete_product_category_by_id(self, product_category_id:int):
        stmt = delete(ProductCategory).where(ProductCategory.productCategoryID == product_category_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_product_category(self, product_category:ProductCategory):
        stmt = insert(ProductCategory).values(product_category)
        self.db.execute(stmt)
        self.db.commit()
        return product_category
    
    