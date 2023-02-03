#!/usr/bin/python3
"""The BaseModel class"""
from datetime import datetime
import uuid


class BaseModel:
    """Defines the class BaseModel"""
    def __init__(self):
        "Initialize the class"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Updated the print str format for the class"""
        return ("[{}], ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
