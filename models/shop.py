#!/usr/bin/python3
"""This is the shop model"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Shop(BaseModel, Base):
    """This is the Shop Model

    Args:
        BaseModel (Object): The base model or template
    """
    __tablename__ = "shops"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    products = relationship("Product", backref="shop")
    
