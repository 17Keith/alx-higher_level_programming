#!/usr/bin/python3

"""A funtion that adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible"""

    # check if obj contains the __dict__() method
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
