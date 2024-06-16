from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import Session
from com.pe.unifast.order.domain.entities.Department import Department


class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def find_by_id(self, department_id: int):
        stmt = select(Department).filter(Department.departmentID == department_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all(self):
        return self.db.execute(select(Department)).scalars().all()
    
    def update_department_by_id(self, department_id:int, department:Department):
        stmt = update(Department).where(Department.departmentID == department_id).values(department)
        self.db.execute(stmt)
        self.db.commit()
        return self.find_by_id(department_id)
    
    def delete_department_by_id(self, department_id:int):
        stmt = delete(Department).where(Department.departmentID == department_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_department(self, department:Department):
        stmt = insert(Department).values(department)
        self.db.execute(stmt)
        self.db.commit()
        return department
    
