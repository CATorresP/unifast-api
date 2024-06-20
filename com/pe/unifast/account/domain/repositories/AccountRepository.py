from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.Account import Account


class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    #get by id
    def find_by_id(self, account_id: int):
        stmt = select(Account).filter(Account.accountID == account_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    #get all
    def get_all(self):
        return self.db.execute(select(Account)).scalars().all()
    #updete by id
    def update_account_by_id(self, account_id:int, account:Account):
        stmt = update(Account).where(Account.accountID == account_id).values(account)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(account_id)
    #delete by id
    def delete_account_by_id(self, account_id:int):
        stmt = delete(Account).where(Account.accountID == account_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    #create account
    def create_account(self, account:Account):
        stmt = insert(Account).values(account)
        self.db.execute(stmt)
        self.db.commit()
        return account
    
    #find credit by account id
    def find_credit_by_account_id(self, account_id: int):
        stmt = select(Account).join(Account.credit).filter(Account.accountID == account_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    #find transaction by account id
    def find_transaction_by_account_id(self, account_id: int):
        stmt = select(Account).join(Account.transaction).filter(Account.accountID == account_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    #find transaction subject by account id
    def find_transaction_subject_by_account_id(self, account_id: int):
        stmt = select(Account).join(Account.transactionSubject).filter(Account.accountID == account_id)
        return self.db.execute(stmt).scalar_one_or_none()
    #find by dni
    def find_by_dni(self, dni: str):
        stmt = select(Account).filter(Account.dni == dni)
        return self.db.execute(stmt).scalar_one_or_none()
    #find by email
    def find_by_email(self, email: str):
        stmt = select(Account).filter(Account.email == email)
        return self.db.execute(stmt).scalar_one_or_none()
    #find by phone number
    def find_by_phone_number(self, phone_number: str):
        stmt = select(Account).filter(Account.phoneNumber == phone_number, Account.status == 'ACTIVE')
        return self.db.execute(stmt).scalar_one_or_none()
    