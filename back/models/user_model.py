from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    firstname = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(128))
