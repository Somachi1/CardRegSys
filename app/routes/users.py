from typing import List, Optional
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schema, models, oauth2, utility
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/createusers", status_code=status.HTTP_201_CREATED, response_model=schema.UserResponse)
def create_user(user: schema.UserCreate, db: Session=Depends(get_db)):
    hashed_password = utility.hash_password(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.dict())
    db.add(new_user)              
    db.commit()       
    db.refresh(new_user)
    
    return new_user


@router.post('/login', response_model=schema.Token)
def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    if not utility.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    return {"access_token": access_token, 'token_type': "bearer"}


@router.get("/card/{lassra_id}")
def get_card_status(lassra_id: int, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):

    user_id=db.query(models.CardInfo).filter(models.CardInfo.lassra_id==lassra_id).first()

    if user_id:
        return {"Lassra_id": user_id.lassra_id,
                "status": user_id.card_status,
                "status_description": user_id.status_descr}
                
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Lassra ID {lassra_id}, was not found")


