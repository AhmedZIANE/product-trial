from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views.product_api import ProductAPI
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
        await conn.run_sync(Base.metadata.create_all)

product_api = ProductAPI()
app.include_router(product_api.router)