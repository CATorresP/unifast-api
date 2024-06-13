from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.Account import Account


class AccountRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_id(self, account_id: int):
        return self.db.get(Account, account_id)

    def find_active_by_phone_number(self, phone_number: str) -> Optional[Account]:
        stmt = select(Account).filter_by(phoneNumber=phone_number, accountStatus="ACTIVE")
        try:
            account = self.db.execute(stmt).scalar_one()
        except NoResultFound:
            return None
        #except MultipleResultsFound:
        return account

    def save(self, account):
        self.db.add(account)
        return account
