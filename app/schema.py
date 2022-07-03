from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    email: str
    

class UserCreate(User):
    password: str
    
    

class UserResponse(User):
    password: str
    pass

    class Config:
        orm_mode = True
    



class Visits(BaseModel):
    lassra_id: int


class VisitsResponse(Visits):
    ip_address: int
    visit_count: int

    class Config:
        orm_mode = True




class CardInfo(BaseModel):
    lassra_id: int
    card_status: str
    status_desc: str


class CardInfoResponse(CardInfo):
    pass

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]= None