from fastapi import APIRouter, Request, Depends, FastAPI, HTTPException, Response, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from datetime import datetime, time, date
import time


router = APIRouter(
    prefix="/visitor",
    tags=['Visitor']
)



@router.get("/ip_counter/{lassra_id}")
def visitor_get_status(request: Request, lassra_id: int, db: Session = Depends(get_db)):
    host = request.client.host
    db_host = models.Visits(visit_ip_address=host)
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    visitor_count= db.query(models.Visits).filter(models.Visits.visit_ip_address==host).count()
    visitor = db.query(models.Visits).filter(models.Visits.visit_ip_address==host).first()

    created_at = visitor.created_at
    
    today_date = date.today()
    created = datetime.strftime(created_at, "%d%b%Y%H%M%S")
    created_at_date = datetime.strptime(created, 
                                 "%d%b%Y%H%M%S")
    created_date = created_at_date.date()
    

    
    


    if visitor_count > 3 and today_date == created_date:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have surpsssed the limit for searches today")

    user_id = db.query(models.CardInfo).filter(models.CardInfo.lassra_id==lassra_id).first()

    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lassra ID {lassra_id}, was not found")  

    return {"Lassra_id": user_id.lassra_id,
                "status": user_id.card_status,
                "status_description": user_id.status_descr}
    
        

    
    

