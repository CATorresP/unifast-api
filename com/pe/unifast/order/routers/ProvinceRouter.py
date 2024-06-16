from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.ProvinceDTO import ProvinceDTO
from ..schemas.ProvinceResponseDTO import ProvinceResponseDTO


provinceRouter = APIRouter()
provinceRouter.prefix = "/province"