from pydantic import BaseModel
from typing import Any, List, TypeVar

T = TypeVar('T')

class PaginationBase(BaseModel):
    totalDocs: int
    page: int
    totalPages: int
    hasNext: bool
    hasPrev: bool

class PaginationResponse(BaseModel):
    results: List[T]
    pagination: PaginationBase
