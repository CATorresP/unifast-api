from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session


from ..schemas.CreditRequestResponseDto import CreditRequesResponseDTO
from ..schemas.CreditRequestDto import CreditRequestDTO

creditRouter = APIRouter()
creditRouter.prefix = "/creditRouter"