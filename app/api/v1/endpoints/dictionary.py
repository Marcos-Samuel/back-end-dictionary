from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.crud import crud
from app.auth.auth import get_current_user
from app.db.database import get_db
from app.api.v1.schemas import dictionary, user
from app.api.v1.models.models import Entry

router = APIRouter()

@router.get("/entries/{word}")
def read_entry(word: str, db: Session = Depends(get_db)):

    result = db.query(Entry).filter(Entry.word == word).first()
    if result is None:
        return {"message": "Nenhum resultado encontrado."}
    return result

@router.get("/entries/en", response_model=dictionary.DictionaryList)
def get_entries(search: str = "", limit: int = 10, page: int = 1, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    entries_query = db.query(Entry).filter(Entry.word.ilike(f"%{search}%"))
    total_docs = entries_query.count()
    entries = entries_query.offset(offset).limit(limit).all()
    total_pages = (total_docs + limit - 1) 
    has_next = page < total_pages
    has_prev = page > 1
    results = [dictionary.EntryDetail(word=e.word, definition=e.definition) for e in entries]

    return {
        "results": results,
        "totalDocs": total_docs,
        "page": page,
        "totalPages": total_pages,
        "hasNext": has_next,
        "hasPrev": has_prev,
        "pagination": {
            "limit": limit,
            "offset": offset
        }
    }


@router.get("/en/{word}", response_model=dictionary.EntryDetail)
def get_entry_for_word(word: str, db: Session = Depends(get_db)):
    entry = crud.get_entry(word, db)
    if not entry:
        raise HTTPException(status_code=404, detail="Word not found")
    return entry

@router.post("/en/{word}/favorite", status_code=204)
def add_favorite(word: str, db: Session = Depends(get_db), current_user: user.User = Depends(get_current_user)):
    try:
        crud.add_favorite(db, current_user.id, word)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to add favorite")

@router.delete("/en/{word}/unfavorite", status_code=204)
def remove_favorite(word: str, db: Session = Depends(get_db), current_user: user.User = Depends(get_current_user)):
    try:
        crud.remove_favorite(db, current_user.id, word)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to remove favorite")
