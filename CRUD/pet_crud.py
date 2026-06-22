from fastapi import HTTPException
from sqlalchemy.orm import Session
from Models.Pets import Pet
from Schemas.pet import PetCreate
from Models.Visit import Visit
from datetime import datetime



def create_pet(db: Session, pet_data: PetCreate):
    try:
        #Create pet object
        new_pet = Pet(
        pet_name = pet_data.petname,
        species = pet_data.species,
        breed = pet_data.breed,
        age = pet_data.age,
        # owner_name = pet_data.owner_name,
        # owner_phone = pet_data.owner_phone
        owner_id = pet_data.owner_id
        )
        
        #Adding pet to data base
        db.add(new_pet)
        db.commit()
        db.refresh(new_pet)
        
        return new_pet
    except Exception as e:
        raise HTTPException(
        status_code=500,
        detail=str(e)
    )
    
# retrieves all pets and apply the filter     
def get_all_pets(
    db: Session,
    species: str = None,
    breed: str = None,
    min_age: int = None,
    max_age: int = None,
    owner_id: int = None,
    search: str = None,
    page: int = 1,
    limit: int = 10,
    sort_by: str = None,
    sort_order: str = "asc"):
    try:
        # pets = db.query(Pet).all()
        # return pets
        # query = db.query(Pet)  #Create the base query for the pet table
        
        query = db.query(Pet).filter(    #only fetch pets that are not soft deleted
            Pet.is_deleted == False
)
        
        if species:
            query = query.filter(Pet.species == species)
            
        if breed:
            query = query.filter(Pet.breed == breed)
            
        if min_age:
            query = query.filter(Pet.age >= min_age)
            
        if max_age:
            query = query.filter(Pet.age <= max_age)
            
        if owner_id:
            query = query.filter(Pet.owner_id == owner_id)
            
        if search:
            query = query.filter(
                Pet.pet_name.ilike(f"%{search}%")  #search pets by name case insensitive
            )
        #SORTING
        if sort_by == "pet_name":
            if sort_order == "desc":
                query = query.order_by(Pet.pet_name.desc())
            else:
                query = query.order_by(Pet.pet_name.asc())
                
                
        elif sort_by == "age":
            if sort_order == "desc":
                query = query.order_by(Pet.age.desc())
            else:
                query = query.order_by(Pet.age.asc())


        elif sort_by == "created_at":       

            if sort_order == "desc":
                query = query.order_by(Pet.created_at.desc())
        else:
            query = query.order_by(Pet.created_at.asc())
            
            # PAGINATION
        offset = (page - 1) * limit
        query = query.offset(offset).limit(limit)
        
        return query.all()
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = str(e)
        )
        
def get_pet_by_id(db, pet_id:int):
    # pet_data = db.query(Pet).filter(Pet.id == pet_id).first()
    
    pet_data = db.query(Pet).filter(
    Pet.id == pet_id,
    Pet.is_deleted == False).first()  #only return pet if it is not soft deleted
    
    if pet_data is None:
        raise HTTPException(
            status_code = 404,
            detail= "pet not found: Try Again"
        )
        
    return pet_data


def update_pet(db, pet_id: int, pet_data: PetCreate):
    
    pet_to_update = db.query(Pet).filter(
        Pet.id == pet_id).first()

    if pet_to_update is None:
        raise HTTPException(
            status_code=404,
            detail="Pet not found"
        )

    pet_to_update.pet_name = pet_data.petname
    pet_to_update.species = pet_data.species
    pet_to_update.breed = pet_data.breed
    pet_to_update.age = pet_data.age
    # pet_to_update.owner_name = pet_data.owner_name
    # pet_to_update.owner_phone = pet_data.owner_phone
    pet_to_update.owner_id = pet_data.owner_id
    pet_to_update.updated_at = datetime.utcnow() # update audit field

    db.commit()
    db.refresh(pet_to_update)

    return pet_to_update


def delete_pet(db, pet_id: int):
    
    pet_to_delete = db.query(Pet).filter(
        Pet.id == pet_id
    ).first()

    if pet_to_delete is None:
        raise HTTPException(
            status_code=404,
            detail="Pet not found"
        )

    # db.query(Visit).filter(
    #     Visit.pet_id == pet_id
    # ).delete()

    # # Delete pet
    # db.delete(pet_to_delete)
    # db.commit()
    
    pet_to_delete.is_deleted = True
    pet_to_delete.deleted_at = datetime.utcnow()

    db.commit()
    db.refresh(pet_to_delete)
    return {
        "message": "Pet soft deleted successfully"
    }