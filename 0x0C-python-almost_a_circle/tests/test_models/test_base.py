#!/usr/bin/python3
"""Tests for Base Class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base Class test class"""

    def setUp(self):
        Base._Base__nb_objects = 0
