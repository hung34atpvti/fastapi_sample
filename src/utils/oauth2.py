from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from . import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    data = jwt.verify_access_token(token)
    if not data:
        raise credentials_exception
    return data
