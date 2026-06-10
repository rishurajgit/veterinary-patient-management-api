from fastapi import HTTPException
from sqlalchemy.orm import Session
from Models.Pets import pet
from Schemas.pet import PetCreate

def create_pet(db: Session, pet_data: PetCreate):
    try:
        #Create pet object
        new_pet = pet(
        Pet_Name = pet_data.PetName,
        Species = pet_data.Species,
        Breed = pet_data.Breed,
        Age = pet_data.Age,
        Owner_name = pet_data.Owner_name,
        Owner_phone = pet_data.Owner_phone
            
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
        pets = db.query(pet).all()
        return pets
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = str(e)
        )
        
def get_pet_by_id(db, pet_id:int):
    pet_data = db.query(pet).filter(pet.ID == pet_id).first()
    
    
    
    if pet_data is None:
        raise HTTPException(
            status = 404,
            detail= "pet not found: Try Again"
        )
        
    return pet_data


def update_pet(db, pet_id: int, pet_data: PetCreate):
    
    pet_to_update = db.query(pet).filter(
        pet.ID == pet_id).first()

    if pet_to_update is None:
        raise HTTPException(
            status_code=404,
            detail="Pet not found"
        )

    pet_to_update.Pet_Name = pet_data.PetName
    pet_to_update.Species = pet_data.Species
    pet_to_update.Breed = pet_data.Breed
    pet_to_update.Age = pet_data.Age
    pet_to_update.Owner_name = pet_data.Owner_name
    pet_to_update.Owner_phone = pet_data.Owner_phone

    db.commit()
    db.refresh(pet_to_update)

    return pet_to_update


def delete_pet(db, pet_id: int):
    
    pet_to_delete = db.query(pet).filter(
        pet.ID == pet_id
    ).first()

    if pet_to_delete is None:
        raise HTTPException(
            status_code=404,
            detail="Pet not found"
        )

    db.delete(pet_to_delete)
    db.commit()

    return {
        "message": "Pet deleted successfully"
        }