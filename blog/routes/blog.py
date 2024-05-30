from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=['Blog'], prefix='/blog')


@router.post('', status_code=status.HTTP_201_CREATED)
async def create(body: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=body.title, body=body.body, user_id=body.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlogDto)
async def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    return blog


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, body: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    blog.update({'title': body.title, 'body': body.body})
    db.commit()
    db.refresh(blog)
    return blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'blog deleted successfully'


@router.get('', response_model=List[schemas.ShowBlogDto])
async def show_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
