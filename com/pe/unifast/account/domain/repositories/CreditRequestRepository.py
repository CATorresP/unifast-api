from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.CreditRequest import CreditRequest


class CreditRequestRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_credit_request_by_id(self, credit_request_id: int):
        stmt = select(CreditRequest).where(CreditRequest.creditID == credit_request_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all_credit_request(self):
        return self.db.execute(select(CreditRequest)).scalars().all()
    
    def update_credit_request_by_id(self, credit_request_id:int, credit_request:CreditRequest):
        stmt = update(CreditRequest).where(CreditRequest.creditID == credit_request_id).values(credit_request)
        self.db.execute(stmt)
        self.db.commit()
        return self.get_credit_request_by_id(credit_request_id)
    
    def delete_credit_request_by_id(self, credit_request_id:int):
        stmt = delete(CreditRequest).where(CreditRequest.creditID == credit_request_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_credit_request(self, credit_request:CreditRequest):
        stmt = insert(CreditRequest).values(credit_request)
        self.db.execute(stmt)
        self.db.commit()
        return credit_request
    