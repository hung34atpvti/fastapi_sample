from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(tags=['User'], prefix='/user')


@router.post('', response_model=schemas.ShowUserDto)
def create_user(body: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=body.name, email=body.email, password=Hash.bcrypt(body.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUserDto)
def show(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not found.")
    return user
