from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from Models.Pets import pet
from Models.Visit import Visit
from Schemas.pet import PetCreate, PetResponse
from CRUD.pet_crud import create_pet as create_pet_db
from CRUD.pet_crud import  get_all_pets

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.post("/pets")
def create_pet(
    pet: PetCreate,
    db: Session = Depends(get_db)
):
    return {
        create_pet_db(db, pet)
    }
    
@app.get("/pets")
def get_pet(
    db: Session = Depends(get_db)
):
    return get_all_pets(db)