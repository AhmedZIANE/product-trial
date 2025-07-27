from sqlalchemy.ext.asyncio import AsyncSession
from repository.user_repository import get_user_by_email, create_user
async def get_user_by_email(session: AsyncSession, email: str):
    return get_user_by_email(session, email)

async def create_user(session: AsyncSession, username: str, firstname: str, email: str, password: str):
    return create_user(session, username, firstname, email, password)