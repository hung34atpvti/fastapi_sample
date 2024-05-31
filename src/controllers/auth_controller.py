from fastapi import APIRouter, Depends, HTTPException, status

from ..dtos.login_dto import LoginDTO
from ..database.database import get_db
from sqlalchemy.orm import Session

from ..repositories.user_repository import UserRepository
from ..utils.hashing import Hash
from ..utils import jwt

router = APIRouter(tags=['Auth'])


@router.post('/login')
async def login(body: LoginDTO, db: Session = Depends(get_db)):
    user = await UserRepository.get_user_by_email(db, body.email)
    if not user or not Hash.verify(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials")
    access_token = jwt.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
