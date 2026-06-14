from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
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
    # owner_name = Column(String)
    # owner_phone = Column(String)
    
    owner_id = Column(Integer, ForeignKey("Owner Details.id"))  #Replacing owner name and phone with id
    
    created_at = Column(DateTime, default = datetime.utcnow)
    
    #one pet can have many visits
    visits = relationship("Visit", back_populates="Pet")
    
    #many pets can have same owner
    
    owner_id = Column(Integer, ForeignKey("Owner Details.id"))
    
    owner = relationship("Owner", back_populates="pets")