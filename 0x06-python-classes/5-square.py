#!/usr/bin/python3
"""This is a class that defines a Square based on 4-square.py"""


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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Gets the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
        for s in range(self.__size):
            for os in range(self.__size):
                print('#', end='')
            print('')
