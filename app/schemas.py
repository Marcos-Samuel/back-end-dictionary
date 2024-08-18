from pydantic import BaseModel

from datetime import datetime
from typing import List, Optional

class HistoryBase(BaseModel):
    word: str
    added: datetime

class HistoryCreate(HistoryBase):
    pass

class HistoryResponse(HistoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class FavoriteBase(BaseModel):
    word: str
    added: datetime

class FavoriteCreate(FavoriteBase):
    pass

class FavoriteResponse(FavoriteBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    history: List[HistoryResponse] = []
    favorites: List[FavoriteResponse] = []

    class Config:
        orm_mode = True

class SignUp(BaseModel):
    name: str
    email: str
    password: str

class SignIn(BaseModel):
    email: str
    password: str
    
    
    
    
    