from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from com.pe.unifast.security.domain.services.AuthService import AuthService
from com.pe.unifast.security.schemas.TokenResponseDto import TokenResponseDto
from dependencies import get_db_session

auth_router = APIRouter()

@auth_router.get("/")
async def root():   
    return {"message": "HELLO FROM AUTH"}
@auth_router.post("/token/")
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Annotated[Session, Depends(get_db_session)]):
    auth_service = AuthService(db)
    token = auth_service.get_token(form_data.username, form_data.password)
    return token
