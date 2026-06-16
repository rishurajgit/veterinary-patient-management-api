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
from CRUD.visit_crud import get_visits_by_pet_id, create_visit, update_visit, delete_visit
from Models.Owner import Owner
from Schemas.owner import OwnerCreate
from CRUD.owner_crud import create_owner
from CRUD.owner_crud import get_pets_by_owner_id
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi import Request
import time
from Schemas.user import UserCreate, UserResponse
from CRUD.user_crud import create_user

app = FastAPI()

#MIDDLEWARE

@app.middleware("http")
async def log_request(request: Request, call_next):
    
    #record start time
    start_time = time.time()
    
    #process request
    response = await call_next(request)
    
    #calculate response time
    process_time = time.time() - start_time
    
    #print log in terminal
    print(
        f"Method: {request.method} | "
        f"Path: {request.url.path} | "
        f"Status COde: {response.status_code} | "
        f"Response time: {process_time: .5f}sec")
    
    return response

# GLOBAL EXCEPTION HANDLING
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,  
        content={
            "success": False,
            "message": exc.detail
        }
    )

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


@app.put("/visits/{visit_id}", tags = ["Visits"])
def update_visit_data(
    visit_id: int,
    visit_data: VisitCreate,
    db: Session = Depends(get_db)):
    return update_visit(
        db,
        visit_id,
        visit_data
    )
    
@app.delete("/visits/{visit_id}", tags=["Visits"])
def delete_visit_data(
    visit_id: int,
    db: Session = Depends(get_db)
):

    return delete_visit(
        db,
        visit_id
    )
    

@app.post("/auth/register", response_model=UserResponse, tags=["Users"])
def register_user(user_data:UserCreate, db:Session = Depends(get_db)):
    
    return create_user(db, user_data)