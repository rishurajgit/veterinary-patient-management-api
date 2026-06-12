from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Visit(Base):
    __tablename__ = "VISIT OF PETS"
    id = Column(Integer, primary_key = True, index = True)
    pet_id = Column(Integer, ForeignKey("PET DETAILS.id"))
    visit_date = Column(DateTime)
    reason = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime, default = datetime.utcnow)
    
    Pet = relationship("Pet", back_populates="visits")