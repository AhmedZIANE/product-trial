from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.product_model import Product as ProductModel

class ProductRepository:
    @staticmethod
    async def get_products(session: AsyncSession):
        result = await session.execute(select(ProductModel))
        return result.scalars().all()
