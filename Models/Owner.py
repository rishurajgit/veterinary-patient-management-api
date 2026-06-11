from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Owner(Base):
    __tablename__ = "Owner Details"
    
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Phone = Column(String)
    Email = Column(String, unique=True) #for unique email ids
    Created_at = Column(DateTime, default = datetime.utcnow)