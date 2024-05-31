from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    blogs = relationship('Blog', back_populates='created_by')
