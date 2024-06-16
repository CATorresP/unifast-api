from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.DepartmentDTO import DepartmentDTO
from ..schemas.DepartmentReponseDTO import DepartmentResponseDTO


departmentRouter = APIRouter()
departmentRouter.prefix = "/department"