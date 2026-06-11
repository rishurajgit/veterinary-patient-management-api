from sqlalchemy import UUID, DateTime
from pydantic import BaseModel, Field
from datetime import datetime

class OwnerCreate(BaseModel):
    Owner_name : str = Field(min_length=2, max_length=20)
    Phone : str = Field(min_length=10, max_length=10)
    Email : str 
    Created_at : DateTime
    
class OwnerResponse(OwnerCreate):
    ID: UUID
    Owner_name: str = Field(min_length=2, max_length=20)
    Phone : str = Field(min_length=10, max_length=10)
    Created_at : DateTime
    
class Config:
    from_attributes = True