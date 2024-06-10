from pydantic import BaseModel


class TokenResponseDto(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
        from_attributes = True
