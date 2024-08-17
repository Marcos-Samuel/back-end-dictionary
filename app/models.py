from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    
    history = relationship('History', back_populates='user')
    favorites = relationship('Favorite', back_populates='user')

class History(Base):
    __tablename__ = 'history'
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, nullable=False)
    added = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='history')

class Favorite(Base):
    __tablename__ = 'favorites'
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, nullable=False)
    added = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='favorites')
