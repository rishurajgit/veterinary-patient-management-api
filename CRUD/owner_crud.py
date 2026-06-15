from sqlalchemy.orm import Session
from Models.Owner import Owner
from Schemas.owner import OwnerCreate
from Models.Pets import Pet

#recieves validated data from the schema

def create_owner(db:Session, owner: OwnerCreate):
    new_owner = Owner(
        name = owner.name,
        phone = owner.phone,
        email = owner.email
    )
    
    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    
    return new_owner


def get_pets_by_owner_id(db: Session, owner_id: int):
    
    # pets = db.query(Pet).filter(Pet.owner_id == owner_id).all() #Get pet details by owner id
    pets = db.query(Pet).filter(
    Pet.owner_id == owner_id,
    Pet.is_deleted == False).all()  #only return active pets for the owner
    
    return pets