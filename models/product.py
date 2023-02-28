#!/usr/bin/python3
"""This is the Product model module"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """This is the Product Model

    Args:
        BaseModel (Object): The base template model
    """
    __tablename__ = "products"
    shop_id = Column(String(60), ForeignKey('shops.id'), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)
    price = Column(Float(2), nullable=False)
    reviews = relationship("Review", backref='product', cascade='all, delete')


        
