from pydantic import BaseModel, Field
from datetime import datetime


class VisitCreate(BaseModel):
    
    Visit_date : datetime 
    Reason : str = Field(min_length = 1, max_length = 500)
    Notes: str = Field(min_length = 1, max_length = 500)
    
class VisitResponse(VisitCreate):
    
    Pet_id : int = Field(min_length = 1, max_length = 100)
    id: int
    Created_at: datetime
    
    class Config:
        from_attributes = True  #Read data from SQLalchemy model