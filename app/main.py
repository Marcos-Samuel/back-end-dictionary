from fastapi import FastAPI
from app.db import Base, engine
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Fullstack Challenge 🏅 - Dictionary"}
