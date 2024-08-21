from fastapi import APIRouter, Depends, HTTPException
from requests import Session

from app.api.v1.crud import crud
from app.api.v1.schemas import user
from app.auth.auth import get_current_user
from app.core.security import create_access_token
from app.db.database import get_db

router = APIRouter()

@router.post("/signup")
def signup(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = crud.create_user(db, user)    
    
    access_token = create_access_token(data={"sub": db_user.email})
    
    return {
        "id": db_user.id,
        "name": db_user.name,
        "token": f"Bearer {access_token}"
    }

@router.post("/signin")
def signin(user: user.UserConect, db: Session = Depends(get_db)):
    db_user = crud.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    
    return {
        "id": db_user.id,
        "name": db_user.name,
        "token": f"Bearer {access_token}"
    }

@router.get("/user/me", response_model=user.UserResponse)
def get_user_profile(db: Session = Depends(get_db), current_user: user.User = Depends(get_current_user)):
    return crud.get_user_profile(db, current_user.id)

@router.get("/user/me/history", response_model=user.HistoryList)
def get_user_history(db: Session = Depends(get_db), current_user: user.User = Depends(get_current_user)):
    history = crud.get_user_history(db, current_user.id)
    return {
        "results": history,
        "totalDocs": len(history),
        "page": 1,  
        "totalPages": 1,
        "hasNext": False,
        "hasPrev": False
    }

@router.get("/user/me/favorites", response_model=user.FavoritesList)
def get_user_favorites(db: Session = Depends(get_db), current_user: user.User = Depends(get_current_user)):
    favorites = crud.get_user_favorites(db, current_user.id)
    return {
        "results": favorites,
        "totalDocs": len(favorites),
        "page": 1, 
        "totalPages": 1,
        "hasNext": False,
        "hasPrev": False
    }
