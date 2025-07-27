import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app  # Your FastAPI app
from database import Base
from models.user_model import User
from models.product_model import Product
from utils.auth import hash_password
from default_settings import TEST_DATABASE_URL  # Import DATABASE_URL

# -- TEST DATABASE --
engine_test = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

# -- OVERRIDE get_session Dependency --
@pytest.fixture(scope="session")
async def init_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def async_session(init_db):
    async with TestingSessionLocal() as session:
        yield session

# -- ASYNC CLIENT (httpx) --
@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

# -- Sample User Fixture --
@pytest.fixture
async def sample_user(async_session):
    user = User(
        username="testuser",
        firstname="Test",
        email="testuser@example.com",
        hashed_password=hash_password("plainpassword")
    )
    async_session.add(user)
    await async_session.commit()
    return user

# -- Sample Product Fixture --
@pytest.fixture
async def sample_product(async_session):
    product = Product(
        id="prod_123",
        name="Test Product",
        description="A product for testing",
        price=9.99
    )
    async_session.add(product)
    await async_session.commit()
    return product
