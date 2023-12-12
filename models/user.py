#!/usr/bin/python3
"""This is the User model"""

from models.base_model import BaseModel, Base
from flask_login import UserMixin
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.cart import Cart


class User(BaseModel, Base, UserMixin):
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
    shops = relationship("Shop", backref="user", cascade='all, delete')
    reviews = relationship("Review", backref='user')
    cart = relationship('Cart', uselist=False, backref='user', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.first_name + " " + self.last_name
        self.cart = Cart(name=self.name + "'s cart")