#!/usr/bin/python
""" class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The representation of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initial Review"""
        super().__init__(*args, **kwargs)
