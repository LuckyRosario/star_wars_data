import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=False)
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class Entertainment(Base):
    __tablename__ = 'entertainment'
    id = Column(Integer, primary_key=True)
    media_type = Column(String(250), nullable=False)
    rating = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    eyecolor = Column(String(250), nullable=False)
    entertainment_id = Column(Integer, ForeignKey('entertainment.id'))
    entertainment = relationship(Entertainment)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    media_id = Column(Integer, ForeignKey('media.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    character = relationship(Character)
    planet = relationship(Planet)
    user = relationship(User)
    post = relationship(Post)
    entertainment = relationship(Entertainment)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')