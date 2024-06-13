from fastapi import HTTPException, status
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from com.pe.unifast.account.domain.entities.Account import Account
from com.pe.unifast.account.domain.repositories.AccountRepository import AccountRepository
from com.pe.unifast.security.schemas.TokenData import TokenData

import jwt
import bcrypt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone

from com.pe.unifast.security.schemas.TokenResponseDto import TokenResponseDto
from config.database import SessionLocal


class AuthService:
    class HashManager:

        @classmethod
        def get_password_hash(cls, password: str) -> bytes:
            hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return hashed_bytes

        @classmethod
        def verify_password(cls, password: str, hashed_password: str) -> bool:
            matched = bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
            return matched

    class TokenManager:

        SECRET_KEY = "d908299fc78d30825316dcbb606107a5307a8c26b8e4e4db750f179c93c9a4ae"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 15

        @classmethod
        def encode(cls, account: Account) -> str:
            expires_delta = timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
            expire = datetime.now(timezone.utc) + expires_delta
            payload = {
                "id": account.accountID,
                "name": account.name,
                "exp": expire
            }
            token = jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
            return token

        @classmethod
        def decode(cls, token) -> dict:
            try:
                payload = jwt.decode(token, cls.SECRET_KEY, algorithms=cls.ALGORITHM)
            except ExpiredSignatureError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            except InvalidTokenError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return payload

    def __init__(self, db: Session):
        self.account_repository = AccountRepository(db)

    def get_token(self, username, password) -> TokenResponseDto:
        account = self.account_repository.find_active_by_phone_number(username)
        if account is not None:
            if AuthService.HashManager.verify_password(password, account.hashedPin):
                token = self.TokenManager.encode(account)
                return TokenResponseDto(access_token=token, token_type="bearer")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    def get_token_data(self, token) -> TokenData:
        payload = self.TokenManager.decode(token)
        try:
            token_data = TokenData(**payload)
        except ValidationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return token_data

from dependencies import get_db_session
import sqlalchemy
#session = SessionLocal()
#auth_service = AuthService(session)
#token = auth_service.get_token('123456789', '123456')
#print(token)
#self.account_repository.find_active_by_phone_number(username)


#stmt = select(Account).filter_by(accountID=3)
#account = session.execute(stmt).scalar_one()#

#stmt = select(Account).filter_by(phoneNumber='123456789', accountStatus="ACTIVE")
#try:
#    account = session.execute(stmt).scalar_one()
#except NoResultFound:
#    account = None
#print(account)
#print(auth_service.get_token('123456789', '123456'))

#ba = AuthService.HashManager.get_password_hash('123456')
#ca = ba.decode('utf-8')
#print('bytes: ', ba)
#print('string: ', ca)
#string = '$12$L5QoJUVt7hyPUrw0ih.EoercV2toTJSBRGAvDh5auoBqqBbf2EF0.'
#print(AuthService.HashManager.verify_password('123456', '$2b$12$U9kgSRckvXJLHZeSYkLBE.Qtvwcw6nnOgC.EhGw.hQ0TtnIraHfzO'))

