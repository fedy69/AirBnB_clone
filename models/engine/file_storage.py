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
        """get item"""
        try:
            return super(Objects, self).__getitem__(key)
        except Exception as e:
            raise Exception("** no instance found **")
