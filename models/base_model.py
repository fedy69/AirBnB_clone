#!/usr/bin/python3
"""
The base class that defines all common attributes/methods for other classes.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
   The BaseModel class 
    """

    def __init__(self, *args, **kwargs):
        """init the instance of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """class to save the new informations to the class object"""
        self.updated_at = datetime.now()
        models.storage.save()
