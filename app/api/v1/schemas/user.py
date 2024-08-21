from pydantic import BaseModel
from typing import List

from app.api.v1.schemas.dictionary import FavoriteResponse, HistoryResponse

class UserBase(BaseModel):
    name: str
    email: str
    
class User(UserBase):
    id: int

class TokenResponse(BaseModel):
    id: int
    name: str
    token: str

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class UserConect(BaseModel):
    email: str
    password: str
    
class HistoryList(BaseModel):
    id: int
    history: List[HistoryResponse] = []
    
class FavoritesList(BaseModel):
    id: int
    favorites: List[FavoriteResponse] = []
    

class UserResponse(UserBase):
    id: int
    history: List[HistoryResponse] = []
    favorites: List[FavoriteResponse] = []

    class Config:
        orm_mode = True
    