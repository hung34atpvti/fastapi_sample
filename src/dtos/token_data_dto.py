from pydantic import BaseModel


class TokenDataDTO(BaseModel):
    email: str
    id: int
