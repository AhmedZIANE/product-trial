import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_register_account_api(async_client: AsyncClient):
    response = await async_client.post("/api/account", json={
        "username": "apiuser",
        "firstname": "API",
        "email": "apiuser@example.com",
        "password": "password123"
    })
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.asyncio
async def test_login_for_token_api(async_client: AsyncClient, sample_user):
    response = await async_client.post("/api/token", json={
        "email": sample_user.email,
        "password": "plainpassword"  # assuming this is correct
    })
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
