#!/usr/bin/python3

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """_summary_

    Args:
        BaseModel (_type_): _description_
        Base (_type_): _description_
    """
    __tablename__ = 'reviews'
    user_id = Column(String(60), ForeignKey('users.id'))
    product_id = Column(String(60), ForeignKey('products.id'))
    text = Column(String(1024), nullable=False)
