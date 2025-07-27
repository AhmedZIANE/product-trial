import pytest
from repository.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

@pytest.mark.asyncio
async def test_create_user(async_session: AsyncSession):
    user = await UserRepository.create_user(
        async_session,
        username="testuser",
        firstname="Test",
        email="testuser@example.com",
        password="hashed_password"
    )
    assert user.email == "testuser@example.com"

@pytest.mark.asyncio
async def test_get_user_by_email(async_session: AsyncSession, sample_user):
    user = await UserRepository.get_user_by_email(async_session, sample_user.email)
    assert user.email == sample_user.email
