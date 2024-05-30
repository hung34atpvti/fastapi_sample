from typing import List
from fastapi import FastAPI, Depends, status, HTTPException

from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

from .hashing import Hash

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blog'])
async def create(body: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=body.title, body=body.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlogDto, tags=['blog'])
async def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    return blog


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blog'])
async def update(id, body: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    blog.update({'title': body.title, 'body': body.body})
    db.commit()
    db.refresh(blog)
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
async def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'blog deleted successfully'


@app.get('/blog', response_model=List[schemas.ShowBlogDto], tags=['blog'])
async def show_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.post('/user', response_model=schemas.ShowUserDto, tags=['user'])
def create_user(body: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=body.name, email=body.email, password=Hash.bcrypt(body.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model=schemas.ShowUserDto, tags=['user'])
def show(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not found.")
    return user
