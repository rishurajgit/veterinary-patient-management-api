from sqlalchemy.orm import Session
from Models.Owner import Owner
from Schemas.owner import OwnerCreate
from Models.Pets import Pet
from fastapi import HTTPException
from sqlalchemy import or_


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
    
    
    if len(pets) == 0:
        raise HTTPException(
            status_code=404,
            detail="No pets found for this owner"
        )

    return pets

def get_all_owners(
    db: Session,
    search: str | None = None,
    page: int = 1,
    limit: int = 10,
):

    query = db.query(Owner)

    if search:
        query = query.filter(
            or_(
                Owner.name.ilike(f"%{search}%"),
                Owner.email.ilike(f"%{search}%"),
                Owner.phone.ilike(f"%{search}%"),
            )
        )

    return (
        query
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )


def get_owner_by_id(
    db: Session,
    owner_id: int,
):
    owner = (
        db.query(Owner)
        .filter(Owner.id == owner_id)
        .first()
    )

    if owner is None:
        raise HTTPException(
            status_code=404,
            detail="Owner not found"
        )

    return owner


def update_owner(
    db: Session,
    owner_id: int,
    owner_data,
):

    owner = get_owner_by_id(db, owner_id)

    update_data = owner_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(owner, key, value)

    db.commit()
    db.refresh(owner)

    return owner


def delete_owner(
    db: Session,
    owner_id: int,
):

    owner = get_owner_by_id(db, owner_id)

    db.delete(owner)

    db.commit()

    return {
        "message": "Owner deleted successfully"
    }