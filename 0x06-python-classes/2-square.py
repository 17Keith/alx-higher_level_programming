#!/usr/bin/python3
"""This is a class that defines a Square based on 0-square.py"""


class Square(object):
    """Class:Square"""
    def __init__(self, size=0):
        """Initialization of Class"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
