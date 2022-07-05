#!/usr/bin/python3
"""Writes a string to a text"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8)"""

    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)

        return count
