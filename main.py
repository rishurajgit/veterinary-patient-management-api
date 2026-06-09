from fastapi import FastAPI
from database import engine, Base
from Models.Pets import pet
from Models.Visit import Visit

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.post("/")
def post_data():
    return{
        "Message":"Database Created"
    }