#!/usr/bin/python3
"""A function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Crreats an object from a JSON file"""

    with open(filename, 'r', encoding="utf-8") as f:

        obj = json.load(f)
    return obj
