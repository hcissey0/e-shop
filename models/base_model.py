#!/usr/bin/python3
"""This is the BaseModel class"""

from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy import Column, String, DateTime

time_format = "%d-%m-%Y %H:%M:%S"

Base = declarative_base()

class BaseModel:
    """This is the BaseModel Class
    """
    
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    image_name = Column(String(128), nullable=True, default="none.jpg")
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """This is the initializer
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """String representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time_format)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time_format)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def save(self):
        """Save the object"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)

    @classmethod
    def query(cls, **kwargs):
        """Searches for a specific object

        Returns:
            obj: The object if found, otherwise None
        """
        if kwargs:
            for obj in models.storage.all(cls).values():
                if all(getattr(obj, k, None) == v for k, v in kwargs.items()):
                    return obj
        return None

    @classmethod
    def all(cls):
        """Returns all objects of the caller class

        Returns:
            list: The list of objects
        """
        return list(models.storage.all(cls).values())

    def __lt__(self, other):
        if isinstance(other, BaseModel):
            return self.name < other.name
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, BaseModel):
            return self.name > other.name
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BaseModel):
            return self.name == other.name
        return NotImplemented
