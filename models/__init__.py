#!/usr/bin/python3
"""This is the initializer for the module"""

from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
