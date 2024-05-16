#!/usr/bin/python3

"""
A model that creates a unique FileStorage instance for the application.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
