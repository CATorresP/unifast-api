from typing import Annotated

from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, ValidationError
from sqlalchemy.orm import Session

from com.pe.unifast.account.domain.repositories.AccountRepository import AccountRepository
from com.pe.unifast.security.schemas.TokenDataDto import TokenDataDto
from com.pe.unifast.security.schemas.TokenResponseDto import TokenResponseDto
from config.oauth2 import oauth2_scheme

import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from dependencies import get_db_session


class AuthService:

    class HashManager:

        PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

        @classmethod
        def get_password_hash(cls, password):
            return cls.PWD_CONTEXT.hash(password)

        @classmethod
        def verify_password(cls, plain_password, hashed_password):
            return cls.PWD_CONTEXT.verify(plain_password, hashed_password)


    class TokenManager:

        SECRET_KEY = "d908299fc78d30825316dcbb606107a5307a8c26b8e4e4db750f179c93c9a4ae"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 60
        @classmethod

    def __init__(self, db: Session):
        self.account_repository = AccountRepository(db)

    def _get_authenticated_user(self, username, password):
        account = self.account_repository.find_active_by_phone_number(username)
        if not account:
            return None
        if not AuthService.HashManager.verify_password(password, account.hashedPin):
            return None
        else:
            return account

    def get_token(self, username, password):
        account = self._get_authenticated_user(username, password)
        if not account:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        expires_delta = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)

        payload = {
            "id": account.accountID,
            "name": account.name,
            "exp": expire
        }
        token = jwt.encode(payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return token

    def get_token_data(self, token):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=self.ALGORITHM)
            try:
                token_data_dto = TokenDataDto(**payload)
            except ValidationError:
                raise credentials_exception
        except InvalidTokenError:
            raise credentials_exception

        return token_data_dto
