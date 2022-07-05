#!/usr/bin/python3
"""A funtion that returns an object"""
import json


def from_json_string(my_str):
    """Rerurns an object represented by a JSON string"""

    return json.loads(my_str)
