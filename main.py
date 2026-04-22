from fastapi import FastAPI

from backend.api import router
from backend.db import create_tables

app = FastAPI()


@app.on_event("startup")
def startup():
    create_tables()


app.include_router(router)
