from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from fastapi.staticfiles import StaticFiles
from app.routes.chat import router as chat_router

app = FastAPI()   

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="app/frontend", html=True), name="frontend")
