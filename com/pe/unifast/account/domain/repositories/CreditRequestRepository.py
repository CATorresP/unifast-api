from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.CreditRequest import CreditRequest


class CreditRequestRepository:
    def __init__(self, db: Session):
        self.db = db