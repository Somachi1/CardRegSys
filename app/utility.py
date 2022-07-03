from sqlalchemy.orm import Session
from . import models, schema
from passlib.context import CryptContext


pwd_context= CryptContext(schemes=["bcrypt"], deprecated= "auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def create_user(user: schema.UserCreate, db: Session):
    password = hash_password(user.password)
    db_user = models.Users(email=user.email, hashed_password=password, lassra_id=user.lassra_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    





