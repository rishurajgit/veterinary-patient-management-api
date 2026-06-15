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
    visits = db.query(Visit).filter(Visit.pet_id == pet_id).all()  #Get all visit of pets
    
    if len(visits)== 0:  #if no visit found
        raise HTTPException(
            status_code = 404,
            detail = "No Visit Records Found For The Specific Pet"
        )
        
    return visits

def update_visit(
    db: Session,
    visit_id: int,
    visit_data: VisitCreate
):
    try:
        visit = db.query(Visit).filter(
            Visit.id == visit_id
        ).first()

        if visit is None:
            raise HTTPException(
                status_code=404,
                detail="Visit not found"
            )

        visit.visit_date = visit_data.visit_date
        visit.reason = visit_data.reason
        visit.notes = visit_data.notes

        db.commit()
        db.refresh(visit)

        return visit

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
def delete_visit(db: Session, visit_id: int):
    
    visit = db.query(Visit).filter(
        Visit.id == visit_id
    ).first()

    if visit is None:
        raise HTTPException(
            status_code=404,
            detail="Visit Record Not Found"
        )

    db.delete(visit)
    db.commit()

    return {
        "message": "Visit Deleted Successfully"
    }