from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.BrandDTO import BrandDTO
from ..schemas.BrandResponseDTO import BrandResponseDTO



brandRouter = APIRouter()
brandRouter.prefix = "/brand"