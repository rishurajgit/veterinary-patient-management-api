from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base  #(Creates a base class for all database tables.)
from config import settings

DATABASE_URL=settings.DATABASE_URL  #WHERE THE DATABASE IS

engine = create_engine(   #CREATE_ENGINE
    DATABASE_URL,
    #connect_args = {"check_same_thread": False}  #Only the thread that created the connection can use it. But FastAPI handles multiple requests simultaneously. So we disable that restriction
)

SessionLocal = sessionmaker(  #CREATE DATABASE SESSION
    autocommit = False,  #Changes are NOT automatically saved.
    autoflush = False,  #Prevents SQLAlchemy from automatically sending changes to the database. We decide when to save. Good for control and performance.
    bind = engine  #Connects sessions to the database engine.
)
Base = declarative_base()  #Creates a parent class for all models.



#Dependencies functions:

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
        