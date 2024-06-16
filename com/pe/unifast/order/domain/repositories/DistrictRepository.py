from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.District import District


class DistrictRepository:
    def __init__(self, db: Session):
        self.db = db