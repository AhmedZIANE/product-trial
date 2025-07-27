import enum
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base
from sqlalchemy import Enum

Base = declarative_base()

class InventoryStatusEnum(enum.Enum):
    INSTOCK = "INSTOCK"
    LOWSTOCK = "LOWSTOCK"
    OUTOFSTOCK = "OUTOFSTOCK"
    
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
    inventoryStatus = Column(Enum(InventoryStatusEnum), nullable=False)
    rating = Column(Numeric)
    createdAt = Column(Integer)
