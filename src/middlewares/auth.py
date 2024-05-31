from fastapi import Depends

from ..dtos.user_show_dto import UserShowDTO
from ..utils.oauth2 import get_current_user

user: UserShowDTO = Depends(get_current_user)
