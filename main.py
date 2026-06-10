from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from Models.Pets import pet
from Models.Visit import Visit
from Schemas.pet import PetCreate, PetResponse
from CRUD.pet_crud import create_pet as create_pet_db
from CRUD.pet_crud import  get_all_pets
from CRUD.pet_crud import get_pet_by_id
from CRUD.pet_crud import update_pet
from CRUD.pet_crud import delete_pet






app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.post("/pets", tags=["Pets"])
def create_pet(
    pet: PetCreate,
    db: Session = Depends(get_db)
):
    return {
        create_pet_db(db, pet)
    }
    
@app.get("/pets", tags=["Pets"])
def get_pets(
    db: Session = Depends(get_db)
):
    return get_all_pets(db)


@app.get("/pets/{pet_id}", tags=["Pets"])
def get_single_pet(
    pet_id: int,
    db : Session = Depends(get_db)
):
    return{
        get_pet_by_id(db, pet_id)
    }
    
@app.put("/pets/{pet_id}", tags=["Pets"])
def update_pet_data(
    pet_id: int,
    pet_data: PetCreate,
    db : Session = Depends(get_db)
):
    return update_pet(db, pet_id, pet_data)


@app.delete("/pets/{pet_id}", tags=["Pets"])
def delete_pet_data(
    pet_id: int,
    db: Session = Depends(get_db)
):
    return delete_pet(db, pet_id)