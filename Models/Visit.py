from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base


class Visit(Base):
    __tablename__ = "VISIT OF PETS"
    ID = Column(Integer, primary_key = True, Index = True)
    Pet_id = Column(Integer, ForeignKey("Pets.id"))
    Visit_date = Column(DateTime)
    Reason = Column(String)
    Notes = Column(Text)
    Created_at = Column(TIMESTAMP)