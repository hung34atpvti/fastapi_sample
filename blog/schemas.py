from typing import List

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    user_id: int


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUserDto(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        from_attributes = True


class ShowBlogDto(BaseModel):
    title: str
    body: str
    created_by: ShowUserDto

    class Config:
        from_attributes = True
