import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    email = Column(String(250), unique=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    birth_date = Column(Date, nullable=False)
    name = Column(String(250), nullable=False)
    picture = Column(ForeignKey('media.id'))
    created_date = Column(Date, nullable=False)

    def to_dict(self):
        return {}

class FollowRequest(Base):
    __tablename__ = 'follow request'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False, unique=True)
    followed_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False, unique=True)

    def to_dict(self):
        return {}
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    media = Column(Integer, ForeignKey('media.id'))
    caption = Column(String(1000))
    like = Column(Integer)
    comment = Column(String(1000))
    created_date = Column(Date, nullable=False)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    extension = Column(Enum('.jpeg','.mov'), nullable=False)
    timestamp = Column(Date, nullable=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
