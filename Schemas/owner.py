from sqlalchemy import DateTime
from pydantic import BaseModel
from datetime import datetime

class OwnerCreate(BaseModel):
    name : str
    phone : str 
    email : str 
    # created_at : datetime
    
class OwnerResponse(OwnerCreate):
    id: int
    name: str 
    phone : str 
    created_at : datetime
    
class Config:
    from_attributes = True