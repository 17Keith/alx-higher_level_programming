#!/usr/bin/python3
"""A class that inherits list"""


class MyList(list):
    """Implementation of a list"""

    def print_sorted(self):
        """prints the list in ascending order"""

        print(sorted(self))
