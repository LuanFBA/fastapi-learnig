from fastapi import FastAPI
from app.user_route import user_router

app = FastAPI()

app.include_router(user_router)
