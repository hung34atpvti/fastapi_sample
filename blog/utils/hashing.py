from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(self: str):
        hashed_password = pwd_context.hash(self)
        return hashed_password
