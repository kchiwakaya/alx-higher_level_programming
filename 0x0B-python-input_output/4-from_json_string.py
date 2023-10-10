#!/usr/bin/python3
""" deserializing json data back to python objects
"""


import json


def from_json_string(my_str):
    """deserializes a JSON string back to a python object
    """
    return json.loads(my_str)

