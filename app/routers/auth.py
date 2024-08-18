from fastapi import APIRouter, Depends, HTTPException
from requests import Session

from app import crud, schemas
from app.auth import create_access_token, verify_access_token, verify_password
from app.db import get_db

router = APIRouter()

@router.post("/signup")
def signup(user: schemas.SignUp, db: Session = Depends(get_db)):
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
def signin(user: schemas.SignIn, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    
    return {
        "id": db_user.id,
        "name": db_user.name,
        "token": f"Bearer {access_token}"
    }
