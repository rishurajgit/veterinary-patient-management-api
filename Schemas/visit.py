from pydantic import BaseModel, Field
from datetime import datetime


class VisitCreate(BaseModel):
    
    visit_date : datetime 
    reason : str 
    notes: str 
    
class VisitResponse(VisitCreate):
    
    
    pet_id : int
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True  #Read data from SQLalchemy model