from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100))
    name = Column(String(100))
    description = Column(String(255))
    image = Column(String(255))
    category = Column(String(100))
    price = Column(Numeric)
    quantity = Column(Integer)
    internalReference = Column(String(100))
    shellId = Column(Integer)
    inventoryStatus = Column(String(50))
    rating = Column(Numeric)
    createdAt = Column(Integer)