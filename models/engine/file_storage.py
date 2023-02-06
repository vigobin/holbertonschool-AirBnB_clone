#!/usr/bin/python3
'''File Storage'''
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        obj_set = obj.__class__.__name__
        FileStorage.__objects[{}] = obj

    def save(self):
        """save obj dictionaries to file"""
        my_dict = {}

        for obj_set, obj in self.__objects.items():
            my_dict[obj_set] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)
    