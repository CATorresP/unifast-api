from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from com.pe.unifast.account.domain.repositories.AccountRepository import AccountRepository
from com.pe.unifast.account.schemas.AccountResponseDto import AccountResponseDto
from com.pe.unifast.security.domain.services.AuthService import AuthService
from com.pe.unifast.security.schemas.TokenResponseDto import TokenResponseDto
from config.database import logger
from dependencies import get_db_session

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/account/")
async def root(db: Annotated[Session, Depends(get_db_session)]):
    account_repository = AccountRepository(db)
    account = account_repository.find_by_id(3)
    logger.info(f"{account.accountID}, {account.phoneNumber}")

    if account is None:
        raise HTTPException(status_code=404, detail="Item not found")
    account_response_dto = AccountResponseDto.from_orm(account)
    return account_response_dto


@app.post("/token")
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Annotated[Session, Depends(get_db_session)]):
    auth_service = AuthService(db)

    token = auth_service.get_token(form_data.username, form_data.password)
    return TokenResponseDto(access_token=token, token_type="bearer")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# from fastapi import FastAPI, APIRouter
# from app.routes import items_router, users_router

# app = FastAPI()

# api_v1_router = APIRouter(prefix="/fastapiv1")

# api_v1_router.include_router(items_router)
# api_v1_router.include_router(users_router)

# app.include_router(api_v1_router)
