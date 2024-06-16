from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.SupplierDTO import SupplierDTO
from ..schemas.SupplierResponseDTO import SupplierResponseDTO



supplierRouter = APIRouter()
supplierRouter.prefix = "/sale"