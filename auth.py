from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from config import settings


# password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# convert plain password into hashed password
def hash_password(password: str):
    return pwd_context.hash(password)


# verify entered password against stored hash
def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# generate jwt token
def create_access_token(data: dict):

    token_data = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    token_data.update({
        "exp": expire
    })

    access_token = jwt.encode(
        token_data,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return access_token


# decode jwt token
def decode_access_token(token: str):

    payload = jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM]
    )

    return payload