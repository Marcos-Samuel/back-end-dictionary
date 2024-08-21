from typing import Dict
from sqlalchemy.orm import Session
from app.api.v1.models import models
from app.api.v1.schemas import  user 
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.api.v1.models.models import Entry
from app.utils.pagination import paginate
from app.utils.utils import verify_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: user.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if user and verify_password(password, user.password):
        return user
    return None

def crud_get_entries(db: Session, search: str = "", page: int = 1, limit: int = 5) -> Dict:
    query = db.query(Entry).filter(Entry.word.ilike(f"%{search}%")).all()
    items = [{"word": entry.word, "definition": entry.definition} for entry in query]
    return paginate(items, page, limit)