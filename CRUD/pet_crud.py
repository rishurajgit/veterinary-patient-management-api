from fastapi import HTTPException
from sqlalchemy.orm import Session
from Models.Pets import Pet
from Schemas.pet import PetCreate
from Models.Visit import Visit



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
        
def get_all_pets(db: Session):
    try:
        pets = db.query(Pet).all()
        return pets
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = str(e)
        )
        
def get_pet_by_id(db, pet_id:int):
    pet_data = db.query(Pet).filter(Pet.id == pet_id).first()
    
    
    
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

    pet_to_update.pet_Name = pet_data.petname
    pet_to_update.species = pet_data.species
    pet_to_update.breed = pet_data.breed
    pet_to_update.age = pet_data.age
    pet_to_update.owner_name = pet_data.owner_name
    pet_to_update.owner_phone = pet_data.owner_phone

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

    db.query(Visit).filter(
        Visit.pet_id == pet_id
    ).delete()

    # Delete pet
    db.delete(pet_to_delete)
    db.commit()
    return {
        "message": "Pet and related visits deleted successfully"
    }