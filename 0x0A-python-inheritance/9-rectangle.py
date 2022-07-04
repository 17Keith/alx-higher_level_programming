#!/usr/bin/python3
"""A class based on 8-base_geometry.py"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a Rectangle geometric shape"""

    def __init__(self, width, height):
        """Initializes width and height\
            attributes of Rectangle object"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Gets the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
