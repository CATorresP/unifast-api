from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.DeparmentRepository import DepartmentRepository
from ...schemas.DepartmentDTO import DepartmentDTO 
from ...schemas.DepartmentReponseDTO import DepartmentResponseDTO 
from ....shared.mapper.Mapper import Mapper


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session


class DepartmentService:
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = DepartmentRepository(db)
        self.mapper = Mapper()

    def get_department_by_id(self, department_id: int):
        department = self.repository.find_by_id(department_id)
        if department is None:
            raise HTTPException(status_code=404, detail="Department not found")
        return self.mapper.entity_to_response_dto(department)
    
    def get_all_department(self):
        departments = self.repository.get_all()
        return self.mapper.list_entity_to_list_response_dto(departments)
    
    def update_department_by_id(self, department_id:int, department_dto:DepartmentDTO):
        department = self.repository.find_by_id(department_id)
        if department is None:
            raise HTTPException(status_code=404, detail="Department not found")
        department = self.mapper.dto_to_entity(department_dto)
        department = self.repository.update_department_by_id(department_id, department)
        return self.mapper.entity_to_response_dto(department)
    
    def delete_department_by_id(self, department_id:int):
        department = self.repository.find_by_id(department_id)
        if department is None:
            raise HTTPException(status_code=404, detail="Department not found")
        self.repository.delete_department_by_id(department_id)
        return
    
    def create_department(self, department_dto:DepartmentDTO):
        department = self.mapper.dto_to_entity(department_dto)
        department = self.repository.create_department(department)
        return self.mapper.entity_to_response_dto(department)