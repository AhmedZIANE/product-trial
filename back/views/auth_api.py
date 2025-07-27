from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from validator.user_validator import UserCreate, UserLogin, TokenResponse
from controllers.user_controller import get_user_by_email, create_user
from utils.auth import verify_password, create_access_token
from database import get_session

class UserAPI:
    def __init__(self):
        self.router = APIRouter(prefix="/api", tags=["auth"])
        self.router.add_api_route("/account", self.register_account, methods=["POST"])
        self.router.add_api_route("/token", self.login_for_token, methods=["POST"])

    async def register_account(self, user: UserCreate, session: AsyncSession = Depends(get_session)):
        existing_user = await get_user_by_email(session, user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        await create_user(session, user.username, user.firstname, user.email, user.password)
        return {"message": "User created successfully"}

    async def login_for_token(self, credentials: UserLogin, session: AsyncSession = Depends(get_session)):
        user = await get_user_by_email(session, credentials.email)
        if not user or not verify_password(credentials.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        
        token = create_access_token(data={"sub": user.email})
        return TokenResponse(access_token=token)
