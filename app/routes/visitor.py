from fastapi import APIRouter, Request, Depends, FastAPI, HTTPException, Response, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

router = APIRouter(
    prefix="/visitor",
    tags=['Visitor']
)



@router.get("/ip_counter/{lassra_id}")
def visitor_get_status(request: Request, lassra_id: int, db: Session = Depends(get_db), limit: int=3):
    
    host = request.client.host
    ip_counter = db.query(models.Visits).filter(models.Visits.visit_ip_address==host).all()

    user_id = db.query(models.CardInfo).filter(models.CardInfo.lassra_id==lassra_id).first()

    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lassra ID {lassra_id}, was not found")
    

    row_count = db.query(models.Visits).count()

    if row_count > 2:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"You have surpassed your maximum search attepmts for the day")
    host = request.client.host
    db_host = models.Visits(visit_ip_address=host)
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    return {"status": user_id.card_status,
            "user_ip": host,
            "status_description": user_id.status_descr}

        

    
    

