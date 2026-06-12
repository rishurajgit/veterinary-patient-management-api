from pydantic import BaseModel, Field
from datetime import datetime

class PetCreate(BaseModel):
    petname : str 
    species : str 
    breed : str 
    age : int
    owner_name: str 
    owner_phone : str 
    
    
class PetResponse(PetCreate):
    id: int
    created_at : datetime
    
    class Config: # Allows response from SQLAlchemy models
        from_attribute = True
