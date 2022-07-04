#!/usr/bin/python3

"""A function that returns a list of\
available attributes and methods of an object"""


def lookup(obj):

    """
    Args:
        obj (Any): object
    Returns:
        list: list of attributes and members
    """

    return dir(obj)
