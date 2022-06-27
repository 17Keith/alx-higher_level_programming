#!/usr/bin/python3
"""
This is a function that adds 2 integers a and b=98 \
    If both a and b are not integers, a TypeError is raised \
        with exeption message 'a must be an integer or b must be an integer' \
            If a and b are floats, they must be casted to integers.
"""


def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
