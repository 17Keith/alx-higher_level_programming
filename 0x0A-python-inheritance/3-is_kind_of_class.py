#!/usr/bin/python3

"""A function that returns True if the objectve\
    is exactly an instance, otherwise False"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class
    Args:
        obj: object
        a_class: class
    """

    return isinstance(obj, a_class)
