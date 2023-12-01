#!/usr/bin/python3
"""This is the User model"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the User Model

    Args:
        BaseModel (Object): Models template
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False, unique=True)
    shops = relationship("Shop", backref="user")
    

        
        