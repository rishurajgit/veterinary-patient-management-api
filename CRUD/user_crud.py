from sqlalchemy.orm import Session
from fastapi import HTTPException
from Models.User import User
from Schemas.user import UserCreate
# from passlib.context import CryptContext
from auth import hash_password

#for user login with jwt
from auth import verify_password, create_access_token
from Schemas.user import UserLogin

# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )



def create_user( db:Session, user_data: UserCreate):
    
    #checking if email already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
        
##hashed password

    hashed_password = hash_password(
        user_data.password
    )
    # hashed_password = pwd_context.hash(
    #     user_data.password
    # )
    
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



#login_user
def login_user(
    db: Session,
    user_data: UserLogin
):
    
    # find user by email
    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    # email not found
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # verify password
    if not verify_password(
        user_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # create jwt token
    access_token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }