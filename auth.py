from datetime import datetime, timedelta

from jose import jwt, JWTError
from passlib.context import CryptContext

from config import settings

#GET/auth/user-context
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException
from sqlalchemy.orm import Session

from database import get_db
from Models.User import User


#GET/auth/user-context
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login")


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



#GET/auth/user-context
def get_current_user(token: str,db: Session):
    print("TOKEN", token)

    try:
        payload = decode_access_token(token)

        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user