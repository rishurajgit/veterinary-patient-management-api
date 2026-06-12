from sqlalchemy import  DateTime
from pydantic import BaseModel
from datetime import datetime

class OwnerCreate(BaseModel):
    owner_name : str
    phone : str 
    email : str 
    created_at : DateTime
    
class OwnerResponse(OwnerCreate):
    id: int
    owner_name: str 
    phone : str 
    created_at : DateTime
    
class Config:
    from_attributes = True