from repository.product_repository import ProductRepository
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

@pytest.mark.asyncio
async def test_get_products(async_session: AsyncSession, sample_product):
    products = await ProductRepository.get_products(async_session)
    assert len(products) >= 1
    assert products[0].id == sample_product.id
