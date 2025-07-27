from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views.product_api import ProductAPI
from views.auth_api import UserAPI
from database import engine
from models.product_model import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Import your models Base and create tables
        from models.user_model import Base
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def on_shutdown():
    await engine.dispose()

product_api = ProductAPI()
user_api = UserAPI()

app.include_router(product_api.router)
app.include_router(user_api.router)
