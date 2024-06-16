from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.ProductCategoryDTO import ProductCategoryDTO
from ..schemas.ProductCategoryResponseDTO import ProductCategoryResponseDTO



productCategoryRouter = APIRouter()
productCategoryRouter.prefix = "/productCategory"