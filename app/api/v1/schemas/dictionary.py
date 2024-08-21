from pydantic import BaseModel
from datetime import datetime
from typing import List

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

class EntryDetail(BaseModel):
    word: str
    definition: str 
    
class DictionaryList(BaseModel):
    results: List[EntryDetail]
    totalDocs: int
    page: int
    totalPages: int
    hasNext: bool
    hasPrev: bool
    pagination: dict
  

    class Config:
        orm_mode = True
