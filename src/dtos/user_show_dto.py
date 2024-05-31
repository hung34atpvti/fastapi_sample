from pydantic import BaseModel


class UserShowDTO(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True
