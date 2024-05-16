#!/usr/bin/python3

"""
The FileStorage class serializes the instances to JSON file and deserializes JSON file to instances.
"""

import json
import os

class FileStorage:
    """
    The FileStorage class.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes the attributes.
        """
        pass

    def all(self):
        """
        Prints the dictionary.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a key value pair for each instance into the objects dictionary.
        """
        obj_class_name = obj.__class__.__name__
        object_id = obj.id
        key = obj_class_name + "." + object_id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects dictionary to the JSON file.
        """
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        try:
            with open(FileStorage.__file_path, "w") as xfile:
                json.dump(new_dict, xfile)
        except Exception:
            pass

    def reload(self):
        """
        Deserializes the JSON file to the objects dictionary.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        objects_dict = {}
        try:
            with open(self.__file_path, "r") as yfile:
                objects_dict = json.load(yfile)
        except Exception:
            objects_dict = {}
            pass
        for key, value in objects_dict.items():
            strclass_name = value["__class__"]
            if strclass_name in classes_dict:
                class_name = classes_dict[strclass_name]
                FileStorage.__objects[key] = class_name(**value)
            else:
                raise TypeError(f"unkown class: {current_class}")
