from sqlalchemy import Integer, String, Column, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base


class pet(Base):
    __tablename__ = "PET DETAILS"
    ID = Column(Integer, index = True, primary_key = True)
    Name = Column(String)
    Species = Column(String)
    Breed = Column(String)
    Age = Column(Integer)
    Owner_name = Column(String)
    Owner_phone = Column(String)
    Created_at = Column(TIMESTAMP)