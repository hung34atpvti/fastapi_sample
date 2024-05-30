from pydantic import BaseModel


class BlogCreateDTO(BaseModel):
    title: str
    body: str
    user_id: int
