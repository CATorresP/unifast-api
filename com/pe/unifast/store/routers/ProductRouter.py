from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.ProductDTO import ProductDTO
from ..schemas.ProductResponseDTO import ProductResponseDTO



productRouter = APIRouter()
productRouter.prefix = "/product"