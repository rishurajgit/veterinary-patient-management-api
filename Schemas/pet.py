from pydantic import BaseModel, Field
from datetime import datetime

class PetCreate(BaseModel):
    PetName : str = Field(min_length = 1, max_length = 15)
    Species : str = Field(min_length = 1, max_length = 10)
    Breed : str = Field(min_length = 1, max_lenght = 20)
    Age : int = Field(min_lenght = 1, max_length = 2000)
    Owner_name: str = Field(min_length = 1, max_length = 20)
    Owner_phone : str = Field(min_length =1, max_length = 10)
    
    
class PetResponse(PetCreate):
    id: int = Field(min_length = 1, max_length = 10000)
    Created_at : datetime
    
    class config:
        from_attribute = True
