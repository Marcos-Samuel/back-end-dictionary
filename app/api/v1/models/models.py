from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    favorites = relationship("Favorite", back_populates="user")
    history = relationship("History", back_populates="user")

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True)
    phonetics = Column(String)  
    meanings = Column(String)  
    license = Column(String)  
    source_urls = Column(String)  

    favorites = relationship("Favorite", back_populates="entry")
    history = relationship("History", back_populates="entry")

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    entry_id = Column(Integer, ForeignKey("entries.id"))

    user = relationship("User", back_populates="favorites")
    entry = relationship("Entry", back_populates="favorites")

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    entry_id = Column(Integer, ForeignKey("entries.id"))
    added = Column(DateTime)

    user = relationship("User", back_populates="history")
    entry = relationship("Entry", back_populates="history")
