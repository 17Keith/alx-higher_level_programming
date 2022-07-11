#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""

import json
from models.base import Base


class Rectangle(Base):
    """Class describing Recangle, which inherits\
        from Base.
        Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
