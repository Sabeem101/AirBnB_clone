#!/usr/bin/python3

"""
This model defines all common the attributes and models for other classes.
"""

from datetime import datetime
from models import storage
import uuid

class BaseModel:
    """
    The class BaseModel defines all commons attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the attributes.
        """
        ignores_attrs = ["__class__"]
        datetime_attrs = ['created_at', 'updated_at']
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ignores_attrs:
                    continue
                elif key in datetime_attrs:
                    setattr(self, key, datetime.now().fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string that represents the class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the datetime.
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Generates a dictionary representation of an instance.
        """
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = datetime.isoformat(self.created_at)
        mydict["updated_at"] = datetime.isoformat(self.updated_at)
        return mydict
