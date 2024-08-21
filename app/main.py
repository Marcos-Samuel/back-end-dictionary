from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.api.cache.cache_utils import clear_cache
from app.api.cache.redis_cache import init_cache
from app.db.database import Base, engine
from app.api.router import router as api_router
from app.utils.exception_handlers import general_exception_handler, http_exception_handler

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing cache...")
    await init_cache()
    yield
    print("Clearing cache...")
    await clear_cache()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Fullstack Challenge 🏅 - Dictionary"}

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)