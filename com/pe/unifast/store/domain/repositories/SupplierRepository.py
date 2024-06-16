from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.store.domain.entities.Supplier import Supplier


class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db