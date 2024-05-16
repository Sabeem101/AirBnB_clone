#!/usr/bin/python3

"""
Defines all the attributes for the City class.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    The City class stores the name of the city/state.
    """
    state_id = ""
    name = ""
