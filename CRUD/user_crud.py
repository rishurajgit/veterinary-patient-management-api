from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.User import User
from Schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def create_user( db:Session, user_data: UserCreate):
    
    #checking if email already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
        
    #hashed password
    hashed_password = pwd_context.hash(
        user_data.password
    )
    
    #create user object
    new_user = User(
        name = user_data.name,
        email = user_data.email,
        password_hash = hashed_password,
        role = user_data.role
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user