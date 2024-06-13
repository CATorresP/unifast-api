from datetime import datetime

from pydantic import BaseModel


class TokenData(BaseModel):
    accountID: int
    name: str
    exp: datetime
