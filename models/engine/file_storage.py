#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """save obj dictionaries to file"""
        a_dict = {}
        for key, value in self.__objects.items():
            a_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(a_dict, f)

    def reload(self):
        '''If json file exists, convert obj dicts back to instances'''
        try:
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
            for key, val in new_dict.items():
                b_obj = eval(val['__class__'])(**val)
                self.__objects[key] = b_obj
        except FileNotFoundError:
            pass
