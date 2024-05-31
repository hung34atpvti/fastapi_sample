from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..dtos.blog_create_dto import BlogCreateDTO
from ..dtos.blog_show_dto import BlogShowDTO
from ..dtos.blog_update_dto import BlogUpdateDTO
from ..dtos.user_show_dto import UserShowDTO
from ..repositories.blog_repository import BlogRepository
from ..utils.oauth2 import get_current_user

router = APIRouter(tags=['Blog'], prefix='/blog')


@router.post('', status_code=status.HTTP_201_CREATED)
async def create(body: BlogCreateDTO, db: Session = Depends(get_db),
                 current_user: UserShowDTO = Depends(get_current_user)):
    new_blog = await BlogRepository.create_one(db, body)
    return new_blog


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=BlogShowDTO)
async def show(id, db: Session = Depends(get_db), current_user: UserShowDTO = Depends(get_current_user)):
    blog = await BlogRepository.get_one(db, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    return blog


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, body: BlogUpdateDTO, db: Session = Depends(get_db),
                 current_user: UserShowDTO = Depends(get_current_user)):
    blog = await BlogRepository.update_one(db, id, body)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found.")
    return blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session = Depends(get_db), current_user: UserShowDTO = Depends(get_current_user)):
    return BlogRepository.remove_one(db, id)


@router.get('', response_model=List[BlogShowDTO])
async def show_all(db: Session = Depends(get_db), current_user: UserShowDTO = Depends(get_current_user)):
    blogs = await BlogRepository.get_all(db)
    return blogs
