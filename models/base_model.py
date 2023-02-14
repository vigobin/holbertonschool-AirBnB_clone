#!/usr/bin/python3
"""The BaseModel class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines the class BaseModel"""
    def __init__(self, *args, **kwargs):
        "args won't be used, Initialize the class use kwargs"
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Updated the print str format for the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        '''deletes the current instance from the storage'''
        from models import storage
        storage.delete(self)

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())
