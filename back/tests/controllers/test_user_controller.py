import pytest
from controllers.user_controller import UserController
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_register_user_controller(async_session: AsyncSession):
    user = await UserController.register_user(
        async_session,
        username="controlleruser",
        firstname="Controller",
        email="controller@example.com",
        password="securepassword"
    )
    assert user.email == "controller@example.com"

@pytest.mark.asyncio
async def test_authenticate_user_controller(async_session: AsyncSession, sample_user):
    user = await UserController.authenticate_user(
        async_session, sample_user.email, "plainpassword"  # assuming plainpassword is correct
    )
    assert user.email == sample_user.email
