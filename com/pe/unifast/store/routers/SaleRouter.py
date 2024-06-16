from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.SaleDTO import SaleDTO
from ..schemas.SaleResponseDTO import SaleResponseDTO



saleRouter = APIRouter()
saleRouter.prefix = "/sale"