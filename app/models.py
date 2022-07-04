from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)


class Visits(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, nullable=False)
    visit_ip_address = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class CardInfo(Base):
    __tablename__ = "cardinfo"

    id = Column(Integer, primary_key=True, nullable=False)
    lassra_id= Column(Integer, unique=True, nullable=False)
    card_status =Column(String, nullable=False)
    status_descr= Column(String,nullable=False)





