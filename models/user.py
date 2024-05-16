#!/usr/bin/python3

"""
Defines all the attributes for the User class.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    The User class stores all the private information of the user.
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
