from contextlib import asynccontextmanager
from database import create_db_and_tables

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import hero


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Load the database and create tables
    create_db_and_tables()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    # "http://localhost:5173/"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hero.router)