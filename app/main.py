from fastapi import FastAPI
from .models import Base
from .db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Fullstack Challenge 🏅 - Dictionary"}


