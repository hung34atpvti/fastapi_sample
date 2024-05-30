from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ShowBlogDto(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUserDto(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True
