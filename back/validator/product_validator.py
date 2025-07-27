from pydantic import BaseModel
from typing import List, Literal, Optional
from datetime import datetime


class Product(BaseModel):
    id: int
    code: str
    name: str
    description: str
    image: str
    category: str
    price: float
    quantity: int
    internalReference: str
    shellId: int
    inventoryStatus: Literal["INSTOCK", "LOWSTOCK", "OUTOFSTOCK"]
    rating: float
    createdAt: int
    updatedAt: Optional[int] = None

    model_config = {
        "from_attributes": True
    }

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    updated_at: Optional[datetime] = None

class ProductList(BaseModel):
    products: List[Product]