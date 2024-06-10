from pydantic import BaseModel


class TokenDataDto(BaseModel):
    name: str | None = None
