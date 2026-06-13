from sqlalchemy.orm import Session
from Models.Owner import Owner
from Schemas.owner import OwnerCreate


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