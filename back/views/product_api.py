from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from controllers.product_controller import ProductController
from validator.product_validator import Product
from repository.product_repository import ProductRepository
from database import get_session
from validator.product_validator import ProductCreate, ProductUpdate, Product
from utils.auth import admin_only


class ProductAPI:
    def __init__(self):
        self.router = APIRouter(prefix="/api", tags=["products"])

        # Routes publiques (ex: liste produits)
        self.router.add_api_route("/", self.get_products, methods=["GET"])

        # Routes admin protégées
        self.router.add_api_route("/", self.create_product, methods=["POST"], dependencies=[Depends(admin_only)])
        self.router.add_api_route("/{product_id}", self.update_product, methods=["PUT"], dependencies=[Depends(admin_only)])
        self.router.add_api_route("/{product_id}", self.delete_product, methods=["DELETE"], dependencies=[Depends(admin_only)])

    async def get_products(self, session: AsyncSession = Depends(get_session)):
        products = await ProductRepository.get_products(session)
        # return [Product.from_orm(p) for p in products]
        return products

    async def create_product(self, product: ProductCreate, session: AsyncSession = Depends(get_session)):
        new_product = await ProductRepository.create_product(session, product)
        # return Product.from_orm(new_product)
        return new_product

    async def update_product(self, product_id: int, product: ProductUpdate, session: AsyncSession = Depends(get_session)):
        updated = await ProductRepository.update_product(session, product_id, product)
        if not updated:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product updated"}

    async def delete_product(self, product_id: int, session: AsyncSession = Depends(get_session)):
        deleted = await ProductRepository.delete_product(session, product_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product deleted"}