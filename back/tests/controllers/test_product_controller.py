from controllers.product_controller import ProductController
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_get_all_products_controller(async_session: AsyncSession, sample_product):
    products = await ProductController.get_products(async_session)
    assert len(products) >= 1
    assert products[0].id == sample_product.id
