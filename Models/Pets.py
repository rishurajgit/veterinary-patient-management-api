from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Pet(Base):
    __tablename__ = "PET DETAILS"
    id = Column(Integer, index = True, primary_key = True)
    pet_name = Column(String)
    species = Column(String)
    breed = Column(String)
    age = Column(String)
    owner_name = Column(String)
    owner_phone = Column(String)
    created_at = Column(DateTime, default = datetime.utcnow)
    
    visits = relationship("Visit", back_populates="Pet")