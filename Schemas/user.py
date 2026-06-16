from pydantic import BaseModel, EmailStr,Field

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length = 8, max_length= 16)
    role: str
    
    
class UserLogin(BaseModel):
    email: EmailStr
    password:  str = Field(min_length = 8, max_length= 16)
    
class UserResponse(BaseModel):
    id : str
    name: str
    email: str
    role: str
    
    #convert database objects into response object
class config:
    from_attributes = True
    