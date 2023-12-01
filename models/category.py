from models.base_model import Base, BaseModel

from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

class Category(BaseModel, Base):
    """_summary_

    Args:
        BaseModel (_type_): _description_
        Base (_type_): _description_
    """
    __tablename__ = 'categories'
    products = relationship('Product', backref='tag')
