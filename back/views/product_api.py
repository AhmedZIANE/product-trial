from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from controllers.product_controller import ProductController
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

    async def get_products(self):
        try:
            result = await ProductController.get_products()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def create_product(self, product: ProductCreate, session: AsyncSession = Depends(get_session)):
        try:
            return await ProductController.create_product(session, product) 
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_product(self, product_id: int, product: ProductUpdate, session: AsyncSession = Depends(get_session)):
        try:
            await ProductController.update_product(product_id, product, session)
            return {"message": "Product updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    async def delete_product(self, product_id: int, session: AsyncSession = Depends(get_session)):
        try:
            await ProductController.delete_product(product_id, session)
            return {"message": "Product deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))