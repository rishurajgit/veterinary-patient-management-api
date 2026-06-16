from sqlalchemy import Column, Integer, String, Enum, DateTime
from database import Base
from datetime import datetime
import uuid
import enum

#User Roles

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    VET = "VET"
    RECEPTIONIST = "RECEPTIONIST"
    
class User(Base):
    __tablename__ = "Users"
    
    #UUID primary key
    id = Column(String, primary_key = True, default = lambda: str(uuid.uuid4())) #new UUID whenever a new user record is created
    
    name = Column(String, nullable= False)
    email = Column(String, unique=True, index = True, nullable=False) #find the email much faster because it has an index.
    
    #Hashed password 
    password_hash = Column(String, nullable=False)
    
    #user role
    role = Column(Enum(UserRole), nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    