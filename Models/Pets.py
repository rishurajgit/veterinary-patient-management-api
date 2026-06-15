from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Pet(Base):
    __tablename__ = "PET DETAILS"
    id = Column(Integer, index = True, primary_key = True)
    pet_name = Column(String)
    species = Column(String)
    breed = Column(String)
    age = Column(Integer)
    # owner_name = Column(String)
    # owner_phone = Column(String)
    
    owner_id = Column(Integer, ForeignKey("Owner Details.id"))  #Replacing owner name and phone with id
    
    created_at = Column(DateTime, default = datetime.utcnow)
    
    # marks whether the pet is soft deleted or not
    # False = active pet
    # True = deleted pet
    
    is_deleted = Column(Boolean, default = False)
    
    # stores the date and time when the pet was deleted
    # remains NULL until the pet is soft deleted
    
    deleted_at = Column(DateTime, nullable=True)
    
    #one pet can have many visits
    visits = relationship("Visit", back_populates="Pet")
    
    #many pets can have same owner
    
    # owner_id = Column(Integer, ForeignKey("Owner Details.id"))
    
    owner = relationship("Owner", back_populates="pets")