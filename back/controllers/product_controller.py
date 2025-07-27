from repository.product_repository import ProductRepository
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from validator.product_validator import ProductCreate, ProductUpdate, Product

class ProductController:
    @staticmethod
    async def get_products():
        products = await ProductRepository.get_products()
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