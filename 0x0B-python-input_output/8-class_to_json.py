#!/usr/bin/python3
"""class to json"""

def class_to_json(obj):
    """create a json representation of an object without using
        json module.
    """
    return repr({key: value for (key, value) in obj.__dict__.items()
                if key in list(obj.__dict__.keys())})
