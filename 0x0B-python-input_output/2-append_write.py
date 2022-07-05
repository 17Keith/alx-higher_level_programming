#!/usr/bin/python3
"""A function that appends a string at the end of a text\
    file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file and returns the\
        number of characrers added."""

    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)

        return count
