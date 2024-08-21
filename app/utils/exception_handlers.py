from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    message: str

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"},
    )
