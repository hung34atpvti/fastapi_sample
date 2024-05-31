from ..dtos.blog_create_dto import BlogCreateDTO
from ..dtos.blog_update_dto import BlogUpdateDTO
from ..models.blog import Blog
from sqlalchemy.orm import Session


class BlogRepository:

    async def get_all(self: Session):
        blogs = self.query(Blog).all()
        return blogs

    async def create_one(self: Session, data: BlogCreateDTO):
        new_blog = Blog(title=data.title, body=data.body, user_id=data.user_id)
        self.add(new_blog)
        self.commit()
        self.refresh(new_blog)
        return new_blog

    async def get_one(self: Session, id):
        blog = self.query(Blog).filter(Blog.id == id).first()
        return blog

    async def update_one(self: Session, id, data: BlogUpdateDTO):
        blog = self.query(Blog).filter(Blog.id == id)
        blog.update({'title': data.title, 'body': data.body})
        self.commit()
        self.refresh(blog)
        return blog

    async def remove_one(self: Session, id):
        self.query(Blog).filter(Blog.id == id).delete()
        return
