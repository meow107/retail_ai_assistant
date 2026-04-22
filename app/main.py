from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI()   # 👈 THIS IS THE MISSING PIECE

app.include_router(chat_router)