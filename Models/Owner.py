from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Owner(Base):
    __tablename__ = "Owner Details"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True) #for unique email ids
    created_at = Column(DateTime, default = datetime.utcnow)
    
    #one Owner can have many pets
    pets = relationship("Pet", back_populates="Owner")