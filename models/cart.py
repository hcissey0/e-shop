#!/usr/bin/python3

from sqlalchemy import Column, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

cart_products = Table('cart_products', Base.metadata,
    Column('cart_id', String(60), ForeignKey('carts.id'), primary_key=True),
    Column('product_id', String(60), ForeignKey('products.id'), primary_key=True)
)

class Cart(BaseModel, Base):
    """_summary_

    Args:
        BaseModel (_type_): _description_
        Base (_type_): _description_
    """
    __tablename__ = 'carts'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    products = relationship('Product', secondary=cart_products, backref='carts')
    total = Column(Float(2), nullable=True, default=0.00)
