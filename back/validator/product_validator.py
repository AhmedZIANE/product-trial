from pydantic import BaseModel
from typing import List, Literal, Optional

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
    updatedAt: Optional[int] = None  # <- make this optional

    model_config = {
        "from_attributes": True
    }


class ProductList(BaseModel):
    products: List[Product]