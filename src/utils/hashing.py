from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(self: str):
        hashed_password = pwd_context.hash(self)
        return hashed_password

    def verify(self: str, hash_password):
        print(f"Verifying hash: {hash_password} with password: {self}")
        return pwd_context.verify(self, hash=hash_password)
