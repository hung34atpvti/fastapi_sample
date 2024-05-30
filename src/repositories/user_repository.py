from ..models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    async def create(self: Session, data):
        new_user = User(name=data.name, email=data.email, password=data.password)
        self.add(new_user)
        self.commit()
        self.refresh(new_user)
        return new_user

    async def show(self: Session, id):
        user = self.query(User).filter(User.id == id).first()
        return user
