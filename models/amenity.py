#!/usr/bin/python3

"""
Defines all the attributes for the Amenity class.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    The Amenity class stores all the types of amenities available at a place.
    """
    name = ""
