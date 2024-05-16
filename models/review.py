#!/usr/bin/python3

"""
Defines all attributes for thr Review class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    The Review class stores the description of the place.
    """
    place_id = ""
    user_id = ""
    text = ""
