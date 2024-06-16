from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.OrderDTO import OrderDTO
from ..schemas.OrderResponseDTO import OrderResponseDTO


orderRouter = APIRouter()
orderRouter.prefix = "/order"