from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from repository.product_repository import ProductRepository
from validator.product_validator import Product

class ProductAPI:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/api/products", self.get_products, methods=["GET"])

    async def get_products(self):
        async with AsyncSessionLocal() as session:
            products = await ProductRepository.get_products(session)
            # return [Product.from_orm(product) for product in products]
            return products