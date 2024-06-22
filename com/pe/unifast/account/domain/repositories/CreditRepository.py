from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.Credit import Credit
from ...schemas.CreditSchemas.CreditDto import CreditDto


class CreditRepository:
    def __init__(self, db: Session):
        self.db = db

    #get all
    def get_all(self):
        return self.db.query(Credit).all()
    #get by id
    def find_by_id(self, credit_id: int):
        stmt = select(Credit).filter(Credit.creditID == credit_id)
        return self.db.execute(stmt).scalar_one()
    #updet credit
    def update_credit_by_id(self, creditID:int, credit:CreditDto):
        stmt = update(Credit).where(Credit.creditID == creditID).values(credit)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(creditID)
    #delete credit
    def delete_credit_by_id(self, creditID:int):
        stmt = delete(Credit).where(Credit.creditID == creditID)
        self.db.execute(stmt)
        self.db.commit()
        return 
    #create credit
    def create_credit(self):
        
        stmt = insert(Credit).values()
        result  = self.db.execute(stmt)
        self.db.commit()
        creditID = result.inserted_primary_key[0]
        return self.find_by_id(creditID)
    
    #get by account id
    def find_by_account_id(self, account_id: int):
        stmt = select(Credit).join(Credit.account).filter(Credit.account.accountID == account_id)
        credits = self.db.execute(stmt).scalars().all()
        return credits
    
    #find creditrequest by credit id
    def find_credit_request_by_credit_id(self, credit_id: int):
        stmt = select(Credit).join(Credit.creditRequests).filter(Credit.creditID == credit_id)
        credit_requests = self.db.execute(stmt).scalars().all()
        return credit_requests
    

    
    
    



