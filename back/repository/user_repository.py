from sqlalchemy.future import select
from models.user_model import User
from utils.auth import pwd_context
from sqlalchemy.ext.asyncio import AsyncSession

async def get_user_by_email(session: AsyncSession, email: str):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def create_user(session: AsyncSession, username: str, firstname: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    new_user = User(
        username=username,
        firstname=firstname,
        email=email,
        hashed_password=hashed_password,
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
