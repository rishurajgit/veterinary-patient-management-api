from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Visit(Base):
    __tablename__ = "VISIT OF PETS"
    ID = Column(Integer, primary_key = True, index = True)
    Pet_id = Column(Integer, ForeignKey("PET DETAILS.ID"))
    Visit_date = Column(DateTime)
    Reason = Column(String)
    Notes = Column(Text)
    Created_at = Column(DateTime, default = datetime.utcnow)