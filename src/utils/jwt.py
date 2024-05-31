import os
from datetime import datetime, timedelta, timezone

import jwt
from jwt import InvalidTokenError

from ..dtos.token_data_dto import TokenDataDTO

SECRET_KEY = os.getenv('JWT_SECRET_KEY', '14c71116134229d8ceec475f2c8c593795c89492e6b6dc01b9b83138daba1924')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('TOKEN_EXPIRE_MINUTES', 30))


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        token_data = TokenDataDTO(email=email)
        return token_data
    except InvalidTokenError:
        return None
