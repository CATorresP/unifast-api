from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from com.pe.unifast.account.domain.repositories.AccountRepository import AccountRepository
from com.pe.unifast.account.routers.AccountRouter import account_router
from com.pe.unifast.account.schemas.AccountResponseDto import AccountResponseDto
from com.pe.unifast.security.routers.auth_router import auth_router
from config.database import logger
from dependencies import get_db_session

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
app.include_router(auth_router, prefix="/auth")
#app.include_router(account_router, prefix="/account")

@app.get("/")
async def root():
    return {"message": "Hello World"}

import create_tables

