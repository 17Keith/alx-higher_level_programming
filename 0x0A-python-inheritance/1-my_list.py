#!/usr/bin/python3

"""A class: MyList that inherits from list"""

class Mylist(list):
    """Implementation of list"""

    def print_sorted(self):
        """Prints the list in ascending order"""

        print(sorted(self))
