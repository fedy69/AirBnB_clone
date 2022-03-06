#!/usr/bin/python
""" The class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """the representation of city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the  city"""
        super().__init__(*args, **kwargs)
