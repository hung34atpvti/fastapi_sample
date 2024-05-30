from pydantic import BaseModel


class BlogUpdateDTO(BaseModel):
    title: str
    body: str
