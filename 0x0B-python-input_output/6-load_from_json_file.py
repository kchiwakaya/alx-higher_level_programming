#!/usr/bin/python3
"""loading data from .json files
"""


import json


def load_from_json_file(filename):
    """loads an object from json file containing json string
    """
    with open(filename, encoding='utf-8') as lines:
        return (json.loads(lines.read()))

