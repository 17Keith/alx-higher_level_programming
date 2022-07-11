#!/usr/bin/python3
"""Contains tests for Base Class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0
