#!/usr/bin/python3
"""This is the Database Storage file"""

from models.base_model import BaseModel, Base
from models.user import User
from models.shop import Shop
from models.product import Product
from models.category import Category
from models.review import Review
from models.cart import Cart
import models
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session


classes = {
    "User": User,
    "Product": Product,
    "Shop": Shop,
    'Category': Category,
    'Review': Review,
    'Cart': Cart
}


class DBStorage():
    """This is the db storage class"""

    __engine = None
    __session: Session = None

    def __init__(self) -> None:
        """This is the initializer"""
        # ESHOP_MYSQL_USER = os.getenv('ESHOP_MYSQL_USER')
        # ESHOP_MYSQL_PWD = os.getenv('ESHOP_MYSQL_PWD')
        # ESHOP_MYSQL_HOST = os.getenv('ESHOP_MYSQL_HOST')
        # ESHOP_MYSQL_DB = os.getenv('ESHOP_MYSQL_DB')

        # This will be remove during production
        # and the above will be used.
        ESHOP_MYSQL_USER = 'eshop_user'
        ESHOP_MYSQL_PWD = 'eshop_pass'
        ESHOP_MYSQL_HOST = 'localhost'
        ESHOP_MYSQL_DB = 'eshop_db'
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            ESHOP_MYSQL_USER, ESHOP_MYSQL_PWD,
            ESHOP_MYSQL_HOST, ESHOP_MYSQL_DB
        ))

    def new(self, obj):
        """create a new object"""
        self.__session.add(obj)

    def all(self, cls=None):
        """Get all objects or all of cls"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def delete(self, obj=None):
        """deletes an obj"""
        if obj is not None:
            self.__session.delete(obj)
    
    def save(self):
        """Save everything"""
        self.__session.commit()

    def reload(self):
        """refreshes the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def remove(self):
        self.__session.remove()

    def close(self):
        self.__session.remove()

    def count(self, cls=None):
        if cls and (cls in classes.keys() or cls in classes.values()):
            return len(models.storage.all(cls).values())
        return len(models.storage.all().values())
