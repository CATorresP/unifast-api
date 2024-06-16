from pydantic import BaseModel

class AccountNotFoundResponse(BaseModel):
    message: str