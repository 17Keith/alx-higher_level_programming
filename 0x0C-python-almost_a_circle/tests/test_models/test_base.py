#!/usr/bin/python3
"""Tests for Base Class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base Class test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test1(self):
        """Create New Instances"""
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(927)
        self.assertEqual(b4.id, 927)
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def test1_1(self):
        """Tests for type instances"""

        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))
