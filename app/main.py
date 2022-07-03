from fastapi import Depends, FastAPI, status, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.routes import users, visitor
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .database import get_db, engine
from . import schema, models, oauth2, utility


models.Base.metadata.create_all(bind=engine)

app= FastAPI()
origin= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


app.include_router(users.router)
app.include_router(visitor.router)
    
    


