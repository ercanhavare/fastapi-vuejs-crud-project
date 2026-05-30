from contextlib import asynccontextmanager
from database import create_db_and_tables

from fastapi import FastAPI
from routers import hero


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Load the database and create tables
    create_db_and_tables()
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(hero.router)