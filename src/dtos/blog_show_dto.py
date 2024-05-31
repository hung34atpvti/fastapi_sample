from pydantic import BaseModel

from .user_show_dto import UserShowDTO


class BlogShowDTO(BaseModel):
    title: str
    body: str

    created_by: UserShowDTO

    class Config:
        from_attributes = True
