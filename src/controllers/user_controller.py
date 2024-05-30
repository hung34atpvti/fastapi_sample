from fastapi import APIRouter, status, HTTPException, Depends
from ..database.database import get_db
from ..dtos.user_create_dto import UserCreateDTO
from ..dtos.user_show_dto import UserShowDTO

from ..repositories.user_repository import UserRepository
from ..utils.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['User'], prefix='/user')


@router.post('', response_model=UserShowDTO)
async def create_user(body: UserCreateDTO, db: Session = Depends(get_db)):
    body.password = Hash.bcrypt(body.password)
    new_user = await UserRepository.create(db, body)
    return new_user


@router.get('/{id}', response_model=UserShowDTO)
async def show(id, db: Session = Depends(get_db)):
    user = await UserRepository.show(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not found.")
    return user
