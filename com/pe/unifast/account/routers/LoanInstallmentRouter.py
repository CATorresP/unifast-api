from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import logger
from dependencies import get_db_session

from ..schemas.LoanInstallmentResponseDto import LoanInstallmentResponseDto
from ..schemas.LoantInstallmentDto import  LoanInstallmentDto


loanInstallmentRouter = APIRouter()
loanInstallmentRouter.prefix = "/loanInstallment"