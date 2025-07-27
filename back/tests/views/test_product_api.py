import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_get_products_api(async_client: AsyncClient):
    response = await async_client.get("/api/products")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
