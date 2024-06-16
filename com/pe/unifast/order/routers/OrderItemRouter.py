from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.OrderItemDTO import OrderItemDTO
from ..schemas.OrderItemDTOResponse import OrderItemResponseDTO


orderItemRouter = APIRouter()
orderItemRouter.prefix = "/orderItem"