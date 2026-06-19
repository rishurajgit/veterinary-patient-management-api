from pydantic import BaseModel, EmailStr,Field
from Models.User import UserRole
from uuid import UUID

#schema for user registration
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length = 8, max_length= 16)
    role: str
    
    
#schema for user login
class UserLogin(BaseModel):
    email: EmailStr
    password:  str = Field(min_length = 8, max_length= 16)
    
    
#schema of API responses
class UserResponse(BaseModel):
    id : UUID
    name: str
    email: str
    role: UserRole
    
    
#convert database objects into response object
class config:
    from_attributes = True