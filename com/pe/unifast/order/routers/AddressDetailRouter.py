from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.AddressDetailDTO import AddressDetailDTO
from ..schemas.AddressDetailResponseDTO import AddressDetailResponseDTO



addressDetailRouter = APIRouter()
addressDetailRouter.prefix = "/addressDetail"