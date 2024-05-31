from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..dtos.token_dto import TokenDTO
from ..repositories.user_repository import UserRepository
from ..utils import jwt
from ..utils.hashing import Hash

router = APIRouter(tags=['Auth'])


@router.post('/login')
async def login(body: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await UserRepository.get_user_by_email(db, body.username)
    if not user or not Hash.verify(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials")
    access_token = jwt.create_access_token(
        data={"sub": user.email, "user_id": user.id}
    )
    return TokenDTO(access_token=access_token, token_type="bearer")
