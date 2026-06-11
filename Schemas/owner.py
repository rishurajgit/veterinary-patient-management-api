from sqlalchemy import UUID, DateTime
from pydantic import BaseModel
from datetime import datetime

class OwnerCreate(BaseModel):
    Owner_name : str
    Phone : str 
    Email : str 
    Created_at : DateTime
    
class OwnerResponse(OwnerCreate):
    ID: UUID
    Owner_name: str 
    Phone : str 
    Created_at : DateTime
    
class Config:
    from_attributes = True