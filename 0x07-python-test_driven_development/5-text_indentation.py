#!/usr/bin/python3
"""
Function that Prints a text with 2 new lines after '.', '?', ':'. 
"""


def text_indentation(text):
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    n = "".join([c if c not in "?.:" else c + "\n\n" for c in text])
    print("\n".join([line.strip() for line in n.split("\n")]), end="")
