from fastapi import HTTPException
from sqlalchemy.orm import Session

from Models.Visit import Visit
from Schemas.visit import VisitCreate


def create_visit(
    db: Session,
    pet_id: int,
    visit_data: VisitCreate
):

    try:

        # Create visit object
        new_visit = Visit(
            pet_id=pet_id,
            visit_date=visit_data.visit_date,
            reason=visit_data.reason,
            notes=visit_data.notes
        )

        # Save to database
        db.add(new_visit)
        db.commit()
        db.refresh(new_visit)

        return new_visit

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
def get_visits_by_pet_id(db: Session, pet_id: int):
    visits = db.query(Visit).filter(Visit.Pet_id == pet_id).all()  #Get all visit of pets
    
    if len(visits)== 0:  #if no visit found
        raise HTTPException(
            status_code = 404,
            details = "No Visit Records Found For The Specific Pet"
        )
        
    return visits