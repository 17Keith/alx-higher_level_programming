#!/usr/bin/python3
"""A class based on 9-rectangle.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implements a Square geometric shape"""

    def __init__(self, size):
        """Initializes width and height attributes of Square object"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
