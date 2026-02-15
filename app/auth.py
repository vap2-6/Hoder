from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import secrets

from .config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# PASSWORD HASHING
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

# ACCESS TOKEN
def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt

# REFRESH TOKEN
def create_refresh_token() -> str:
    return secrets.token_urlsafe(64)
