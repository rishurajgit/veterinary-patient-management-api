from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from Models.Pets import Pet
from Models.Visit import Visit
from Schemas.pet import PetCreate, PetResponse
from CRUD.pet_crud import create_pet as create_pet_db
from CRUD.pet_crud import  get_all_pets
from CRUD.pet_crud import get_pet_by_id
from CRUD.pet_crud import update_pet
from CRUD.pet_crud import delete_pet
from CRUD.visit_crud import create_visit
from Schemas.visit import VisitCreate
from CRUD.visit_crud import get_visits_by_pet_id
from Models.Owner import Owner
from Schemas.owner import OwnerCreate
from CRUD.owner_crud import create_owner
from CRUD.owner_crud import get_pets_by_owner_id



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
    species: str = None,
    breed: str = None,
    min_age: int = None,
    max_age: int = None,
    owner_id: int = None,
    search: str = None,
    
    page: int = 1,
    limit: int = 10,
    sort_by: str = None,
    sort_order: str = "asc",
    db: Session = Depends(get_db)
):
    
    return get_all_pets(db, species, breed, min_age, max_age, owner_id, search,
                        page, limit, sort_by, sort_order)


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


@app.post("/pets/{pet_id}/visits", tags =["Visits"])
def create_visit_data(
    pet_id: int,
    visit: VisitCreate,
    db: Session = Depends(get_db)
):

    return create_visit(
        db,
        pet_id,
        visit
    )
    
    
@app.get("/pets/{pet_id}/visits", tags =["Visits"])
def get_pet_visits(pet_id:int, db: Session = Depends(get_db)): # Get database session
    return get_visits_by_pet_id(db, pet_id)



@app.post("/Owners", tags =["Owners"])
def create_owner_data(
    owner: OwnerCreate,
    db : Session = Depends(get_db)
):
    return{
        create_owner(db, owner)
    }
    
    
@app.get("/Owners/{owner_id}/pets", tags =["Owners"])
def get_owner_pets(owner_id:int, db: Session = Depends(get_db)):
    
    return get_pets_by_owner_id(db, owner_id)