from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    firstname: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
