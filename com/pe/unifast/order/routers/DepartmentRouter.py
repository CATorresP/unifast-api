from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.DepartmentDTO import DepartmentDTO
from ..schemas.DepartmentReponseDTO import DepartmentResponseDTO
from ..domain.services.DepartmentService import DepartmentService


departmentRouter = APIRouter()
departmentRouter.prefix = "/department"

@departmentRouter.get("/{department_id}")
def get_department_by_id(department_id:int, db: Annotated[Session, Depends(get_db_session)])->DepartmentResponseDTO:
    service = DepartmentService(db)
    department = service.get_department_by_id(department_id)
    return department

@departmentRouter.get("/")
def get_all_department(db: Annotated[Session, Depends(get_db_session)])->list[DepartmentResponseDTO]:
    service = DepartmentService(db)
    departments = service.get_all_department()
    return departments

@departmentRouter.put("/{department_id}")
def update_department_by_id(department_id:int, department_dto:DepartmentDTO, db: Annotated[Session, Depends(get_db_session)])->DepartmentResponseDTO:
    service = DepartmentService(db)
    department = service.update_department_by_id(department_id, department_dto)
    return department

@departmentRouter.delete("/{department_id}")
def delete_department_by_id(department_id:int, db: Annotated[Session, Depends(get_db_session)])->None:
    service = DepartmentService(db)
    service.delete_department_by_id(department_id)
    return

@departmentRouter.post("/")
def create_department(department_dto:DepartmentDTO, db: Annotated[Session, Depends(get_db_session)])->DepartmentResponseDTO:
    service = DepartmentService(db)
    department = service.create_department(department_dto)
    return department
