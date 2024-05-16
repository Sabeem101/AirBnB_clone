#!/usr/bin/python3

"""
Defines all the attributes for the Place class.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    The Place class stores all the attributes and infos.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longtitude = float(0.0)
    amenity_ids = []
