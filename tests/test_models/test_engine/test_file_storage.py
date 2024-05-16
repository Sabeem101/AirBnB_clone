#!/usr/bin/python3

"""
Test modules for the FileStorage class.
"""

import os
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Class for testing the FileStorage
    """
    def SetUp(self):
        """
        Creates an instance for testing.
        """
        self.FS = FileStorage()
        kwargs = {
                "name": "Test model 1",
                "id": "11",
                "my_number": 1111,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
        }
        self.BM = BaseModel(**kwargs)

        self.test_path = self.FS._FileStorage__file_path
        self.FS.new(self.BM)
        self.FS.save()
        self.FS.reload()
        self.objects_dict = self.FS.all()

    def test_file_path(self):
        """
        Tests the file path class attribute.
        """
        self.assertEqual(self.test_path, "file.json")

    def test_objects_dict(self):
        """
        Tests the objects class attribute.
        """
        self.assertEqual(type(self.objects_dict), dict)

    def test_new(self):
        """
        Tests the instance for new method.
        """
        self.assertIn("BaseModel.11", self.objects_dict)

    def test_save(self):
        """
        Tests the instance save method.
        """
        self.assertEqual(os.path.exists(self.test_path))
        with open(self.test_path, "r", encoding='utf-8') as xfile:
            data = json.load(xfile)
        self.assertIn("BaseModel.11", data)

    def test_reload(self):
        """
        Tests the instance method reload.
        """
        new_FS = FileStorage()
        new_FS.reload()
        new_objects_dict = new_FS.all()
        self.assertEqual(self.objects_dict, new_objects_dict)

    def test_reload_obj(self):
        """
        Tests the instance method to reload an object.
        """
        old_obj = self.objects_dict["BaseModel.11"]
        new_obj = BaseModel(**old_obj.to_dict())
        self.assertEqual(old_obj.to_dict(), new_obj.to_dict())

    def Tearit(self):
        """
        Cleans up the instance that was used for testing.
        """
        try:
            os.remove(self.FS._FileStorage__file_path)
        except FileNotFoundError:
            pass
