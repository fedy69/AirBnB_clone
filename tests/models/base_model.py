#!/usr/bin/python3
"""
The base class that defines all common attributes/methods.
"""

import uuid
from datetime import datetime
import models
from json import JSONEncoder


class BaseModel:
    """The BaseModel class"""

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

    def to_dict(self):
        """class to return dictionary representaton of the instance"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def __str__(self):
        """class to return the string formated mesg when instance is called"""
        clName = self.__class__.__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """The class JSON encoder
    """

    def default(self, o):
        """ The class default"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
