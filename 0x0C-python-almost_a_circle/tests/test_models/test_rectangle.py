#!/usr/bin/python3
"""Test Cases for Rectangle Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_2_0(self):
        """Test Rectangle class: check for id."""

        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r4.id, 34)
        r5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r5.id, -5)
        r6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r6.id, 9)

    def test_2_1(self):
        """Test Rectangle class: check for attributes values."""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

    def test_2_2(self):
        """Test class Rectangle: check for missing arguments."""

        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle()
        self.assertEqual(s, str(x.exception))

    def test_2_3(self):
        """Test class Rectangle: check for inheritance."""

        r1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_3_0(self):
        """Test Rectangle class: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            r = Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, "Foo", 3)
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Rectangle(1, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Rectangle(2, 8, 9, -65)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_4_0(self):
        """Test for public method area with normal types."""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(75, 2)
        self.assertEqual(r2.area(), 150)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_4_1(self):
        """Test for public method area with wrong args."""

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(3, 2)
            r1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_5_0(self):
        """Test for public method display."""

        f = io.StringIO()
        r1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_5_1(self):
        """Test for public method display with wrong args."""

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(9, 6)
            r1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))
