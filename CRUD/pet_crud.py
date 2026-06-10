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