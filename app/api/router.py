from fastapi import APIRouter

from app.api.v1.endpoints import user, dictionary

router = APIRouter()

router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(dictionary.router, prefix="/dictionary", tags=["dictionary"])
