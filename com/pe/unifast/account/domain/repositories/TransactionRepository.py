from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.Transaction import Transaction


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_transaction_by_id(self, transaction_id: int):
        stmt = select(Transaction).where(Transaction.transactionID == transaction_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all_transaction(self):
        return self.db.execute(select(Transaction)).scalars().all()
    
    def update_transaction_by_id(self, transaction_id:int, transaction:Transaction):
        stmt = update(Transaction).where(Transaction.transactionID == transaction_id).values(transaction)
        self.db.execute(stmt)
        self.db.commit()
        return self.get_transaction_by_id(transaction_id)
    
    def delete_transaction_by_id(self, transaction_id:int):
        stmt = delete(Transaction).where(Transaction.transactionID == transaction_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_transaction(self, transaction:Transaction):
        stmt = insert(Transaction).values(transaction)
        self.db.execute(stmt)
        self.db.commit()
        return transaction

    