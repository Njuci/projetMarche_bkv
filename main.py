
# main.py
from fastapi import FastAPI
from api.user import router as users_router

app = FastAPI()

app.include_router(users_router, prefix="/api")
