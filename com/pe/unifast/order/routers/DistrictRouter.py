from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.DistrictDTO import DistrictDTO
from ..schemas.DistrictResponseDTO import DistrictResponseDTO


districtRouter = APIRouter()
districtRouter.prefix = "/district"