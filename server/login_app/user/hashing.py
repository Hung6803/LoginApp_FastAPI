from passlib.context import CryptContext
from . import services

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(database, email, password):
    user = services.get_user_by_email(email, database)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
