#!/usr/bin/python3
"""
Print_square Module:
    Prints out a square to the terminal, made up of #
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    else:
        print("\n".join([
            "".join(["#" for x in range(size)])
            for y in range(size)]))
