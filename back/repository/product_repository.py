from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete
from models.product_model import Product as ProductModel 
from validator.product_validator import ProductCreate, ProductUpdate
from database import get_session


class ProductRepository:
    @staticmethod
    async def get_products():
        async for session in get_session():
            result = await session.execute(select(ProductModel))
            return result.scalars().all()

    @staticmethod
    async def create_product(session: AsyncSession, product_data: ProductCreate):
        new_product = ProductModel(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            created_at=product_data.created_at,  
            updated_at=product_data.updated_at   
        )
        session.add(new_product)
        await session.commit()
        await session.refresh(new_product)
        return new_product

    @staticmethod
    async def update_product(session: AsyncSession, product_id: int, product_data: ProductUpdate):
        result = await session.execute(select(ProductModel).where(ProductModel.id == product_id))
        product = result.scalars().first()
        if not product:
            return None
        
        # Mise à jour des champs
        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        
        await session.commit()
        await session.refresh(product)
        return product

    @staticmethod
    async def delete_product(session: AsyncSession, product_id: int):
        result = await session.execute(select(ProductModel).where(ProductModel.id == product_id))
        product = result.scalars().first()
        if not product:
            return False

        await session.delete(product)
        await session.commit()
        return True
