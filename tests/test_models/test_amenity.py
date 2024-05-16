#!/usr/bin/python3

"""
Module for testing the Amenity class.
"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Testing the Amenity class.
    """

    def SetUp(self):
        """
        Creates an instance of the amenity class for testing usage.
        """
        self.myamen = Amenity()

    def test_amen_exists(self):
        """
        Tests the existence and type of amenity object.
        """
        self.assertTrue(self.myamen)
        self.assertEqual(type(self.myamen), Amenity)

    def test_amen_name(self):
        """
        Tests the existence of the amenity attribute.
        """
        self.assertEqual(self.myamen.name, "")

    def TearIt(self):
        """
        Cleans up the instance that was used for testing.
        """
        pass
