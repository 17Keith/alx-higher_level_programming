#!/usr/bin/python3

"""A class based on 6-base_geometry.py"""


class BaseGeometry:
    """Empty class"""

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        # if value is not an integer
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        # if value is less or equal to 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
