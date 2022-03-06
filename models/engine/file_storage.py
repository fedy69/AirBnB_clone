#!/usr/bin/python3
"""
The storage file:  serializes instances to a JSON file and
    deserializes JSON file to instances:
"""

import json
import models
import os


class Objects(dict):
    """The class object"""

    def __getitem__(self, key):
        """the get item"""
        try:
            return super(Objects, self).__getitem__(key)
        except Exception as e:
            raise Exception("** no instance found **")

    def pop(self, key):
        """the pop item"""
        try:
            return super(Objects, self).pop(key)
        except Exception as e:
            raise Exception("** no instance found **")


class FileStorage:
    """
    class to serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = Objects()

    def __init__(self):
        """the initialze method"""
        super().__init__()

    def all(self):
        """class to return the class atribute objects"""
        return FileStorage.__objects
